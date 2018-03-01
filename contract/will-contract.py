from boa.blockchain.vm.Neo.Runtime import CheckWitness
from boa.blockchain.vm.Neo.Storage import GetContext, Put, Delete, Get
from boa.code.builtins import concat


def authorization_check(input_inheritage_hash):
    """
    Use CheckWitness to check matching of caller and person authorized to
    the registered inheritage.
    """

    legal_entity = Get(GetContext, input_inheritage_hash)

    legal_entity_is_authorized = CheckWitness(legal_entity) # Boolean

    if not legal_entity_is_authorized:
        print('Authorization failed.')
    else:
        print('Authorization confirmed.')

    return legal_entity_is_authorized


def Main(operation, args):
    """
    Calling the Main function of this NEO smart contract enables registering a
    last will or inheritage hash. It also allows to set heirs and transfers of
    inheritage, which works exactly like the NEO licensing contracts.
    """

    caller = args[0] # used with CheckWitness below to conform authorization
    caller_is_authorized = CheckWitness(caller) # Boolean

    if not caller_is_authorized:
        print('Action denied.')
        return False

    print('Action granted.')
    input_inheritage_hash = args[1]
    caller_with_input_will_or_inheritage_hash = concat(caller, input_inheritage_hash)

    # Set testator_or_heir to the optional third argument or use the caller
    if len(args) == 3:
        testator_or_heir = args[2]
        legal_entity_with_inheritage_hash = concat(testator_or_heir, input_inheritage_hash)
    else:
        testator_or_heir = caller
        legal_entity_with_inheritage_hash = caller_with_input_will_or_inheritage_hash


    if operation != None:


        if operation == 'RegisterWillOrInheritage':        
            """
            Register will or equity specification document to the contract caller.
            """
            storage_occupying_hash = Get(GetContext, input_inheritage_hash)

            if not storage_occupying_hash:
                Put(GetContext, input_inheritage_hash, caller)

                print("Your inheritage was successfully registered.")

                return True


        if operation == 'SetInheritage':        
            """
            Set a testator_or_heir for a registered equity .
            """
            if authorization_check(input_inheritage_hash):
                Put(GetContext, legal_entity_with_inheritage_hash, testator_or_heir)

                print("The inheritage was successfully set to legal entity.")

                return True


        if operation == 'QueryInheritage':
            """
            Quiery the legal testator_or_heir of an inheritage
            """
            legal_testator_or_heir = Get(GetContext, legal_entity_with_inheritage_hash)

            if legal_testator_or_heir:
                return  legal_testator_or_heir 


        if operation == 'CancelInheritage':
            if authorization_check(input_inheritage_hash):
                testator_or_heir_to_del = args[2]

                inheritage_to_be_removed = concat(testator_or_heir_to_del, input_inheritage_hash)
                Delete(GetContext, inheritage_to_be_removed)

                print("The inheritance was successfully removed from the will.")

                return True


        if operation == 'ChangeInheritage':
            legal_entity = Get(GetContext, caller_with_input_will_or_inheritage_hash)

            if legal_entity:
                is_authorized_legal_entity = CheckWitness(legal_entity)

                if is_authorized_legal_entity:
                    changed_testator_or_heir = args[2]
                    changed_testator_with_input_inheritage_hash = concat(changed_testator_or_heir, input_inheritage_hash)
                    Delete(GetContext, caller_with_input_will_or_inheritage_hash)
                    Put(GetContext, changed_testator_with_input_inheritage_hash, changed_testator_or_heir)

                    print("Your will has changed.")

                    return True


        return False

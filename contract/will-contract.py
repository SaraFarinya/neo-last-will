from boa.blockchain.vm.Neo.Runtime import CheckWitness
from boa.blockchain.vm.Neo.Storage import GetContext, Put, Delete, Get
from boa.code.builtins import concat


def authorization_check(input_inheritage_datum):
    """
    Use CheckWitness to check matching of caller and
    entity authorized to the registered inheritage.
    """

    legal_entity = Get(GetContext, input_inheritage_datum)

    legal_entity_is_authorized = CheckWitness(legal_entity) # Boolean

    if not legal_entity_is_authorized:
        print('Authorization failed.')
    else:
        print('Authorization confirmed.')

    return legal_entity_is_authorized


def Main(operation, args):
    """
    Calling the Main function of this NEO smart contract enables registering
    a last will or inheritage datum. It also allows to set heirs and transfers
    of inheritage, which works exactly like the NEO licensing contracts.
    """

    caller = args[0] # used with CheckWitness below to conform authorization
    caller_is_authorized = CheckWitness(caller) # Boolean

    if not caller_is_authorized:
        print('Action denied.')
        return False

    print('Action granted.')
    input_inheritage_datum = args[1]
    caller_with_input_will_or_inheritage_datum = concat(caller, input_inheritage_datum)

    # Set testator_or_heir to the optional third argument or use the caller
    if len(args) == 3:
        testator_or_heir = args[2]
        legal_entity_with_inheritage_datum = concat(testator_or_heir, input_inheritage_datum)
    else:
        testator_or_heir = caller
        legal_entity_with_inheritage_datum = caller_with_input_will_or_inheritage_datum


    if operation != None:


        if operation == 'RegisterWillOrInheritage':        
            """
            Register will or equity specification 
            document to the contract caller.
            """
            storage_occupying_name = Get(GetContext, input_inheritage_datum)
            
            print(storage_occupying_name)

            if not storage_occupying_name:
                Put(GetContext, input_inheritage_datum, caller)

                print("Your inheritage was successfully registered.")

                return True


        if operation == 'SetInheritage':        
            """
            Set a testator_or_heir for a registered equity.
            """
            if authorization_check(input_inheritage_datum):
                Put(GetContext, legal_entity_with_inheritage_datum, testator_or_heir)

                print("The inheritage was successfully set to legal entity.")

                return True


        if operation == 'QueryInheritage':
            """
            Quiery the legal testator_or_heir of an inheritage.
            """
            legal_testator_or_heir = Get(GetContext, legal_entity_with_inheritage_datum)

            if legal_testator_or_heir:
                return  legal_testator_or_heir 


        if operation == 'CancelInheritage':
            if authorization_check(input_inheritage_datum):
                testator_or_heir_to_del = args[2]

                inheritage_to_be_removed = concat(testator_or_heir_to_del, input_inheritage_datum)
                Delete(GetContext, inheritage_to_be_removed)

                print("The inheritance was successfully removed from the will.")

                return True


        if operation == 'ChangeInheritage':
            legal_entity = Get(GetContext, caller_with_input_will_or_inheritage_datum)

            if legal_entity:
                is_authorized_legal_entity = CheckWitness(legal_entity)

                if is_authorized_legal_entity:
                    changed_testator_or_heir = args[2]
                    changed_testator_with_input_inheritage_datum = concat(changed_testator_or_heir, input_inheritage_datum)
                    Delete(GetContext, caller_with_input_will_or_inheritage_datum)
                    Put(GetContext, changed_testator_with_input_inheritage_datum, changed_testator_or_heir)

                    print("Your will has changed.")

                    return True


        return False

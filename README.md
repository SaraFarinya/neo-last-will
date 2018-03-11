# neo-last-will

Use the blockchain to empower old people to [administer their own legacy](https://en.wikipedia.org/wiki/Holographic_will) in a permanent and lasting way. Enable anyone to use smart technology and feel secure about what happens after they are not around anymore.

<p align="center">
 <img src="https://i.imgur.com/rVA7z2Q.png" width="500" height="500">
</p>

## neo-python-gui-extension
The [neo-python](https://github.com/CityOfZion/neo-python) cli is all you need to interact with the blockchain and your contract and it can be operated with the graphical user interface. The gui also has a tab to author documents and computate hash which can be used as input to the last-will-contract.

Watch the demo video:

<p align="center">
https://youtu.be/ajjCcCNYcV0
</p>

Screenshot of video:

<p align="center">
 <img src="https://i.imgur.com/MQ4oEVK.jpg">
</p>

### how to install
  * install neo-python and PyQt5
  * copy `prompty.py` [and](https://github.com/SaraFarinya/neo-last-will/tree/master/neo-python) `gui_memory.json` into neo-python/
  * copy the [HelperGUI](https://github.com/SaraFarinya/neo-last-will/tree/master/neo-python/neo/Prompt/HelperGUI) directory to neo-python/neo/Prompt

Note: On the last dApp day, a new neo-python branch was merged in, which changed code around the closing of the reactor module. There is also a new line for the gui there, but merging those requires fixing a threading issue first which I have to fix and push later. For those reading this in some time after this day, simply copypaste the lines from the prompt.py - it's just 10 new lines and I've marked those with a tag in a comment `# >>>`. If people like the gui, I can make a PR too. Right now I'm working on more hotkeys and direct SC support functionality. 
Basically, the only difference is the following code branch in `prompt.py`:
```python
       if self.gui_on:
            result = self.gui_result("gui> ")
       else:
            try:
                result = prompt("neo> ", ...
                
       command, arguments = self.input_parser.parse_input(result)
       ...
       
       elif command == 'testinvoke':
            self.test_invoke_contract(arguments)
       elif command == 'gui':
            self.gui_on = True
       ...
```
It can also be tested in isolation with the [test script](https://github.com/SaraFarinya/neo-last-will/blob/master/neo-python/neo/Prompt/HelperGUI/Test.py) that emulates the prompt loop. The persistent memory is saved in a json file and currenly reciding in the neo-python root. Also, if you're not on a Mac, to have the gui listen to keyboard keys (the Enter and Escape key in particular), you might have to change the OS dependent [config file](https://github.com/SaraFarinya/neo-last-will/blob/master/neo-python/neo/Prompt/HelperGUI/Config.py). 

## smart-contract
Calling the `Main(operation, args)` function of [this NEO smart contract written in Python](https://github.com/SaraFarinya/neo-last-will/blob/master/contract/will-contract.py) enables registering a last will or inheritage hash. It also allows to set heirs and transfers of inheritage, which works exactly like the NEO licensing contracts.

Enter an operation and an args list:
  * operation ... `RegisterWillOrInheritage`, `SetInheritage`, `QueryInheritage`, `CancelInheritage`, `ChangeInheritage`
  * 1st arg ... sender legal entity hash
  * 2nd arg ... will or inheritage hash
  * 3rd arg ... extra legal entity hash
  
The contract was developed and tested with the neo-python-privatenet, but there is now a deployed contract on the NEO testnet with the hash `0x5a8549de307df54af7c7259eb2cf922d495de0e3` which was deployed with gui-developer. 
 
Please write issues for questions.

## roadmap
  * include inheritage funds in will contract with verify-trigger logic
  * find most efficient way to store data on blockchain
  * learn about @AbeIgnocious refactoring strategies
  * a threading issue with the `reactor` module must be fixed to use the GUI with blocks

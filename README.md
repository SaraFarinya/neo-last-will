# neo-last-will

Use the blockchain to empower old people to administer their legacy in a secure and permanent way.

<p align="center">
 <img src="https://i.imgur.com/rVA7z2Q.png" width="500" height="500">
</p>

## neo-python-gui-extension
The neo-python cli can be operated with the graphical user interface. The gui also has a tab to author documents and computate hash which can be used as input to the last-will-contract.

Watch the demo video:

<p align="center">
https://youtu.be/ajjCcCNYcV0
</p>

<p align="center">
 <img src="https://i.imgur.com/MQ4oEVK.jpg">
</p>

### how to install
  * install neo-python and PyQt5
  * copy `prompty.py` and `gui_memory.json` into neo-python/
  * copy the HelperGUI directory to neo-python/neo/Prompt

Note: On the last dApp day, a new neo-python branch was merged in that changed code around the exiting of the reactor module. There is also a new line for the gui, but merging those requiring fixing a threading issue first which I'll have to fix and push later. For those reading this in some time after this day, just copypaste the just lines from the prompt.py - it's just 12 new lines and I've marked those with a tag in a comment `# >>>`. If people like the gui, I can make a PR too. Right now I'm working on more hotkeys and direct SC support functionality. Basically, the only difference is the following code branch in `prompt.py`:
```python
       while self.go_on: # >>>
            if self.gui_on:
                print('gui> ')
                self.show()
                result = self.gui_result()
            else:
                try:
                    result = prompt("neo> ", 
                    ...
```
If you're not on a Mac, to have the gui listen to keyboard keys (the Enter and Escape key in particular), you might have to change the OS dependent config file found in the HelperGUI folder. 

## smart-contract
Calling the `Main` function of this NEO smart contract enables registering a last will or inheritage hash. It also allows to set heirs and transfers of inheritage, which works exactly like the NEO licensing contracts.

Enter an operation and an args list:
  * operation = `QueryInheritage`, `RegisterInheritage`, `SetInheritage`, `CancelInheritage`, `ChangeInheritage`
  * 1st arg = sender legal entity hash
  * 2nd arg = will or inheritage hash
  * 3nd arg = extra legal entity hash
  
The contract was developed and tested with the neo-python-privatenet, but there is now a deployed contract on the NEO testnet with the hash `0x5a8549de307df54af7c7259eb2cf922d495de0e3` which was deployed with gui-developer. 
 
Please write issues for questions.

## roadmap
  * a threading issue with the `reactor` module must be fixed to use the GUI with blocks
  * find most efficient way to store data on blockchain
  * include inheritage funds in will contract with verify logic

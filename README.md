# Creality-Box-Upload
Python script that automatically uploads gcode to crealitycloud.com

## General Setup

To use the script you will need an installation of Python 3 and you will have to have the required libraries installed.
Use Terminal or Command Prompt or whatever command-line emulator you use on your computer to install Selenium.

Go through the Python file and customise as needs be.
For Mac you can use an Automator Quick Action to just right click on the saved gcode files.
For other devices you will need to run the python script with the file input window.


## Automator Quick Action Setup

1. Open Automator and create a new document and select "Quick Action"
2. Edit the workflow input (at the top) so that the "Workflow recieves current" is set to "files or folders"
3. Drop in a "Run Shell Script" action and set the "Shell:" to "/usr/local/bin/python3", and set "Pass input:" to "as arguments"
4. Paste the python code into the text box (after you have made your specific changes to the python script)
5. Save the Automator Quick Action and now you'll be able to right click on any gcode file and upload it to Creality Cloud

The Automator document should be set up as shown in the image below:

<img width="1652" alt="image" src="https://user-images.githubusercontent.com/130921240/233007417-691428d2-53f2-48aa-b2b6-da31b8b8ea8e.png">


For Mac Automator, Python needs to be installed in your bash_profile folder. If you get a "Python command not found" error when trying to run the Quick Action run the following command in Terminal: ```echo "alias python=/usr/bin/python3" >> ~/.bash_profile```

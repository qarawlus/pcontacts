# PContacts 
Python YAML Address Book tool 

This tool reads and writes to a YAML file to store contact entries. 
Each contact stored has a name, an email field, and a number field. 

To install this tool, simply navigate to the project's folder, run the following command in your command line tool: 

``` python setup.py install ```

Afterthat, the module is installed as a package.

The module's main executable can then be executed in a command line environment by running the "pcontacts.py" file inside the PContacts folder. 

Example:
```python pcontacts.py --list```
The above example will list all the contact entries currently available in the YAML file. 

The options available to the user for running the program are:

```--list or -l```: this lists the current contacts in the contacts book file.
```--show ContactName```: this shows the details of the contact specified, if the contact does not exist, the program will simply state that.

```--add ContactName --number "0123456789" --email "test@example.com"``` will add a new contact to the list of contacts. The YAML file will be updated accordingly. 

```--file PATH_TO_FILE``` This option can be used alongside other commands if the user has a different file that he/she wishes to use instead of the current file. This has to be set everytime a command is requested. The permanent method is to change the path in the source file of the main executable. 

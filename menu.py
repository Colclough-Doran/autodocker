from autoDocker import *
from fileHandler import *
import sys

class Menu():
    
    def mainMenu(self):
        #try:        
        userInput = input('Please select from the menu below \n' +
               '[1] Display container list \n' +
                '[2] Create new containers \n' +
                '[3] Delete one or more containers \n' +
                '[4] Start a container \n' +
                '[5] Stop a container \n' +
                '[6] Exit AutoDocker \n' +
                'User input: ')

        if userInput == 1:
            FileHandler().readContainerList(AutoDocker().containerListFile)
            self.mainMenu()
        elif userInput == 2:
            createRange = input('\nHow many containers do you wish to create? ')
            FileHandler().createContainer(createRange)
        elif userInput == 3:
            deleteRequest = input('\nWhat container do you want to delete? ')
            FileHandler().deleteContainer(deleteRequest)
        elif userInput == 4:
            AutoDocker().startContainer()
        elif userInput == 5:
            AutoDocker().stopContainer()
        elif userInput == 6:
            sys.exit('\nGoodbye\n')
        else:
            print("\nThat is not a valid entry. Try again.\n")
            self.mainMenu()
        #except:
          #  print("That is not a valid entry. Try again.!!")
           # self.mainMenu()


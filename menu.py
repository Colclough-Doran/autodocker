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
            AutoDocker().displayContainers()	    
            self.mainMenu()
        elif userInput == 2:
            userCrInput = input('\nDo you wish to create a [1]Default server or [2]Custom name? ')
            
            if userCrInput == 1:
                userCrConInput = input('\nHow many default containers do you want to create? ')
            elif userCrInput == 2:
                userCrConInput = raw_input('\nPlease enter the name of the custom server: ')

            AutoDocker().createContainer(userCrConInput)
            self.mainMenu()
        elif userInput == 3:
            deleteRequest = input('\nWhat container do you want to delete? ')
            AutoDocker().deleteContainer(deleteRequest)
            self.mainMenu()
        elif userInput == 4:
            AutoDocker().startContainer()
            self.mainMenu()
        elif userInput == 5:
            AutoDocker().stopContainer()
            self.mainMenu()
        elif userInput == 6:
            sys.exit('\nGoodbye\n')
        else:
            print("\nThat is not a valid entry. Try again.\n")
            self.mainMenu()
        #except:
          #  print("That is not a valid entry. Try again.!!")
           # self.mainMenu()


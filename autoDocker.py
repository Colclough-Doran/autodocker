import os


class AutoDocker():

    containerListFile = 'containerlist.csv'    
    servName = 'sv-centos-{}'
    sudoPassword = ''
    sudoCommand = 'echo {}|sudo -S docker {}'
  

    def createContainer(self, userCrConInput):
        print(type(userCrConInput))
        createDefaultCommand = 'run -d -t --name ' +self.servName+ ' centos'
        createCustomCommand = 'run -d -t --name ' +userCrConInput+ ' centos'
        
        if type(userCrConInput) is int:
            for i in range(userCrConInput):
                if i+1 < 10:
                    os.system(self.sudoCommand.format(self.sudoPassword, createDefaultCommand.format('0'+str(i+1))))  
                else:           
                    os.system(self.sudoCommand.format(self.sudoPassword, createDefaultCommand.format(str(i+1))))  

        else:
           os.system(self.sudoCommand.format(self.sudoPassword, createCustomCommand))
    
    def createContainerList(self):
        contrainerListCommand = 'ps > {}'
        os.system(self.sudoCommand.format(self.sudoPassword, contrainerListCommand.format(self.containerListFile)))
    
    
    def deleteContainer(self, deleteRequest):
        deleteCommand = 'container rm -f ' +self.servName


    def displayContainers(self):
	    displayContainerCommand = 'ps'
	    os.system(self.sudoCommand.format(self.sudoPassword, displayContainerCommand))

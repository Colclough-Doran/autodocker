class AutoDocker():
    import os


    containerListFile = 'containerlist.csv'    
    servName = 'sv-centos-{}'
    sudoPassword = ''
    sudoCommand = 'echo {}|sudo -S docker {}'
  

    def createContainer(self, createRange):
        createCommand = 'run -d -t --name ' +self.servName+ ' centos'
        for i in range(createRange):
            if i+1 < 10:
                os.system(self.sudoCommand.format(self.sudoPassword, createCommand.format('0'+str(i+1))))  
            else:                         
                os.system(self.sudoCommand.format(self.sudoPassword, createCommand.format(str(i+1))))  
    
    
    def deleteContainer(self, deleteRequest):
        deleteCommand = 'container rm -f ' +self.servName


    def createContainerList(self):
        contrainerListCommand = 'ps > {}'
        os.system(self.sudoCommand.format(self.sudoPassword, contrainerListCommand.format(self.containerListFile)))

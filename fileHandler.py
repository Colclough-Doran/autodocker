class FileHandler():

    
    def readContainerList(self, containerListFile):
        fileHandler = open(containerListFile, 'r')
        containerlist = []


        for lines in fileHandler.readlines():
            lines = lines[::-1]
            tmp = lines[:lines.find(' ')]
            lines = tmp[::-1]
            containerlist.append(lines.strip())
        
    
        fileHandler.close()     
        containerlist.remove(containerlist[0])

        return(containerlist)

import os
import pathlib

def DirectoryItems(directories, whitelist):
    '''List all the directories and files within a specified path
    
    Args:
        directories (list): List all the items from specified directories
        whitelist (list): Whitelist of all the extensions
    '''

    directoryItems = []

    # Loop-over all the directories
    for directory in directories:
        # Loop-over all the items within a directory
        for item in os.listdir(directory):
            # Loop-over all the whitelisted extensions
            for white in whitelist:
                if item.endswith(white):
                    pathToFile = os.path.join(directory,item)
                    directoryItems.append(pathToFile)
    return directoryItems

directories = ["C:\\Users\\joost\\Downloads","D:\\tmp"]
whitelist = [".txt"]

dirItems = DirectoryItems(directories,whitelist)

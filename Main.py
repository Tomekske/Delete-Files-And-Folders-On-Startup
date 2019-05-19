import os
import pathlib
import json
from dataclasses import dataclass

@dataclass
class Config:
    '''POCO class for config data'''

    Directories: str = ""
    Whitelist: str = ""
    Folders: bool = False

def DirectoryItems(directories, whitelist, folders):
    '''List all the directories and files within a specified path
    
    Args:
        directories (list): List all the items from specified directories
        whitelist (list): Whitelist of all the extensions
        fodlers (boolean): Check if folders should be deleted
    Returns:
        (list): List of all directory items
    '''

    directoryItems = []

    # Loop-over all the directories
    for directory in directories:
        # Loop-over all the items within a directory
        for item in os.listdir(directory):
            # Full path lenght to an item
            pathToItem = os.path.join(directory,item)

            # Check if folders should be deleted
            if folders:
                # Check if item is a folder
                if os.path.isdir(pathToItem):
                    directoryItems.append(pathToItem)
            # Loop-over all the whitelisted extensions
            for white in whitelist:
                if item.endswith(white):
                    directoryItems.append(pathToItem)
                    
    return directoryItems

with open('config.json') as f:
    data = json.load(f)
    config = Config(data['Directories'],data['Whitelist'],data['Folders'])

dirItems = DirectoryItems(config.Directories,config.Whitelist, config.Folders)

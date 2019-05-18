import os
import pathlib
import json
from dataclasses import dataclass

@dataclass
class Config:
    '''POCO class for config data'''
    
    Directories: str = ""
    Whitelist: str = ""

def DirectoryItems(directories, whitelist):
    '''List all the directories and files within a specified path
    
    Args:
        directories (list): List all the items from specified directories
        whitelist (list): Whitelist of all the extensions
    Returns:
        (list): List of all directory items
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

with open('config.json') as f:
    data = json.load(f)
    config = Config(data['Directories'],data['Whitelist'])

dirItems = DirectoryItems(config.Directories,config.Whitelist)

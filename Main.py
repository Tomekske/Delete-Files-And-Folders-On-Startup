import os
import pathlib
import json
from dataclasses import dataclass
import logging

@dataclass
class Config:
    '''POCO class for config data'''

    Directories: str = ""
    Whitelist: str = ""
    Folders: bool = False
    Logging: str = ""

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

    # logging configuration
    logging.basicConfig(level=logging.INFO,filename=config.Logging, filemode='a', format='[%(asctime)s] - [%(levelname)s] - %(message)s', datefmt='%d-%m-%y %H:%M:%S')

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
                    logging.info(f'[DIR]  - [{pathToItem}]')
            # Loop-over all the whitelisted extensions
            for white in whitelist:
                if item.endswith(white):
                    directoryItems.append(pathToItem)
                    logging.info(f'[FILE] - [{pathToItem}]')

    return directoryItems

with open('config.json') as f:
    # Load data from file
    data = json.load(f)

    # Prepare config object
    config = Config(data['Directories'],data['Whitelist'],data['Folders'], data["Logging"])

dirItems = DirectoryItems(config.Directories,config.Whitelist, config.Folders)

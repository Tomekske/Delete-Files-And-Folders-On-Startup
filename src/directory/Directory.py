import os
import logging
import src.directory.Delete as dl
import src.logging.Message as logger
import src.guard.Guard as grd
import src.config.Config

class Directory:
    def __init__(self, directory, config):
        '''Constructor of the directory class
        
        Args:
            directory (list): List of all directories to scan for items to delete
            config (Config): Config object containing configuration file information
        '''

        self.directory = directory
        self.config = config

        # Check whether path exists
        grd.Guard.PathExist(self.config.Logging)
        # Check whether config value is empty
        grd.Guard.IsNotEmpty(self.config.Logging,"whitelist", self.config.Whitelist)

    def DeleteItems(self):
        '''Delete a folder item'''

        # Loop over all items within a directory
        for item in os.listdir(self.directory):
            # Get Absolute file path
            path = self.__AbsolutePath(item)

            # Check whether file exists
            grd.Guard.PathExist(path, self.config.Logging)

            # Check if whitelisted items should be deleted
            self.__WhitelistItems(path)

            # Check if folders should be deleted
            if self.config.Folders:
                self.__FolderItems(path)

    def __WhitelistItems(self, path):
        '''Function to delete only whitelisted extensions
        
        Args:
            path (string): Name of the directory item
        '''

        # Loop over all whitelisted items
        for white in self.config.Whitelist:
            # Check if the item ends with a whitelisted extension
            if path.endswith(white):
                try:
                    # Delete the file 
                    dl.Delete.File(path)
                    # Log delete operation
                    logger.Message.File(self.config.Logging, path)
                except OSError as error:
                    # Log any errors
                    logger.Message.Error(self.config.Logging, error)

    def __FolderItems(self, path):
        '''Function to delete folders within a directory
        
        Args:
            path (string): Name of the directory item
        '''

        # Check if item is a folder
        if os.path.isdir(self.__AbsolutePath(path)):
            try:
                # Delete the folder 
                dl.Delete.Directory(path)
                # Log delete operation
                logger.Message.Directory(self.config.Logging, path)
            except OSError as error:
                # Log any errors
                logger.Message.Error(self.config.Logging, error)

    def __AbsolutePath(self, item):
        '''Retrieve the absolute path to an item
        
        Args:
            item (string): Name of the directory item
        '''
        
        return os.path.join(self.directory,item)

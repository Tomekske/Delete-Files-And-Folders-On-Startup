import os
import logging
import src.logging.Message as logger

class Guard:
    '''Guard class containing static methods to easily check whether objects are valid'''

    @staticmethod
    def IsNotEmpty(filename, error, item):
        '''Check whether a object is not empty
        
        Args:
            filename (string): The name of the logfile
            error (string): The error message
            item (object): To be tested object
        '''

        # Check whether object is empty
        if not item:
            exception = f'Item {error} is empty'
            logger.Message.Error(filename, exception)
            raise Exception(exception)
        return True
    
    @staticmethod
    def PathExist(path, filename=None):
        '''Check whether a path exists
        
        Args:
            filename (string): The name of the logfile
            path (string): Path to the item
        '''

        # Check whether the path the file or directory exists
        if not os.path.exists(path):
            exception = f"Path - '{path}' does not exist"

            # Check whether logfile name is not none
            if filename is not None:
                logger.Message.Error(filename, exception)
            raise(exception)
        return True

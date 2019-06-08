import logging

class Message:
    '''Class containing static methods to easily log information to the config file'''

    @staticmethod
    def File(filename, path):
        '''Static method to log about file items
        
        Args:
            filename (string): The name of the logfile
            path (string): Path to the item
        '''

        Message.__BasicConfiguration(filename)
        logging.info(f'[FILE] - [{path}]')
    
    @staticmethod
    def Directory(filename, path):
        '''Static method to log about file items
        
        Args:
            filename (string): The name of the logfile
            path (string): Path to the item
        '''

        Message.__BasicConfiguration(filename)
        logging.info(f'[DIR]  - [{path}]')

    @staticmethod
    def Error(filename, error):
        '''Static method to log errors
        
        Args:
            filename (string): The name of the logfile
            error (string): Error description
        '''

        Message.__BasicConfiguration(filename)
        logging.error(f'[{error}]')

    @classmethod
    def __BasicConfiguration(cls, filename):
        '''Wrapper method around the basicConfig function
        
        Args:
            filename (string): The name of the logfile
        '''

        logging.basicConfig(level = logging.INFO,filename = filename,  filemode = 'a', format = '[%(asctime)s] - [%(levelname)s] - %(message)s', datefmt = '%d-%m-%y %H:%M:%S')

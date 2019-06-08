import os
import shutil

class Delete:
    '''Class containing static methods to easily delete folders or files within a directory'''

    @staticmethod
    def File(path):
        '''Static method for deleting a file within a directory
        
        Args:
            path (string): Path to the file
        '''
        
        os.unlink(path)
    
    @staticmethod
    def Directory(path):
        '''Static method for deleting a folder within a directory
        
        Args:
            path (string): Path to the folder
        '''

        shutil.rmtree(path)
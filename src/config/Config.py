from dataclasses import dataclass

@dataclass
class Config:
    '''POCO class for config data'''

    Directories: str = ""
    Whitelist: str = ""
    Folders: bool = False
    Logging: str = ""

# Project Title

Delete files and folder items on startup

## Description

This is a script where unnecessary files and folders are getting deleted within certain folders, all deleted items are saved in a log file.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Make sure python version >= 3.7.0 is installed

### Installing

Installing project

```
git clone https://github.com/Tomekske/Delete-Files-And-Folders-On-Startup
```

### Configuration file
Replace the following placeholder values within the template.json file and change the filename to config.json

```
{
    "Directories": [
        "<C:\\path\\to\\directory_1>",
        "<C:\\path\\to\\directory_2>"
    ],
    "Whitelist": [
        ".<extension_1>",
        ".<extension_2>",
        ".<extension_3>",
        ".<extension_4>"
    ],
    "Folders" : true,
    "Logging" : "<C:/path/to/logfile.log>"
}
```

#### Directories
An array of desired path directories where items are getting deleted

#### Whitelist
An array of desired file extensions which are getting deleted

#### Folders
Boolean to determine whether folders within a directory should be deleted

#### Logging
Path to the save location of the log file where deleted items and error messages are registered




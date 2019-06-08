import pathlib
import json
import src.config.Config as cfg
import src.directory.Directory as drs

with open('config.json') as f:
    # Load data from file
    data = json.load(f)

    # Prepare config object
    config = cfg.Config(data['Directories'], data['Whitelist'], data['Folders'], data["Logging"])

# loop over every specified directory in the config file
for d in config.Directories:
    # Create a dictionary object
    directory = drs.Directory(d, config)
    # Delete an item in the specified directory
    directory.DeleteItems()

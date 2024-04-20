"""Water Logger

This script centralizes the configuration of the logger for the project. 

The setup of the logger is automatic on import. 

This file following function:
    * getLogger - returns a instance of logger
"""


import pathlib
import os
import logging
import logging.config
import logging.handlers

import env
from env import ROOT_DIR


DEFAULT_CONFIG_PATH = 'config/logging.conf'


def setup():
    config_file_path = os.path.join(ROOT_DIR, DEFAULT_CONFIG_PATH)
    
    try:
        logging.config.fileConfig(config_file_path, disable_existing_loggers=False)
    except(TypeError) as err:
        print("Log path most likely not configured. Update your 'config/logging.conf'")
        raise err

def getLogger(name='root'):
    """Returns an instance of logger

    Parameters
    ----------
    name : str
        Name of the logger

    Returns
    -------
    Logger
        a Logger instance
    """
    return logging.getLogger(name)

setup()

'''
Utilities to log messages
'''
__author__ = "Danilo Piparo"
__copyright__ = "CERN"
__license__ = "LGPL2"
__email__ = "danilo.piparo@cern.ch"

import logging

def getLogger(name):
    logging.basicConfig(format='%(asctime)s - ' + name + ' - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    return logger
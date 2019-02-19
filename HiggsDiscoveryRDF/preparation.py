'''
Fetch input files and compile root macro to run
simplified higgs discrovery analysis modelled around the 
ROOT tutorial rf103.
'''
__author__ = "Danilo Piparo"
__copyright__ = "CERN"
__license__ = "LGPL2"
__email__ = "danilo.piparo@cern.ch"

import ROOT
import os
import hashlib
import shutil
from multiprocessing import Pool

from utils.log import getLogger
logger = getLogger("HiggsDiscoveryRDF")

filesPath = "root://eospublic.cern.ch//eos/root-eos/cms_opendata_2012_nanoaod/"
filesNamesHashList = [("Run2012B_DoubleElectron.root", "0e1fa70419a61fbf9ecd3bf2e660c7230685053e"),
                      ("Run2012B_DoubleMuParked.root", "212cea19c990c7709214c48d5e39b49f109ecd50"),
                      ("Run2012C_DoubleElectron.root", "ed0ca1ecc5e7113dc19fa44100ee0f130603c5a7"),
                      ("Run2012C_DoubleMuParked.root", "01f0c9ed14f3fb84ba91d2071e61b3492ada1c03"),
                      ("SMHiggsToZZTo4L.root", "0b93a74e90c674a28b6128c7eb5b8792843c45b8"),
                      ("ZZTo2e2mu.root", "ed25c624e55b070fcf229b01a0a762185d17c0a4"),
                      ("ZZTo4e.root", "94e995079a107c04a917c591fee753cb80d1f4e4"),
                      ("ZZTo4mu.root", "556fde4d36f17288e395d23660ab78494623ab46")]

macroName = "higgsDiscovery.C"

def sha1sum(fileName):
    '''Create a hash of a file starting from its name'''
    if not os.path.exists(fileName): 
        return None
    h  = hashlib.sha1()
    b  = bytearray(16*1024*1024)
    mv = memoryview(b)
    with open(fileName, 'rb', buffering=0) as f:
        for n in iter(lambda : f.readinto(mv), 0):
            h.update(mv[:n])
    return h.hexdigest()

def checkHash(fileNameHash):
    fileName, fileHash = fileNameHash
    retVal = None if fileHash == sha1sum(fileName) else fileName
    if not retVal:
        logger.debug("File %s was found on disk with the correct hash. It will not be downloaded." % fileName)
    return retVal

def getFiles():
    logger.debug("Getting input files from EOS")
    # We use MP to optimise the time needed to hash
    pool = Pool(4)
    fileNames = filter(lambda name: name, pool.map(checkHash, filesNamesHashList))
    
    for fileName in fileNames:
        fullFileName = filesPath + fileName
        logger.debug("Copying %s to local disk..." %fullFileName)
        ROOT.TFile.Cp(fullFileName, "./%s" %fileName)
    del pool # I see the processes alive after this call...

def compileMacro():
    if os.path.exists(macroName.replace(".C","_C.so")):
        logger.debug("ROOT Macro already compiled")
        return
    logger.debug("Compiling ROOT Macro")
    thisPath = os.path.dirname(__file__)
    shutil.copyfile(os.path.join(thisPath,macroName), macroName)
    os.system('root -b -q -l -e ".L %s+"' %macroName)

def run():
    getFiles()
    compileMacro()

if __name__ == "__main__":
    run()
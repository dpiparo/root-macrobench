'''
Run all the benchmarks
'''
__author__ = "Danilo Piparo"
__copyright__ = "CERN"
__license__ = "LGPL2"
__email__ = "danilo.piparo@cern.ch"

benchmarkNameList = ["HiggsDiscoveryRDF"]

import importlib
import os

def mkdirIfNotThere(name):
    if not os.path.exists(name):
        os.mkdir(bmodWorkDir)

def getWorkDirName(name):
    return "%s_workdir" %name

def run():
    curDir = os.getcwd()
    for benchmarkName in benchmarkNameList:
        prep = importlib.import_module("%s.preparation" %benchmarkName)
        bench = importlib.import_module("%s.benchmark" %benchmarkName)
        bmodWorkDir = getWorkDirName(benchmarkName)
        mkdirIfNotThere(bmodWorkDir)
        os.chdir(bmodWorkDir)
        prep.run()
        bench.run()
        os.chdir(curDir)

if __name__ == "__main__":
    run()
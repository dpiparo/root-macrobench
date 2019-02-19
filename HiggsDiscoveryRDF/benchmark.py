'''
Fetch input files and compile root macro to run
simplified higgs discrovery analysis modelled around the 
ROOT tutorial rf103.
'''
__author__ = "Danilo Piparo"
__copyright__ = "CERN"
__license__ = "LGPL2"
__email__ = "danilo.piparo@cern.ch"

from utils.benchmarking import runBenchmark
import os

def launchMacro():
    os.system("root -b -q -l higgsDiscovery.C+")

def run():
    runBenchmark("HiggsDiscoveryRDF", launchMacro)

if __name__ == "__main__":
    run()

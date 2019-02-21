# root-macrobench
A repository for long running ROOT benchmark workflows

## The idea
Run workflows which last a significant amount of time (tens of seconds, minutes) and measure the runtime.
This allows to check for performance regressions.

## How to write a benchmark
The package is written for Python3.
Benchmarks are expressed in directories which are python packages.
These packages need to provide two submodules, `preparation` and `benchmark`, each providing a method: `run`.

A useful tool to run a benchmark, print to screen the runtime and save a file with the result of the benchmark in the 
work directory is the `utils.Benchmarking.runBenchmark` function. In order to get a logger for your messages, use the function
`utils.log.getLogger`.

Don't forget to add the benchmark name (aka the directory name) to the list of directories in the `run.py` driver script.

## How does it work?
The driver creates a workdir for each benchmark. It prepares the benchmark and runs it.

## Benchmarks
1. HiggsDiscoveryRDF
2. YOUR NICE CONTRIBUTION!

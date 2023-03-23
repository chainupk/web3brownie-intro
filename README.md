# Brownie Framework and Pytest

## Install Brownie

`pip install eth-brownie`

## Create a Brownie Project

To start a brownie project create a directory using command:`mkdir` and then change directory to the newly created directory  using command:`cd`. Then in the directory run command:`brownie init`.

Each Brownie project uses the following structure:

- contracts/: Contract sources
- interfaces/: Interface sources
- scripts/: Scripts for deployment and interaction
- tests/: Scripts for testing the project
- build/: where the compiled ABI's are located

When you init a brownie project these folders are empty.

After creating a contract in the `contracts` folder, you may run the command: `brownie compile` from anywhere in the directory. This will build the ABI required in the `build` folder.

## The Brownie framework makes use of pytest for testing.

Pytest performs a test discovery process to locate functions that should be included in your project's test suite. Tests must be stored within the `tests/` directory of your project, or a subdirectory thereof.

Filenames must match `test_*.py` or `*_test.py`. Within the test files, the following methods will be run as tests:

- Functions outside of a class prefixed with `test`.
- Class methods prefixed with `test`, where the class is prefixed with `Test` and does not include an `__init__` method.

You may run the tests cases by running:
`brownie test` or `brownie test tests` or `brownie test tests/test_xxx.py`

By default, pytest only prints functions that FAILS on assertion

If you'd like to print a all logs you could pass in a "-s" parameter, provided by pytest:
E.g. `brownie test tests/test_xxx.py -s`

There are other brownie specific such as `--gas` and `--coverage`

Review:
Overall this is a very simple framework. However comparing to the Foundry project you will not be able to see any printed `"console.log("xxx")"` statements within your contract codes when running the tests. Which might be helpful during a nested call between contracts.
import pytest


@pytest.fixture(autouse=True)
def setup(fn_isolation):
    """
    Isolation setup fixture.
    This ensures that each test runs against the same base environment.
    """
    print("conftest setup")
    pass


# @pytest.fixture(scope="module")
# def vyper_storage(accounts, VyperStorage):
#     """
#     Yield a `Contract` object for the VyperStorage contract.
#     """
#     print("conftest vyper_storage")
#     yield accounts[0].deploy(VyperStorage)


@pytest.fixture(scope="module")
def solidity_storage(accounts, SolidityStorage):
    """
    Yield a `Contract` object for the SolidityStorage contract.
    """
    print("conftest solidity_storage")
    yield accounts[0].deploy(SolidityStorage)

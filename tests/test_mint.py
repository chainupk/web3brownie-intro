import pytest

from brownie import Storage, accounts

def test_mint():
    print("test run test_mint function")
    acc = accounts[0]
    deployed_contract = Storage.deploy({'from': acc})
    balance = deployed_contract.retrieve()
    print("balance1 :", balance)
    deployed_contract.store(1, {'from': acc})
    balance2 = deployed_contract.retrieve()
    print("balance2 :", balance2)
    pass

def test_sure_pass():
    print("sure pass")
    pass

def test_account_balance():
    balance = accounts[0].balance()
    print("balance1 : ", balance)
    accounts[0].transfer(accounts[1], "10 ether", gas_price=0)
    print("balance 2: ", accounts[0].balance())
    assert balance - "10 ether" == accounts[0].balance()

def test_sure_pass():
    print("this should fail!")
    assert False
from brownie import FundMe,MockV3Aggregator, accounts,network,config,exceptions
from scripts.helpfulScripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account,deploy_mocks
from web3 import Web3
from scripts.deploy import deploy_fund_me
import pytest


def test_can_fund_withdraw():
    account = get_account()
    fundme = deploy_fund_me()
    entrance_fee = fundme.getEntranceFee()
    tx1 = fundme.fund({"from":account,"value":entrance_fee})
    tx1.wait(1)
    assert fundme.addressToAmountFunded(account.address)==entrance_fee
    tx2 = fundme.withdraw({"from":account})
    tx2.wait(1)
    assert fundme.addressToAmountFunded(account.address) == 0

def test_only_owner():
    fund_me = deploy_fund_me()
    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from":bad_actor})

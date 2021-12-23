from brownie import FundMe,MockV3Aggregator, accounts,network,config
from scripts.helpfulScripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account,deploy_mocks
from web3 import Web3



def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    fund_me.fund({"from":account,"value":entrance_fee})

def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from":account})


def main():
    fund()
    withdraw()
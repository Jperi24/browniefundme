from brownie import accounts,config,network, MockV3Aggregator
from web3 import Web3
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development","ganache-local"]

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    print(f"Active network is {network.show_active()}")
    if len(MockV3Aggregator)<=0:
        MockV3Aggregator.deploy(8,Web3.toWei(200000000,"ether"),{"from":get_account()})
 

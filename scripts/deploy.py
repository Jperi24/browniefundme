from brownie import FundMe,MockV3Aggregator, accounts,network,config
from scripts.helpfulScripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account,deploy_mocks
from web3 import Web3

def deploy_fund_me():

  

    account = get_account()

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fundme = FundMe.deploy(price_feed_address,
    {"from":account},publish_source = config["networks"][network.show_active()]["verify"])
    print({fundme.address})
    return fundme




def main():
    deploy_fund_me()

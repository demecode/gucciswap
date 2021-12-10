
from web3 import Web3
from scripts.helpers import get_account
from brownie import GucciToken


initial_supply = Web3.toWei(1000000, "ether")

def deploy_token():
    account = get_account()
    print(account)
    gucci_tkn = GucciToken.deploy(initial_supply, {"from": account})
    print(gucci_tkn.name())

def main():
    deploy_token()
    

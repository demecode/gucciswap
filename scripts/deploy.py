
from web3 import Web3


initial_supply = Web3.toWei(1000000, "ether")

def deploy_token():
    account = get_account()
    print(account)
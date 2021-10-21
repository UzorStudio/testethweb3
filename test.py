from web3 import Web3
import web3Func

w = web3Func.Work('https://ropsten.infura.io/v3/537c4c65f5bd41a9bfb65d33948ece9d')




#print(w.getLastBlockInfo("latest"))

print(len(w.getLast10BlockInfo()))
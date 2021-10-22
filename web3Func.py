import web3
from web3 import Web3
import json

class Work():
    def __init__(self,apiId):
        self.apiId = apiId
        self.w3 = Web3(Web3.HTTPProvider(self.apiId))

    def getLast10BlockInfo(self):

        bloks = []

        i = 0
        while i != 10:
            bloks.append(Web3.toJSON(self.w3.eth.getBlock(self.w3.eth.blockNumber - i)))
            i+=1

        return bloks

    def getLastBlockInfo(self,blockId):
        bl = self.w3.eth.get_block(blockId)
        bltrans = []
        for i in bl["transactions"]:
            bltrans.append(i.hex())

        ret = {"timestamp":bl["timestamp"],
               "transactions count":len(bl["transactions"]),
               "transactions":bltrans
               }

        return ret
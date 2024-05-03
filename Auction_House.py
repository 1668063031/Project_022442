from DataPack import Principal


class Auction_House:
    def __init__(self,name):
        self.pri = Principal(name)

    def register(self,customer):
        
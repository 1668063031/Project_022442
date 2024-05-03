from Auction_House import Auction_House
from Customer import Customer
from DataAgent import DataAgent
from Label import Label

if __name__ == '__main__':
    bob = Customer("bob")
    da = DataAgent("da")
    ah = Auction_House("Auction")
    bh = Auction_House("Auction1")


    def test(lab):
        print(f">>Test<< Owner: {lab.owner}, Readers: {lab.readers}")


    label = Label(bob, ah)
    test(label)
    bob.register(ah, label)
    # ah.register(bob, label)
    # test(label)
    ah.switch_user_status(bob, label)
    test(label)
    bob.requestRef(ah, label)
    test(label)
    print("--")
    bob.register(bh, label)
    test(label)
    bob.commitRef(bh,label)

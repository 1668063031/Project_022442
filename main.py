from Auction_House import Auction_House
from Customer import Customer
from DataAgent import DataAgent
from Label import Label

if __name__ == '__main__':
    bob = Customer("bob")

    ah = Auction_House("Auction")
    bh = Auction_House("Auction1")


    def test(lab):
        print(f">>Test<< Owner: {lab.owner}, Readers: {lab.readers}")


    label = Label(bob, readers=[bob, ah])
    print("---")
    test(label)
    bob.register(ah, label)
    # ah.register(bob, label)
    # test(label)
    print("---")
    ah.switch_user_status(bob, label)
    print("---")
    bob.register(bh, label)
    test(label)
    print("---")
    bob.requestRef(ah, label)
    test(label)
    print("---")
    bob.commitRef(bh, label)
    test(label)

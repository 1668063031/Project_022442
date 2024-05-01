class Label:
    def __init__(self, owners_readers):
        self.owners_readers = owners_readers

    def effective_readers(self):
        all_readers = list(self.owners_readers.values())
        if not all_readers:
            return set()
        effective = set(all_readers[0])
        for readers in all_readers[1:]:
            effective.intersection_update(readers)
        return effective

    def can_read(self, user):
        if self.effective_readers() is not None:
            if user in self.effective_readers():
                print(f">>Label<< {user} is the effective reader")
                return user in self.effective_readers()
            else:
                print(f">>Label<< {user} is not the effective reader for Owner {list(self.owners_readers.keys())} "
                      f"as junction are: {self.effective_readers()}")

    def add_reader(self, owner, readers):
        if owner in self.owners_readers:
            self.owners_readers[owner].add(readers)
            print(f">>Label<< Added {readers} to {owner}'s allowed readers. Full list:{self.owners_readers}")
        else:
            print(f">>Label<< {owner} not found.")

    def remove_readers_beside(self, owner, reader):
        current_readers = self.owners_readers[owner]
        self.owners_readers[owner] = {reader} if reader in current_readers else set()
        print(f">>Label<< All other Readers removed for owner {owner} beside {reader}. The Label now: {self.owners_readers}")

    def remove_reader(self, owner, reader):
        if owner in self.owners_readers and reader in self.owners_readers[owner]:
            self.owners_readers[owner].remove(reader)
            print(f">>Label<< Removed {reader} from {owner}'s allowed readers.The Label now: {self.owners_readers}")

        else:
            print(f">>Label<< {reader} is not an allowed reader of {owner} or {owner} not found.")

    def add_owner(self, owner, readers=None):
        if readers is None:
            readers = set()
        self.owners_readers[owner] = set()
        self.owners_readers[owner].add(readers)
        print(f">>Label<< Added {owner} as a new owner with initial readers set.")

    def remove_owner(self, owner):
        if owner in self.owners_readers:
            del self.owners_readers[owner]
            print(f">>Label<< Removed {owner} and their readers list.")
        else:
            print(f">>Label<< {owner} not found.")


class Customer:
    def __init__(self, maxBid, identity_Level, cus_id, relationship):
        self.id = cus_id
        self.identity_Level = identity_Level
        self.maxBid = maxBid
        self.security_label = Label(relationship)

    def reputation(self, user):
        if self.security_label.can_read(user.id):
            print(f">>Customer<< reputation promoted for {user.id}, level {self.identity_Level}")
            return self.identity_Level
        print(">>Customer<< reputation not promoted")
        return "0"

    def promote_rep(self, user, new_identity_Level, ref=None):
        if ref is None:
            if self.security_label.can_read(user.id):
                self.identity_Level = new_identity_Level
                return print(
                    f">>Customer<< Reputation updated to {new_identity_Level} based on trusted reference")  # from {self.r.owner} -> {self.r.receiver} : {self.r.id}.")
            return print(">>Customer<< Update Denied: Unauthorized access.")


class Auction:
    def __init__(self, name, relationship, trusted=None):
        self.name = name
        self.customers = {}
        self.trusted = trusted if trusted else []
        self.security_label = Label(relationship)

    def register(self, cus):
        self.customers[cus.id] = cus
        self.security_label.add_reader(self.name, cus.id)
        # print(">>Logic<< Data Declassification")
        # Declassify?
        print(f">>Auction<< Customer {cus.id} registered in {self.name}.")

    def ref(self, cus_id, ref_auc, ref_cus):
        if ref_auc.name in self.trusted:
            customer = ref_auc.customers.get(cus_id)
            if customer:
                rep = customer.reputation(ref_cus)
                if rep != "0":
                    self.customers[cus_id].promote_rep(ref_cus, rep)
                    self.security_label.add_reader(self.name,"temp")
                    print(">>Logic<< Data Declassification")
                    self.security_label.remove_reader(self.name,"temp")
                    print(">>Logic<< Data Relabeling")
                    # Remove label`s reader for security (3.4 rule 1) data flow auc1 ->(cus)-> auc2
                    print(
                        f">>Auction<< {cus_id}'s reputation updated to {rep} in {self.name} based on reference from {ref_auc.name}.")
                else:
                    print(">>Auction<< Reference access denied.")
            else:
                print(f">>Auction<< Customer {cus_id} not found in {ref_auc.name}.")
        else:
            print(f">>Auction<< {ref_auc.name} is not a trusted auction house by {self.name}.")


if __name__ == '__main__':
    label = {
        "a1": {"c2"},
        "a2": {"c3"},
        "a3": {"c122"}
    }
    aus_a = Auction("a1", label)
    aus_b = Auction("a2", label, trusted="a1")
    aus_c = Auction("a3", label)
    cus_1 = Customer("1000", "high", "c1", label)
    aus_a.register(cus_1)

    cus_2 = Customer("500", "low", "c1", label)
    aus_c.register(cus_2)
    aus_b.register(cus_2)
    aus_b.ref(cus_2.id, aus_a, cus_2)

    print(cus_2.identity_Level)

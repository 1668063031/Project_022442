class Label:
    def __init__(self, owner, readers):
        self.owner = owner
        self.readers = set(readers)

    def can_read(self, principal):
        return principal == self.owner or principal in self.readers

    def add_reader(self, owner, readers):
        if owner == self.owner:
            if readers not in self.readers: self.readers.add(readers)
            print(f">>Logic<< Declassified from owner {owner}")
            return True
        else:
            raise Exception("Only the Owners can add new readers")

    def remove_reader(self, owner, removed):
        if owner == self.owner:
            self.readers.discard(removed)
        else:
            raise Exception("Only the owners can remove reader")

    def intersect_readers(self, other_label):
        print(f">>logic<< {self} U {other_label}, result {self.readers.intersection(other_label.readers)}")
        return self.readers.intersection(other_label.readers)

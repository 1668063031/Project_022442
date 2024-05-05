from DataPack import DataPack, Principal, Reference
from Label import Label


class Customer:
    def __init__(self, name):
        self.principal = Principal(name)
        self.ref = Reference()

    def share_data(self, reader, share, label):
        if label.can_read(share):
            label.add_reader(label.owner, share)
        else:
            raise Exception(f"Principal {reader.name} can not read label: {label}")

    def register(self, auc, label):
        re = Label(self, readers=[self, auc])
        if (label.owner and label.readers) != (re.owner and re.readers):
            label.relabelling(label, self, self)
            print(f">>Logic<< Reset label, o {label.owner}, r {label.readers}")
        else:
            print(f">>CUS<< Label does not require refresh")
        name = auc.principal.name
        label.add_reader(label.owner, auc.principal.name)
        if label.can_read(name):
            auc.register(self, label)
        else:
            # print(label.owner,label.readers)
            raise Exception(f"Principal {name} can not read label: o {label.owner}, r {label.readers}")

    def requestRef(self, auc, label):
        re = Label(self, readers=[self, auc])
        if (label.owner and label.readers) != (re.owner and re.readers):
            label.relabelling(label, self, self)
            print(f">>Logic<< Reset label, o {label.owner}, r {label.readers}")

        name = auc.principal.name
        label.add_reader(label.owner, name)

        if label.can_read(name):
            self.ref = auc.make_reference(self, label)
            return self.ref
        else:
            raise Exception(f"Principal {name} can not read label: o {label.owner}, r {label.readers}")

    def commitRef(self, auc, label):
        re = Label(self, readers=[self, auc])
        if (label.owner and label.readers) != (re.owner and re.readers):
            label.relabelling(label, self, self)
            print(f">>Logic<< Reset label, o {label.owner}, r {label.readers}")
        name = auc.principal.name
        label.add_reader(label.owner, auc.principal.name)
        if label.can_read(name):

            b = auc.check_reference(self, label, self.ref)
            return b
        else:
            raise Exception(f"Principal {name} can not read label: {label}")

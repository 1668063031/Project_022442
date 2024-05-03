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
        label.relabelling(label, self, auc)
        print(f">>Logic<< Reset label, o {label.owner}, r {label.readers}")

        name = auc.principal.name
        if label.can_read(name):
            label.add_reader(label.owner, self.principal.name)
            auc.register(self, label)
        else:
            raise Exception(f"Principal {name} can not read label: {label}")

    def requestRef(self, auc, label):

        label.relabelling(label, self, auc)
        print(f">>Logic<< Reset label, o {label.owner}, r {label.readers}")

        name = auc.principal.name
        if label.can_read(name):
            label.add_reader(label.owner, self.principal.name)
            self.ref = auc.make_reference(self, label)
            return self.ref
        else:
            raise Exception(f"Principal {name} can not read label: {label}")

    def commitRef(self, auc, label):
        label.relabelling(label, self, auc)
        print(f">>Logic<< Reset label, o {label.owner}, r {label.readers}")
        name = auc.principal.name
        if label.can_read(name):
            label.add_reader(label.owner, self.principal.name)
            b = auc.check_reference(self, label, self.ref)
            return b
        else:
            raise Exception(f"Principal {name} can not read label: {label}")

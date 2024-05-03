from DataPack import DataPack, Principal
from Label import Label


class Customer:
    def __init__(self, name):
        self.principal = Principal(name)
        self.infos = {}

    def init_register(self, name, label, ref=None):
        if label.can_read(self.principal):
            if ref == None:
                if name not in self.infos:
                    label.readers.add(label.owner)
                    info = []
                    self.infos[name] = DataPack(info, label)
                else: raise Exception("Customer Already Existed")
            else:
                if name not in self.infos:
                    label.readers.add(label.owner)
                    info = [ref]
                    self.infos[name] = DataPack(info, label)
                else:
                    raise Exception("Customer Already Existed")

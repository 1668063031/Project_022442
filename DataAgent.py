from DataPack import Principal, DataPack


class DataAgent:
    def __init__(self, name):
        self.principal = Principal(name)
        self.db = {}
        self.trusted = {"Auction", "Auction2", "Auction1"}

    def checkTrusted(self, name, label):
        if name in self.trusted:
            if label.can_read(self.principal.name):
                label.readers.add(label.owner)
                return True
            raise Exception(f"Principal {self.__class__} can not read label: {label.owner,label.readers,self.principal.name}")
        return False

    def add_Data(self, opt, name, label):
        if label.can_read(self.principal.name):
            #label.add_reader(label.owner, label.owner)
            self.db[name] = DataPack(False, label)
        else:
            raise Exception(f"Principal {self.__class__} can not read label: {label}")

    def change_status(self, opt, name, label):
        if label.can_read(self.principal.name):
            self.db[name] = DataPack(not self.db[name].content, label)
            return self.db[name].content
        else:
            raise Exception(f"Principal {self.__class__} can not read label: {label}")

    def read_Data(self, name, reader):
        record = self.db.get(name)
        if record and record.label.can_read(reader):
            return record.content
        else:
            raise Exception(f"Principal {reader.name} can not read label: {record.label}")

    def share_data(self, name, reader, share):
        record = self.db.get(name)
        if record and record.label.can_read(share):
            record.label.add_reader(record.label.owner, share)
        else:
            raise Exception(f"Principal {reader.name} can not read label: {record.label}")

    def remove_data_access(self, name, reader, remove):
        record = self.db.get(name)
        if record and record.label.can_read(remove):
            record.label.remove_reader(record.label.owner, remove)
        else:
            raise Exception(f"Principal {reader.name} can not read label: {record.label}")

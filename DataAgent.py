from DataPack import Principal, DataPack


class DataAgent:
    def __init__(self, name):
        self.p = Principal(name)
        self.db = {}

    def add_Data(self, name, label):
        if label.can_read(self.p):
            label.readers.add(label.owner)
            self.db[name] = DataPack(True,label)
        else:
            raise Exception(f"Principal {self.__class__} can not read label: {label}")

    def change_status(self,name,label):
        if label.can_read(self.p):
            label.readers.add(label.owner)
            self.db[name] = DataPack(not self.db[name].content,label)
        else:
            raise Exception(f"Principal {self.__class__} can not read label: {label}")

    def read_Data(self,name,reader):
        record = self.db.get(name)
        if record and record.label.can_read(reader):
            return record.content
        else: raise Exception(f"Principal {reader.name} can not read label: {record.label}")
            #record.label.add_reader(record.label.owner,reader)

    def share_data(self,name,reader,share):
        record = self.db.get(name)
        if record and record.label.can_read(share):
            record.label.add_reader(record.label.owner,share)
        else: raise Exception(f"Principal {reader.name} can not read label: {record.label}")

    def remove_data_access(self,name,reader,remove):
        record = self.db.get(name)
        if record and record.label.can_read(remove):
            record.label.remove_reader(record.label.owner,remove)
        else: raise Exception(f"Principal {reader.name} can not read label: {record.label}")

class DataPack:
    def __init__(self, content, label):
        self.content = content
        self.label = label


class Principal:
    def __init__(self, name):
        self.name = name


class Reference:
    def __init__(self, org=None, name=None, level=None):
        self.org = org
        self.name = name
        self.level = level

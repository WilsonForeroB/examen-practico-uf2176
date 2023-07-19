class solicitudes:
    def __init__(self):
        self.data = []

    def add(self, item):
        usuario_para_añadir = {item[0]: [item[1], item[2], item[3], item[4]]}
        self.data.append(usuario_para_añadir)

    def add_all(self, items):
        self.data.extend(items)

    def get(self, id):
        return self.data[id]

    def get_all(self):
        return self.data

    def update(self, id, item):
        self.data[id] = item

    def delete(self, id):
        del self.data[id]

    def print_dict(self, dict):
        for key, value in dict.items():
            print(key, value)

    def print_array(self, array):
        for item in array:
            print(item)

    def print_data(self, data):
        if isinstance(data, dict):
            self.print_dict(data)
        elif isinstance(data, list):
            self.print_array(data)
        else:
            print(data)

class Model:
    def query(self, **kwargs):
        self.data = kwargs

    def __str__(self):
        if 'data' in self.__dict__:
            return 'Model: ' + ', '.join([f"{key} = {value}" for key, value in self.data.items()])
        return 'Model'


model = Model()
model.query(id=1, fio='Sergey', old=33)
print(model)
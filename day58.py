class Model:
    @classmethod
    def create(cls, name):
        return cls(name)


class GPTModel(Model):
    def __init__(self, name):
        self.name = name


model = GPTModel.create("GPT-5")

print(type(model).__name__)
print(model.name)
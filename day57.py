class Model:
    total_models=0
    def __init__(self,name):
        self.name=name
        Model.total_models=+1

    @classmethod
    def get_total_model(cls):
        return cls.total_models

print(Model.get_total_model())

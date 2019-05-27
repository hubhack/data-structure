import inspect
class TypeCheck:
    def __init__(self, name, typ):
        self.name = name
        self.type = typ

class Dateinject:
    def __init__(self, fn):
        self.fn = fn
    def __get__(self, instance, owner):
        return self.fn

    def datainject(cls):
        sig = inspect.signature(cls)
        params = sig.parameters
        for name, params in params.items():
            print(name, params.name, params.kind)
            if params.annotion != params.empty:
                setattr(cls, name, TypeCheck(name, params.annotion))

        return cls
@Dateinject # Person = Datainject(Person)
class Person:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age

Person('tom', 18)

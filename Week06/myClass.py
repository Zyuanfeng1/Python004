class Zoo(object):
    def __init__(self,name):
        self.name=name
    def add_animal(self, ani):
        ani_name = type(ani).__name__
        if not hasattr(self, ani_name):
            setattr(self, ani_name, [])
            getattr(self, ani_name).append(ani)
class Animal(object):
    tixing = 0
    Fierce = False
    def __init__(self, kind, size, character):
        self.kind = kind
        self.size = size
        self.character = character
        if (self.size == '小'):
            self.tixing = 1
        if (self.size == '中'):
            self.tixing = 2
        if (self.size == '大'):
            self.tixing = 3
        if (self.tixing >= 2 and self.kind == '食肉' and self.character == '凶猛'):
            self.Fierce = True
class Cat(Animal):
    isPetable=False
    sound='miaomiao'
    def __init__(self,name,kind, size, character):
        super().__init__(kind,size,character)
        self.name = name
        self.isPetable=not self.Fierce

class Dog(Animal):
    isPetable=False
    sound='wangwang'
    def __init__(self,name,kind, size, character):
        super().__init__(kind,size,character)
        self.name = name
        self.isPetable=not self.Fierce

if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    print(z.__dict__)
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    cat2 = Cat('大花猫 2', '食肉', '大', '凶猛')
    print(cat1.name)
    print(cat1.__dict__)
    print(cat1.Fierce)
    print(cat2.name)
    print(cat2.__dict__)
    print(cat2.Fierce)
    # 增加一只猫到动物园
    z.add_animal(cat1)
    z.add_animal(cat2)
    print(z.__dict__)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
    print(have_cat)
    print(z.Cat)



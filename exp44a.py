# 隐式继承-子类的行为与父类的行为相同
class Parent(object):

# 如果将函数放在基类中，然后所有子类会自动获得这些特性，对于需要写很多重复代码的类来说非常方便
    def implict(self):
        print("PARENT implict()")

class Child(Parent):
    pass  # 告诉python我需要一个空块的方式，没有什么新的内容需要定义，继承父类的所有行为

dad = Parent()
son = Child()

dad.implict()
son.implict()

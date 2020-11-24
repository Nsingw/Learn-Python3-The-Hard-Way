class mystuff(object):

    def __init__(self):  # 用于初始化新创建的空对象，self是python为我创建的空对象，我可以在里面设置变量
        self.tangerine = "And now a thousand years between" # 给self.tangerine赋值，完成对象的初始化

thing = mystuff()  #把新打造的对象赋给thing变量使用
print(thing.tangerine)

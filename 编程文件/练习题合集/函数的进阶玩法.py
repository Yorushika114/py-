# 假设有函数
def text(name2, name1):
    print(f"你好，{name1}!")
    print(f"你好，{name2}!")


# 1.注意位置实参的顺序
# name1 = 'KiriTo'
# name2 = 'Chloe'
# text(name1, name2)  # 如果两者的顺序改变，则在函数中输出的顺序会变
# text(name2, name1)

# 2.关键字实参
# text(name1='KiriTo', name2='Chloe')  # 关键字实参是在主函数中定义，交换位置也不会有影响，因为已经指定了
# text(name2='Chloe', name1='KiriTo')

# 3.默认值
# def text1(name1, name2='柯罗伊'):
#     print(f"你好，{name1}!")
#     print(f"你好，{name2}!")
#
#
# name = input()
# name1 = 'Chloe'  # 如果不把这一段加入到函数text1中，那么name2自动使用在定义时就已经设置好的默认值
# text1(name)

# 4.返回值
# 1)返回一个简单值
# def add(num1, num2):
#     num3 = num1 + num2
#     return num3
#
#
# num3 = int(input())
# num4 = int(input())
# print(add(num3, num4))  # 有return返回时就返回相加的值，没有return返回时就为None

# 2)返回一个字典
# def dic1(name1, name2):
#     dic2 = {'fruit': name1, 'color': name2}
#     return dic2
#
# 
# name1 = input('请输入一种水果：')
# name2 = input('请输入该水果的颜色：')
# print(dic1(name1, name2))

# 5.传递列表
# def test(namelist):
#     for name in namelist:
#         temp = name.title()
#         print(f"Hello {temp}!")
#
#
# list1 = ['KiriTo', 'Chloe', 'Asuna']
# test(list1)

# 6.在函数中修改列表
# def test(namelist):
#     namelist2 = []
#     while namelist:
#         temp = namelist.pop()
#         print(f"修改了元素{temp}")
#         namelist2.append(temp)
#     return namelist2
#
#
# list1 = ['KiriTo', 'Chloe', 'Asuna']
# print(test(list1))

# 7.传递任意数量的实参
# def test1(*fruitname):  # "*"表示让py创建一个名为fruitname的空元组，"**"表示让py创建一个名为fruitname的空字典
#     print(fruitname)    # 可以接受多个值，也可以接受一个值
#
#
# name1 = 'apple'
# name2 = 'banana'
# name3 = 'orange'
# test1(name1, name2, name3)

# 8.将函数存储在模块中

# 1)导入整个模块（文字描述）
""" 
假设在文件test1.py中有函数output()，如果想在本文件中使用，则需要使用“import test1”的形式将
test1.py中的函数拿到当前文件中使用，在使用函数时要类似于“test1.output()”这种形式来调用
模块中包含的所有函数

注意：导入了这个模块之后，在当前文件使用函数时模块中的函数仍然起作用。也是就说如果没有相关的限制，
模块中的函数在当前文件启动后仍然可以运行
"""

# 2)导入特定的函数（文字描述）
"""
在上文中解释了导入模块的方式，其实导入特定函数的方式也很简单（假设我只想使用output()函数），
使用"from test1 import output"的形式即可

注意：导入了这个模块之后，在当前文件使用函数时模块中的函数仍然起作用。也是就说如果没有相关的限制，
模块中的函数在当前文件启动后仍然可以运行
"""

# 3)使用as给函数指定别（文字描述）
"""
如果你嫌output()这个函数的名字太长了，不方便输入，则可以用"output as p"的形式将output()
函数的名字改成了“p”，则在调用函数的时候就是以p()的形式使用output()函数（两者的区别就是改了
一个名字而已）
"""

# 4)使用as给模块指定别名（文字描述）
"""
原理与"3)"同理
"""

# 5)导入模块中所有的函数（文字描述）
"""
如果你认为“1)”中调用函数的形式太麻烦，那么就可以使用"*"运算符来导入模块中的所有函数，例如
"from test1 import *"，则可以直接使用test1中的所有函数，而不用使用“1)”中的形式进行调用
"""
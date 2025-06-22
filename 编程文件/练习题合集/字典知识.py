# 字典的创建

# 1.直接创建
dic = {'你好': '1', '我不好': '2'}
# print(dic)

# 2.使用内置函数dict()来创建字典

# 1) 使用列表以键对键的格式创建
dic1 = dict([('你好', '1'), ('我不好', '2')])
# print(dic1)

# 2) 通过关键字进行创建
dic2 = dict(你好='1', 我不好='2')
# print(dic2)

# 3) 与zip()函数结合创建

# zip()函数：将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的zip对象
# zip()函数的示例
list1 = ['a', 'b', 'c']
list2 = ['1', '2', '3']
list3 = zip(list1, list2)
# print(list(list3))

# 两者的结合
dic3 = dict(zip(list1, list2))
# print(dic3)

# 字典的基本操作

# 1.字典的访问
# print(dic1['你好'])  # 在开头那个字典中，“你好”相当于下标，“1”相当于下标对应的值

# 2.字典的添加
dic1['我非常不好'] = 10  # “我非常不好”是一个新的下标，”10“是新的值，这就相当于添加了一个键对
# print(dic1)

# 3.空字典的创建（非常简单）
dicty = {}  # 现在一个名为dicty的空字典就已经创建出来了

# 4.修改字典中的值
# print(f"原字典的内容为：{dic1}")
# dic1['你好'] = 100  # 在已有的下标中进行修改，新赋的值将会替代掉原来的值
# print(f"新字典的内容为：{dic1}")

# 5.删除字典中的元素

# 1)使用del命令进行删除
# print(f"原字典的内容为：{dic1}")
# del dic1['你好']  # 下标为“你好”的键及其对应的值就被删除了
# print(f"新字典的内容为：{dic1}")

# 2)使用clear()方法清除字典中所有的元素
# print(f"原字典的内容为：{dic1}")
# dic1.clear()
# print(f"新字典的内容为：{dic1}")

# # 3)使用pop方法删除指定的键对，并且返回键的值
# print(f"原字典的内容为：{dic1}")
# print(dic1.pop('你好'))  # 利用pop删除掉这个下标键后，返回了其相应的值
# print(dic1.pop('你好', 11))  # 无指定的值，返回默认值为11
# print(f"新字典的内容为：{dic1}")

# 6.使用get()来访问值
# 函数格式：get(指定键,指定的键不存在时要返回的值)
# 解释：键存在时返回键所对应的值，不存在是返回设定的值
# value1 = dic.get('你好', '这个值并不存在！')
# value2 = dic.get('你很好', '这个值并不存在！')
# print(value1)
# print(value2)

# 7.遍历字典

# 1)遍历所有的键对（使用item()函数，返回键对）
# for i, j in dic.items():
#     print(f"\nKey: {i}\nValue: {j}")

# 2)遍历字典中所有的键（使用key()函数，只返回键）
# 备注：使用这个方法能够很快地收集到字典中的人名
# for name in dic.keys():   #这行代码的等效代码为：for name in dic:
#     print(f"{name}")

# 3)遍历字典中所有的值（使用values()函数，只返回值）
# for value in dic.values():
#     print(f"{value}")
# 如果需要计算有多少种类的值，则可以使用set()函数来合并相同的值，例如：
# dict4 = {
#     'name1': '1',
#     'name2': '2',
#     'name3': '1'
# }
# for value in set(dict4.values()):  #集合中的元素是独一无二的
#     print(f"{value}")

# 8.嵌套

# 1)在列表中存储字典数据
# a = {'color': 'blue', 'size': 10}
# b = {'color': 'red', 'size': 30}
# c = {'color': 'yellow', 'size': 20}
# All = [a, b, c]
# for i in All:  # 还可以利用切片的形式来决定要循环多少的数据
#     if i['color'] == 'blue':  # 还能用if语句来更改单一的数据
#         i['size'] = 7
#     print(i)

# 2)在字典中存储列表（适合一个键关联多个值）
# Apple = {
#     'color': 'red',
#     'taste': ['great', 'delicious']
# }
# print(f"apple的颜色是{Apple['color']},味道很:")
# for num in Apple['taste']:
#     print(num)

# 3)在字典中存储字典
# fruits = {
#     'apple': {
#         'color': 'red',
#         'taste': 'delicious'
#     },
#     'banana': {
#         'color': 'yellow',
#         'taste': 'Great'
#     }
# }
# for name, nature in fruits.items():
#     print(f"Fruit's name:{name}")
#     print(f"color:{nature['color']}")
#     print(f"taste:{nature['taste']}")
#     print('\n')

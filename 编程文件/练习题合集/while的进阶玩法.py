# 1.使用while循环处理列表和字典

# 1)在列表之间移动元素
user1 = ['苹果', '香蕉', '橘子']
user2 = []
user3 = ['苹果', '香蕉', '橘子', '1', '2', '1', '4', '1', '6', '7', '2', '9']
# while user1:
#     num1 = user1.pop()
#     print(f"{num1.title()}已经验证啦")
#     user2.append(num1)
# for num in user2:
#     print(f"已经通过验证的元素有{num}")

# 2)删除为特定值的所有列表元素
# print(user3)
# while '1' in user3:
#     user3.remove('1')
# print

# 3)使用用户输入来填充字典
print('请输入需要加入的水果：(没有了请输入no退出哦)')
while True:
    elem = input()
    if elem == 'no':
        break
    user1.append(elem)
print(user1)
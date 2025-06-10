# 这个使用的是切片法，教材上使用的是下标法
def judge(str1):
    if len(str1) % 2 == 0:
        len1 = int(len(str1) / 2)
        teststr1 = str1[len1:]  # 前面加负号表示获取从下标len1之后所有的元素
        teststr2 = str1[:len1]
        teststr3 = teststr1[::-1]
        # print(teststr3)
        if teststr3 == teststr2:
            print('这是一个回文串')
        else:
            print('这不是回文串')

    if len(str1) % 2 != 0:
        len1 = int(len(str1) / 2)
        teststr1 = str1[len1 + 1:]
        teststr2 = str1[:len1]
        teststr3 = teststr1[::-1]
        if teststr3 == teststr2:
            print('这是一个回文串')
        else:
            print('这不是一个回文串')


str1 = input()
judge(str1)


"""num=0
for i in'hello':
    num+=1
    print(num,i)
for i in range(1,11):
    if i % 2==0:
        print(i,'是偶数')
    else:
        print(i,'是奇数')"""


"""for i in  range(1000,2000):
    if i%3==0:
        print(i,'是三的倍数')
    else:
        print(i,'不是三的倍数')"""

"""anser=input('今天上课吗?y\n:')
while anser=='y':
    print('好好学习，天天向上')
    anser=input('今天上课吗？y\n:')"""

"""s=0
i=1
while i<=100:
    s+=i
    i+=1
else:
    print('1-100之间的累加和：',s)"""

"""i=0
while i<3:
    user_name=input('请输入您的用户名：')
    pwd=input('请输入您的密码：')
    if user_name=='ysj' and pwd=='888888':
        print('系统正在登陆，请稍后')
        i=4
    else:
        if i<2:
          print('用户名或密码不正确，您还有',2-i,'次机会')
        i+=1
    if i==3:
        print('对不起，三次均输入错误')"""


"""for i in range(0,3):
    for j in range(0,4):
        print('*',end='')
    print()
print('---------------------------')

for i in range(0,6):
     print('*'*i)
print('------------------------------------------')

for i in range(0,6):
    print('*'*(6-i))
print('------------------------------------------')

for i in range(1,6):
    print(' '*(5-i)+'*'*(2*i-1))
print('------------------------------------------')

for i in range(1,5):
    print(' '*(4-i)+'*'*(2*i-1)+''*(4-i))
for i in range(1, 4):
    print(' ' *i + '*' * (2*(4-i)-1)+''*i)
print('------------------------------------------')
print('  * ')
print(' * *')
print('*   *')
print(' * * ')
print('  *  ')"""

"""for i in 'hello':
    if i=='e':
        break
    print(i)
print('---------------------------')
for i in range(0,3):
    user_name=input('请输入您的用户名：')
    pwd=input('请输入您的密码：')
    if user_name=='ysj' and pwd=='888888':
        print('系统正在登陆，请稍后')
        break
    else:
        if i<2:
          print('用户名或密码不正确，您还有',2-i,'次机会')
        i+=1
else :
        print('对不起，三次均输入错误')"""

"""s=0
i=1
while i<=100:
    if i%2==1:
        i+=1
        continue

    s+=i
    i+=1
print('1-100之间的偶数和',s)"""


"""if True:
    pass
while True:
    pass"""





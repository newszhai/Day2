"""4.1
name='张三'
age=20
a=b=c=d=100
a,b,c,d='room'
print(a)
print(b)
print(c)
print(d)
print('---------输入/输出语句也是典型的顺序结构--------')
name=input('请输入您的姓名；')
age=eval(input('请输入您的年龄:'))"""


"""4.2
number=eval(input('请输入您的6位中奖号码'))

if number==987654:
  print('恭喜你中奖了！')
if number!=987654:
  print('您未中本期大奖！')

print('---------以上if判断的表达式，是通过比较运算符计算出来的，结果是布尔值类型----')
n=98
if n%2: 
   print(n,'是奇数')
else:
    print(n,'是偶数')
n=98
if not n%2:
    print(n,'为偶数')
print('-------判断一个字符串是否是空字符串-------')
x=input('请输入一个字符串：')
if x:
    print('x是一个非空字符串')
if not x:
    print('x是一个空字符串')
print('----表达式也可以式一个单纯的布尔型变量-----')
flag=eval(input('请输入一个布尔类型的值True或False'))
if flag:
    print('flag的值是True')
if not flag:
    print('flag的值是False')"""


"""print('=-=-==-===-=-使用if语句时，如果语句块中只有一句代码')
a=10
b=5
if a>b:max=a
print('a和b的最大值',max)"""


"""score=eval(input('请输入您的成绩：'))
if score<0 or score>100:
    print('成绩有误！')
elif 0<=score<60:
    print('E')
elif 60<=score<70:
    print('D')
elif 70<=score<80:
    print('C')
elif 80<=score<90:
    print('B')
else:
    print('A')"""

"""answer=input('请问，您喝酒了吗？')
if answer=='y':
    proof=eval(input('请输入酒精含量'))
    if proof<20:
        print('构不成酒驾，一路平安')
    elif proof<80:
        print('已构成酒驾，请不要开车')
    else:
        print('已构成醉驾标准，千万不要开车')
else:
    print('你走吧，安全通过')"""

user_name=input('请输入您的用户名：')
pwd=input("请输入您的密码：")
if user_name=='ysj' and pwd=="888888":
    print('登陆成功')
else:
    print('用户名或密码不正确')
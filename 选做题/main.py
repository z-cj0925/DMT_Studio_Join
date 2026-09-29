"""

本代码演示了
各类字面量的写法
通过print语句输出
"""
from math import fsum

# 写一个整数字面量
88888
# 写一个浮点数字面量
13.14
# 写一个字符串字面量
"去码头整点薯条"



print("13.14")
print("去码头整点薯条")




# 定义一个变量 来记录钱包余额
money=50
# 通过print语句 输出变量记录的内容
print("钱包还有:",money)

# 买了一个冰淇淋 花费10元
money=money-10
print("买了冰淇淋花费10元，还有:",money,"元")

# 假设 每隔一小时 输出一个钱包的余额
print("现在是下午1点，钱包还剩:",money)
print("现在是下午2点，钱包还剩:",money)
print("现在是下午3点，钱包还剩:",money)
print("现在是下午4点，钱包还剩:",money)
money=50
money=money-15
print("买了一个冰淇淋和可乐，还有：",money,"元")
# 方式一: 使用print直接输出类型信息
print(type(888))
print(type(13.14))
print(type("去码头整点薯条"))
#  方式二： 使用变量储存type()语句的结果
string_type=type("老鼠爱大米")
int_type=(666)
flot_type=(1.1)
print(type(string_type))
print(type(int_type))
print(type(flot_type))
# 方式三： 使用type（）语句，查看变量储存的数据类型信息
name="老鼠爱大米"
name_type=type(name)
print(type(name))





# 将数字类型转换成字符串
num_str=str(11)
print(type(num_str),num_str)
print(type(11))
print(type(num_str))
X=str(11)
print(type(X),X)
x=str(1.1)
print(type(x),x)
# 将字符串类型转换成数字
y=int(99.99)
print(type(y),y)
num_str=("11")
print(type(num_str),num_str)
num_str=float("11")
print(type(num_str),num_str)

# 7.11第一次复习
# 字符串
print("紫菜卷")
print('你好世界')
# 整数
print(5201314)
# 浮点数
print(3.1415926)
# 注释,单行，多行
#
"""

本代码进行了第一次
paython基础语法复习
时间为7月11
"""
#变量
money=10086
money=money /160
print("一张专票花费160元一共可以抽：",money,"抽")

# 数据类型
print(type("紫菜卷"))
print(type(5201314))
print(type(3.1415926))


# 规则一： 内容限定，限定只能使用中文，英文，数字，下划线，数字不能开头，特殊符号
name_1='张三'
# 规则二，大小写敏感
ID="橙子"
id=666
# 规则三 ：不可使用关键字
# class+1
# def=1
Class=1
# 算数（数字）运算符 加+ 减- 乘* 除/ 取整数//  取余数%  指数**
print("1+1=",1+1)
print("2-1=",2-1)
print("3*3=",3*3)
print("4/2=",4/2)
print("9//2=",9//2)
print("9%2=",9%2)
print("2**2=",2**2)


# 赋值运算符
num=(1+2*3)
# 复合赋值运算
# 加+=  减-=  除/=  取整数//=  取余数%=  指数**=
num=1
num+=1
print("num+=1",num)# 2
num-=1
print("num-=1",num) #1
num*=4
print("num*=4",num)  #4
num/=2
print("num/=2",num) #2
num//=1.1
print("num//=1,1",num) #1
num%=2
print("num%=2",num) #1
num**=2
print("num**=2",num) #1

# 单引号定义法 使用单引号进行包围
name='紫菜卷'
print(name)
# 双引号定义法 使用双引号进行包围
name="紫菜卷"
print(name)
# 三引号
name="""紫菜卷"""
print(name)
# 字符内包含引号
name="'紫菜卷’"
print(name)
# 使用转义字符\解除引号的效用
name="\'紫菜卷\'"
print(name)
name='\'紫菜卷\''
print(name)

# 字符串拼接
# 字符串和字面量拼接
print("会萤的"+"紫菜卷")
# 变量
print("会萤的"+name)
# 加号只能拼接字符串
tel=str(10086)
print("我的电话是"+tel)

# 字符串格式化
# 通过占位的形式完成拼接
name="紫菜卷"
message='会萤的%s'%name
print("终于走到这里了,",message)

# 通过占位的形式，完成数字和字符串的拼接
num=666
salary=10000
message="paython数据分析，第%s期，毕业薪资为：%s" %(num,salary)
print(message)
name="紫菜卷"
year=18
price=0.7
message="我是：%s我今年:%d,我今年的价格是%f"%(name,year,price)
print(message)



# 字符串格式化 - 精度控制
num1=11
num2=11.345
print("数字11宽度设置为:5结果是：%5d"%num1)
print("数字11宽度设置为:1,结果是:%1d"%num1)
print("数字11.345宽度设置为7，小数精度2，结果是:%7.2f"%num2)
print('数字11.345不限制，小数精度2，结是：%2f'%num2)
# 字符串转化 快速写法
name='紫菜卷'
born=1900
price=7.99
print(f"我是{name}，为出生于：{born},我的价格是{price}")

# 字符串格式化-表达式的格式化
print("1*1的结果是：%d"%(1*1))
print(f'1*1的结果是：{1*1}')
print("字符串在paython中的类型是%s:"%type("字符串"))
# 数据输入input()
# print("请告诉我你是谁")
# name=input()
# print("你好！我是%s:"%name)

# 输入数字类型
# num=input("请告诉我你的银行卡号码")
# num=int(num)
# print("您当前银行卡号密码的类型是什么：",type(num))
# 输入的无论什么都会被认为是字符串
# 定义变量：存储数据紫菜卷
# my_name="紫菜卷"
# print(my_name)


# 定义变量：存储数据 黑马程序员
school_name="我是紫菜卷"
print(school_name)
""""
# 准备数据
# 格式化符号输出数据
"""
age=18
name="紫菜卷"
weight=62
stu_id=30

# 今年我的年龄是x岁--整数%d
print('今年我的年龄是%d岁'%age)

print('我的名字是%s'%name)

print('我的体重是%.3f'%weight)

print('我的学号是%03d'%stu_id)


print('我的名字是%s,我的年龄是%d'%(name,age))


# 语法f'{表达式}
print(f'我的名字是{name},今年{age}了')

# 结束符end=
# \n换行    \t 制表符
print('hello',end='\n')
print('world',end='\t')

# bool布尔型，通常判断用,有两个取值Ture,Flase
b=True
print(type(b))
result=10>5
print(f"10>5的结果是{result}，类型是{type(result)}")
result="itcast"=="itheima"
print(f"字符串是否相等，结果是：{result}")
# 比较符运算符的使用
# ==,!=,>,<,>=,<=

c=[10,20,30]
print(type(c))


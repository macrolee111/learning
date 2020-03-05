#元组
place_1=(1,2)
print('longitude',place_1[1])
dimensions= 1,2,3
lenth,width,height =dimensions
print(lenth)
print('the dimensions are{}*{}*{}'.format(lenth,width,height))
#list  可以变化，有顺序，tuple不能变化，有顺序，几何，无顺序，可以变化
#集合和列表去重
palce=['beijing','shanghai','shanghai']
unique_place=set(palce)
print(unique_place)
#add加上 pop取出东西
print('london' in unique_place)
number={1,2,3,4,5,6,7,8}
number.add(9)
print(number)
#字典 打印的为定义下面的解释
names={'tom':'tom is very tall','william':'william is very handsome.'}
print(names['william'])
#字典 get 不管有没有 程序不会崩溃
print(names.get('mary'))
print(names.get('tom'))
#恒等运算符
x=names.get('mary')
print(x is None)
print(x is not None)
#字典get自定义返回值
dic={'tom':'tom is my father','mary':'mary is my son'}
print(dic.get('willim','there is no william'))
print(dic.get('mary','there is no mary'))
#‘=‘ ’==‘ ’is'辨析
a=[1,2,3,4,5,6,7,8]
b=a
c=[1,2,3,4,5,6,7,8]
print(a==b)
print(a is b)
print(a==c) 
print(a is c) 
#复合数据结构 字典里再加一个字典
people={'tom':{'height':175,'weight':'80kg'},'marry':'she is hot','william'}
tom=people['tom']
tom_weight=people['tom']['weight']
print('tom')
print(tom_weight)
#数据类型和运算符总复习
int(4.0)
float(5) #浮点数
type(5.7) #
str('this is me') #字符串
#布尔值 true false
#list 有顺序 可以变
list=[1,2,'3',3]
#元组 ，有顺序，不可变
tuple=(1,2,3,4,5)
#set集合 没顺序，可以变 对list进行处理，有重复的可以去掉
set=<1,2,3,4,5,>
#字典 不可变 key，解释
dict={'1':1,'2':2}
#运算符
#= - * / 幂运算 2**3 余9%2 除了整数9//2 ==
#逻辑运算 and or not
1<2 and 2<3
1<2 or 2<1
not 1>3
#add加上 pop取出东西

#条件语句
client_balance = 100
bank_banlance = 1000000000

print('you have'+str(client_balance)+'rmb in your game balance' +
      'you have'+str(bank_banlance)+'in your bank balance')

if client_balance < 2000:
     client_balance += 1500
     bank_banlance-+1500
print('you have'+str(client_balance)+'rmb in your game balance' +
      'you have'+str(bank_banlance)+'in your bank balance')

people = 'mary'
if people == 'mary':
    print('hello mary')
elif people == 'tom':
    print('hello tom')
else:
    print('go away')

#if 后面的复杂布尔表达式
height = 1.76
weight = 60
if 18.5 <= weight/height**2 <= 25:
    print('well you are in good shape'+str(weight/height**2))
else:
    print('well,you need to work harder'+str(weight/height**2))

tall = true
rich = true
handsome = false
if tall and rich and handsome:
    print('he is the one')
else:
    print('pass')

#for循环
names = ['tom', 'mary', 'jimmy', 'william']
capitalized_name = []
for name in names:
    capitalized_name.append(name.title)
print(capitalized_name)

#range 到100结束，star=0 stop=，step=2 可以理解为番位
for a in range(100):
    print('i am the best')
a = list(ange(100))
print(a)

names = ['marry', 'william', 'tom', 'garry']
for index in range(len(names)):  # 从第一个长度len到最后
    names[index] = names[index].title()  # 重新命名name

print(names)

names = ['mary wang', 'william wang ',
         'tom wang']
names_news = []
for name in names:
    names_new.append(name.lower().replace(' ', '_'))
print(names_news)

names = {'mary wang': 'she is ver nice', 'william wang ', : 'she it bad',
         'tom wang': 'he is rich'}  # key是前面的  value是冒号后面的
for key in names:
    print(key)
for key, value in names.items():
    print('nams:{}     saying:{}'format(key, value))

#while 一直循环循环到限定的 break 断开 continue从头进行循环
dect = [1, 2, 3, 4, 5, 6, 7, 8, 9]
equipped = []

while sum(equipped) <= 20:
    equipped.append(deck.pop())
print(equipped)

while True:
    word = input('enter sring to capitalize[type q to quit]:')
    if word == 'q':
        break
    print(word.title())

while True:
    value = input('even number please[enter q to quit]')
    if value == 'q':
        break
    number = int(value)
    if number % 2 == 0:
        continue
    print('i said even number,are you blind?!')

#zip迭代器，返回多个迭代的对象
names = ['william', 'marry', 'tommy', 'jimmy']
height = [185, 175, 173, 164]
list(zip(names, height))
print(list)

names = ['william', 'marry', 'tommy', 'jimmy']
# range 为从0开始的迭代，对应，0，1，2，3，4 zip将两个结合，成为了zip
for i, name in zip(range(len(names)), names):
    print(i+1, name)

#自定义函数


def add(num1, num2):  # 头部
    result = (num1+num2)  # 定义函数
    return print(result)  # 最终返回输出什么


def supper_add(num1, num2, super_num3=10000):
    result = (num1+num2)*super_num3
    return print(result)

#贷款到期日拆分提醒


def remainder(days):
    years = days//365
    mouths = (days % 365)//30
    days_rem = (day % 365) % 30
    return"{}year(s){}month(s){}and {}days remain."format(yeas, months, days_rem)

#写文档 pe.__doc__


def pe(price, earning):
    """calculate pe ratio
    INPUT：
    price :int or float .the price of the stock you choose .
    earning: int or float. the earning og the stock you choose

    output:
    pe:price /earing.the pe ratio of the stock you choose
    """
    pe = price/earning
    return print(pe)


#lambda表达式 创建一个匿名函数
def super_add(num1, num2): return num1+num2


#高阶内置函数filter（）筛选
#filter()可叠戴对象进行输入
names = ['tom', 'william', 'tommy', 'sdufhasfhkashfkasjnf',
         'dhsfsdafgasgfakjsfhjkasgfashfsahjfhsafh']


def fake_name(name):
    return len(name) > 20


fake_name_list = list(filter(fake_name, names))
print(fake_name_list)

#map()函数 高阶函数，套入函数 返回的是迭代器


def square(x):
    return x**2


list_1 = [1, 2, 3, 4, 5, 6, 7]
a = map(square, list_1)
print(list(a)

      score_cards=[[1, 2, 3, 4, 5, 6, 7], [
          1, 5, 4, 3, 4, 2, 3, 4], [7, 3, 4, 2, 4, 2, 23, 2]]
      def mean(score_list):
      return sum(score_list)/len(score_list)
      average_score=list(map(mean, score_cards))
      print(average_score)

      score_cards=[[1, 2, 3, 4, 5, 6, 7], [
          1, 5, 4, 3, 4, 2, 3, 4], [7, 3, 4, 2, 4, 2, 23, 2]]
      average_score=list(map(lambda x: sum(x)/len(x), score_card))
      print(average_score)

      #迭代器 表示数据流对象 是数据流 并无法打印 enumberate 报数
      list_1=[1, 2, 3, 4, 5, 3, 1]
      print(list(enumerate(list_1)))

      #生成器生成迭代器 生成器可以用 def和yield生成一个迭代器 节约内存 不用输入list里面的东西。迭代期可以生成需要的数字
      def my_range(x):
      a=0
      while a < x:
      yield a
      a += 1

      print(list(my_range(99)))
      for x in my_range(20):
      print(x)

      #创建自己的enumberate
      stpes=['python', 'git', 'deap', 'ai']

      def my_enumberate(iterable, strat=0):
      count=strat
      for element in iterable:
      yield count, element
      connt += 1

      for i, step in my_enumberate(stpes, 1):
      print('step{}:{}'.format(i, step))

      #数据处理
      #编写生成器对大数据进行拆分
      def chunker(iterable, size):
      for i in range(0, len(iterable), size):
      yield iterable[i:i+size]

      for chunk in chunker(range(100), 20):
      print(list(chunk))

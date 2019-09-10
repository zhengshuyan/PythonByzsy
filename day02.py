# 1.
# import math 
# a = float(input('输入a:'))
# b = float(input('输入b:'))
# c = float(input('输入c:'))
# if b**2 - 4*a*c > 0:
#     r1 = (-b + math.sqrt(b**2 - 4*a*c))/2*a
#     r2 = (-b - math.sqrt(b**2 - 4*a*c))/2*a
#     print(r1,r2)
# elif b**2 - 4*a*c == 0:
#     r1=r2=(-b + math.sqrt(b**2 - 4*a*c))/2*a
#     print(r1)
# else:
#     print('此方程无根')


# # 2.
# import random
# correctCount = 0
# count = 0
# num1 = random.randint(0,100)
# num2 = random.randint(0,100)
# if num1 < num2:
#     num1,num2 = num2,num1
# answer = eval(input('计算'+str(num1)+"-"+str(num2)+"="))
# if answer == num1 - num2:
#     print('赢')
#     correctCount += 1
# else:
#     print('输.\n',num1,"-",num2,'is',num1 - num2)


# 3.
# num = float(input('输入今天是一周中的哪一天的数字'))
# day = float(input('输入今天之后到未来某天的天数'))
# num_ = (num + day)%7
# if num_ == 0:
#     print('周日')
# elif num_ == 1:
#     print('周一')
# elif num_ == 2:
#     print('周二')
# elif num_ == 3:
#     print('周三')
# elif num_ == 4:
#     print('周四')
# elif num_ == 5:
#     print('周五')
# else:
#     print('周六')


# 4.
# num1,num2,num3=map(int,input('请输入三个整数：').split())
# min = min(num1,num2,num3)
# max = max(num1,num2,num3)
# print('升序为：%d %d %d' %(min,num1+num2+num3-min-max,max))


5.
# a = float(input('输入第一种大米的重量：'))
# b = float(input('输入第一种大米的价格：'))
# c = float(input('输入第二种大米的重量：'))
# d = float(input('输入第二种大米的价格：'))
# # a,b =  map(int,input('输入第一种大米的重量和价格：').split())
# # c,d =  map(int,input('输入第二种大米的重量和价格：').split())
# mi1 = float(b/a)
# mi2 = float(d/c)
# if mi1 > mi2:
#     print('第二种大米比较实惠')
# elif mi1 == mi2:
#     print('两种大米一样')
# else:
#     print('第一种大米比较实惠')


# 6.
# n = int(input('输入一个年份：'))
# y = int(input('输入一个月份：'))
# #n,y = map (int,input('输入一个年份和月份：').split())
# if (y == 1 or y == 3 or y == 5 or y == 7 or y == 8 or y == 10 or y == 12) and 1<=y<=12:
#     print('%d年%d月有31天'%(n,y))
# elif( y == 4 or y == 6 or y == 9 or y == 11) and 1<=y<=12:
#     print('%d年%d月有30天'%(n,y))
# else:
#    if (n % 4 == 0 and n % 100 == 0) or (n % 400 ==0):
#      print('%d年%d月有29天'%(n,y))


# 7.
# import random
# a =  int(input('猜测硬币正反面：'))
# b = random.randint(0,1)
# if b == 1:
#     print('正面')
# else:
#     print('反面')
# if a == b:
#     print('猜对了')
# else:
#     print('猜错了')


# 8.
# import numpy as np
# computer = np.random.randint(0,2)
# user =  int(input('0:石头,1:剪刀,2:布'))
# if computer == user:
#     print('平局')
# elif computer == '0' and user == '1':
#     print('user输')
# elif computer == '1' and user == '2':
#     print('user输')
# elif computer == '2' and user == '0':
#     print('user输')
# else:
#     print('user赢')


# 9.
# year = int(input('输入年份:'))
# month = int(input('输入月份(1-12):'))
# day = int(input('输入这个月的某一天(1-31):'))
# if month == 1:
#     month =13
#     year -= 1
#     h = (day +(26 * (month + 1)/ 10) +(year%100) +((year%100)/4) +((year/100)/4) +5* (year/100))%7
# elif month == 2:
#     month = 14
#     year -= 1
#     h = (day + (26 * (month + 1)/ 10) + (year%100) + ((year%100)/4) + ((year/100)/4) + 5* (year/100))%7
# else:
#     h = (day + (26 * (month + 1)/ 10) + (year%100) + ((year%100)/4) + ((year/100)/4) + 5* (year/100))%7
#     h = h//1
#     print(h)
#     if h==2:
#         print('今天周日')
#     elif h==3:
#         print('今天周一')
#     elif h==4:
#         print('今天周二')
#     elif h==5:
#         print('今天周三')
#     elif h==6:
#         print('今天周四')
#     elif h==0:
#         print('今天周五')
#     elif h==1:
#         print('今天周六')


# 10.
# import numpy as np
# num = int(input('输入你选择的牌的大小:'))
# print('扑克牌的大小分别为：1(Ace)、2、3、4、5、6、7、8、9、10、11(Jack)、12(Queen)、13(King)')
# print('扑克牌的花色分别为:1:梅花、2:红桃、3:方块、4:黑桃')
# num1 = np.random.randint(1,14)
# if num == 1:
#     print('你选择的是:Area')
#     num2 = np.random.randint(1,5)
# if num2 ==1:
#     print('梅花')
# elif num2 ==2:
#     print('红桃')
# elif num2 ==3:
#     print('方块')
# else:
#     print('黑桃')


# 11.
# num = float(input('判断是否是回文数,请输入一个三位整数:'))
# num1 = num//100 
# num2 = num%10
# num3 = (num - 100)//10 
# if num1 == num2:
#     print('是一个回文数')
# else:
#     print('不是回文数')


# 12.
# a = float(input('输入三角形的a边长'))
# b = float(input('输入三角形的b边长'))
# c = float(input('输入三角形的c边长'))
# if a+b>c and a+c>b and b+c>a:
#     print('能够成三角形')
#     print('三角形的周长是:%d' %(a+b+c))
# else:
#     print('不能够组成三角形')



# 13.
# def main():
#     num_z = 0
#     num_f = 0
#     sum = 0
#     data = 1
#     while data != 0:
#         data = int(input('请输入数字：'))
#         if data > 0:
#             num_z += 1
#         elif data < 0:
#             num_f +=1
#         sum += data
#     print('正数个数为:%d'%num_z)
#     print('负数个数为:%d'%num_f)
#     aver = sum / (num_z + num_f)
#     print('平均值为：%2f'%aver)
# main()


# 14.
# def main():
#     money = [1000]
#     for i in range(10):
#         x = money[i] * 1.05
#         money.append(x)
#     print('十年后的学费：%.2f'%money[10])
#     print('现在及十年后的学费：%.2f'%sum(money))   
# main() 


# 15.
# def main():
#     count = 0
#     for i in range(100,1000):
#         if i % 5 == 0 and i % 6 == 0:
#             print(i,end = ' ')
#             count += 1
#             if count % 10 ==0:
#                 print("\n")
#         else:
#             continue           
# main()


# 16.
# def main():
#     n2 = 0
#     n3 = 0
#     while n2 ** 2 < 12000:
#         n2 += 1
#     #最小的n满足n^2 > 12000的数字
#     print(n2)#110
#     while n3 ** 3 < 12000:
#         n3 += 1
#     #最小的n满足n^3 < 12000的数字
#     print(n3-1)#22
# main()


# 17.
# def main():
#     sum = 0
#     for i in range(1,50001):
#         sum += 1/i
#     print(sum)
# main()


# 18.
# def main():
#     sum = 0
#     for i in range(1,98,2):
#         sum += i/(i + 2)
#     print(sum)
# main()


# 19.
# def main():
#     sum = 0
#     for i in range(1,100000):
#         sum += 4 * (-1) ** (i + 1) / (2 * i - 1)
#     print(sum)
# main()


# 20.
# def main():
#     for i in range(1,10000):
#         sum = 0
#         for j in range(1,i):
#             if i % j ==0:
#                 sum += j
#         if i ==sum:
#             print(i)
# main()


# 21.
# def main():
#     count = 0
#     for i in range(1,8,2):
#         for j in range(2,8):
#             if i != j:
#                 print(i,j)
#                 count += 1
#     print(count)
# main()


22.
number = []
he = 0
for i in range(10):
    data = float(input('请输入10个数字：'))
    number.append(data)
average = sum(number) / len(number)
for x in number:
    cha = (average - x) ** 2
    he += cha
st = (he / (len(number)-1)) ** 0.5
print('The mean is %f'%average)
print('The Standard deviation is %f'%st)












            














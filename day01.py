# 1.
# C = float(input('输入摄氏温度'))
# F = (9/5)*C + 32
# print('%.2F 华氏度' %F)


# 2.
# import math
# r = float(input('输入圆柱半径:'))
# l = float(input('输入圆柱高:'))
# area = r*r*math.pi
# volume = area*l
# print('面积:%.2f' %area)
# print('体积:%.2f' %volume)


# 3.
# feet = float(input('请输入英尺数：'))
# meters = feet * 0.305
# print('%.1ffeet is %.4fmeters'%(feet,meters))


# 4.
# M = float(input('输入按千克计算的水量:'))
# initialTemperature = float(input('输入水的初始温度:'))
# finalTemperature = float(input('输入水的最终温度:'))
# Q = M * (finalTemperature-initialTemperature)*4184
# print('所需能量:%.1f%Q',Q)


# 5.
# balance = float(input('输入差额:'))
# interest_rate = float(input('输入年利率：'))
# interest = balance*(interest_rate/1200)
# print('下月需付利息:%.5f' %interest)


# 6.
# v0 = float(input('输入初始速度：'))
# v1 = float(input('输入末速度：'))
# t = float(input('输入速度变化所占用的时间：'))
# a =(v1-v0)/t
# print('平均加速度为:%.4f' %a)


# 7.
# num = float(input('输入每月存款数:'))
# rate =0.05/12
# interest = 1+rate
# count=[0]
# for i in range(6):
#     month = (100+count[i]*interest)
#     count.append(month)
# print('六个月后的账户总额:%.2f' %count[6])


8.
# num = int(input("请输入1-1000的一个整数："))
# bai = int(num%10)
# shi = int(num/10%10)
# ge = int(num/100)
# sum = ge + shi + bai
# print('各位数字之和:' ,sum)


# 9.
# import math
# r = float(input('输入顶点到中心的距离:'))
# s = 2*r*math.sin(math.pi/5)
# area = 5*s*s/(4*math.tan(math.pi/5))
# print('五边形的面积%.2f' %area)


# 10.
# import math 
# print ('输入第一个坐标:')
# x1 = float(input('>'))
# y1 = float(input('>'))
# print ('输入第二个坐标:')
# x2 = float(input('>'))
# y2 = float(input('>'))
# radius = 6371.01
# math.radians = float(input('输入地球表面的经度:'))
# math.arccoss = float(input('输入地球表面的纬度:'))
# d = math.radians * math.arccos(math.sin(math.radians(x1)) * math.sin(math.radians(x2)) + math.cos(math.radians(x1)) * math.cos(math.radians(x2)) * math.cos(math.radians(y1-y2))
# print ('%d' %d)


10.
# import math
# x1,y1 = eval(input('Please input point1(latitude and longitude) in degrees:'))
# x2,y2 = eval(input('Please input point2(latitude and longitude) in degrees:'))
# radius = 6371.01
# x11 = math.radians(x1) #math.radians()函数将度数转换成弧度数
# y11 = math.radians(y1)
# x22 = math.radians(x2)
# y22 = math.radians(y2)
# d = radius * math.acos(math.sin(x11) * math.sin(x22) + math.cos(x11) * math.cos(x22) * math.cos(y11-y22))
# print('The distance between the two points is %5.2f km'%d)


# 11.
# import math
# s = float(input('输入五角星的边长:'))
# area = (5*s*s)/(4*math.tan(math.pi/5))
# print('五角星的面积为：%.2f',area)


# 12.
# import math
# n = int(input('输入边数：'))
# s = float(input('输入正多边形的边长：'))
# area = (n * s * s) / (4 * math.tan (math.pi / n))
# print('%.2f',area)


# 13.
# ASCII = int(input('输入整数=>'))
# print(chr(ASCII))


# 14.
# name = (input('姓名：'))
# workhour = int(input('一周工作时间：'))
# many = float(input('每小时的报酬：'))
# lianbang = float(input('联邦预扣税率：'))
# zhou = float(input('州预扣税率：'))
# rate1 = workhour * many
# print(rate1)
# print('Deduction:')
# faderal = rate1 * lianbang
# print(faderal)
# state = rate1 * zhou
# print(state)
# zongmany = rate1 -(faderal + state)
# print(zongmany)


15.
# num = input('输入一个四位整数数字：')
# for i in range(len(num)):
#      print(num[-i + len(num)-1],end='')


# # 16.
# import hashlib
# a = input('请输入一行文本:') 
# m = hashlib.md5()
# b = a.encode(encoding='utf-8')
# m.update(b)
# a_md5 = m.hexdigest
# print('md5加密前为:'+a)
# print('md5加密前为:'+a_md5)


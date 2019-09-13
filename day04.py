# #1.成绩分级
# def ScoreGrade()):
#     list1=list(map(int,input('Please enter score:').split(',')))
#     list2=sorted(list1)
#     best=list2[-1]
#     for i in range(0,len(list1)):
#         if best>=list1[i]>=best-10:
#             print('Student %d score is %d and grade is A !'%(i,list1[i]))
#         elif best-10>list1[i]>=best-20:
#             print('Student %d score is %d and grade is B !'%(i,list1[i]))
#         elif best-20>list1[i]>=best-30:
#             print('Student %d score is %d and grade is C !'%(i,list1[i]))
#         elif best-30>list1[i]>=best-40:
#             print('Student %d score is %d and grade is D !'%(i,list1[i]))
#         else:
#             print('Student %d score is %d and grade is E !'%(i,list1[i]))
# if __name__ == '__main__':
#     ScoreGrade()

# #2.逆序读取列表
# def Nixu():
#     list_ = list(map(int,input('Please enter integers：').split(',')))
#     print(list_[::-1])
# if __name__ == '__main__':
#     Nixu()

# #3.统计列表里元素的个数
# def Statistics():
#     list_=list(map(int,input('Please enter integers between 1 and 100：').split(',')))
#     set_=set(list_)
#     for i in set_:
#         number=0
#         for j in list_:  
#             if j==i:
#                 number+=1
#         print('Number %d has %d '%(i,number))
# if __name__ == '__main__':
#     Statistics()

# 
# #4.输出最小元素的下标
# def IndexOfSmallestElement():
#     list1=list(map(int,input('Please enter a list of numbers:').split(',')))
#     list2=sorted(list1)
#     num=0
#     for i in list1:
#         if i==list2[0]:
#             print('The subscript of the smallest element is：%d'%num)
#         else:
#             num+=1
# if __name__ == '__main__':
#     indexOfSmallestElement()

# #5.打乱一个列表并返回这个列表
# import random
# lst=list(map(int,input('Please enter a list of number:').split(' ')))
# def Shuffle(lst):
#     random.shuffle(lst)
#     for i in lst:
#        print(i,end=' ')
# if __name__ == '__main__':
#     Shuffle(lst)

# #6.消除重复
# lst=list(map(int,input('Please enter a list of number:').split(' ')))
# def eliminateDupLicates(lst):
#     set1=set(lst)
#     for i in set1:
#         print(i,end=' ')   
# if __name__ == '__main__':
#     eliminateDupLicates(lst)

# #7.检测是否排序
# lst=list(map(int,input('Please enter a list of number:').split(' ')))
# def isSorted(lst):
#     if lst != sorted(lst):
#         print('Not sorted !')
#     else:
#         print('Already sorted !')
# if __name__ == '__main__':
#     isSorted(lst)

# #8.冒泡排序
# lst=list(map(int,input('Please enter a list of number:').split(' ')))
# def MaoPaoSort(lst):
#     while lst != sorted(lst):
#         for i in range(0,len(lst)-1):
#             if lst[i] > lst[i+1]:
#                 lst[i],lst[i+1] = lst[i+1],lst[i] #不能分两行写，会刷新列表
#     else:
#         print(lst)
# if __name__ == '__main__':
#     MaoPaoSort(lst)


# #9..判断序列包含具有相同值的连续四个数字
# def isconsecutivefour():
#     num=0
#     list_=list(map(int,input('请输入一个整数序列（用逗号隔开）:').split(',')))
#     for i in range(0,len(list_)-3):
#         if list_[i]==list_[i+1]==list_[i+2]==list_[i+3]:
#             if num==0:
#                 print('这个序列包含具有相同值的连续四个数字！')
#                 num+=1
#     if num==0:
#         print('不包含！')
# if __name__ == '__main__':
#     isconsecutivefour()

# #10.检测SSN
# def Ssn():
#     ssn='111-222-3333'
#     list_=str(input('请输入SSN号码（ddd-ddd-dddd）:'))
#     a=list_[0]+list_[1]+list_[2]
#     b=list_[4]+list_[5]+list_[6]
#     c=list_[8]+list_[9]+list_[10]+list_[11]
#     if a+'-'+b+'-'+c == ssn:
#         print('Ture')
#     else:
#         print('False')
# if __name__ == '__main__':
#     Ssn()

# #11.
# def Find():
#     a=str(input('请输入第一个字符串：'))
#     b=str(input('请输入第二个字符串：'))
#     res=b.find(a)
#     if res==-1:
#         print(a,'不是',b,'的子串')
#     else:
#         print(a,'是',b,'的子串')
# if __name__ == '__main__':
#     Find()



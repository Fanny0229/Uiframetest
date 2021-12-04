# list1 = [1,2,3,4,5]
# def fun():
#     list1.append('添加了')
#     print(list1)
# fun()
# print(list1)

# num=int(input('请输入一个整数:'))
# num_n=input('请输入%d个整数，并用逗号隔开:' %num)
#
# num_list=num_n.split(',')
# num_list=list(map(int,num_list))
#
# for m in range(num-1):
#     for n in range(num-1-m):
#         if num_list[n]>num_list[n+1]:
#             num_list[n],num_list[n+1]=num_list[n+1],num_list[n]
# print(num_list)
# a_list=[]
# for m in range(num-1):
#      a_list.append(num_list[m+1]-num_list[m])
# print(a_list)
# b_list=sorted(a_list)
# print(b_list)
# print(b_list[0])

num=int(input('请输入一个整数:'))
num_n=input('请输入%d个整数，并用逗号隔开:' %num)

num_list=num_n.split(',')
num_list=list(map(int,num_list))

div_list=[]
for m in range(num):
    for n in range(num):
        if m!=n:
            div_list.append(abs(num_list[m]-num_list[n]))
print(div_list)
print(min(div_list))

for m in range(num):
    for n in range(num):
        if m!=n:
            if abs(num_list[m]-num_list[n])==min(div_list):
                print(num_list[m],num_list[n])


with open('bcbx.txt','r',encoding='utf-8') as readfile:
    num_bcbx=0
    for line in readfile.readlines():
        line_new=line.strip()
        num_line=line_new.count('bcbx')
        num_bcbx += num_line
print(num_bcbx)


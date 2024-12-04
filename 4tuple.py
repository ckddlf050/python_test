# t1 = (10, 20, 30)
# print(type(t1))
# print(t1)
# print(t1[0])
# #del t1[0] 안됨
# #t1[0] =3 안됨

# t2 = (10)
# t3 = (10,)
# t4 = 10,   #,만 들어가도 튜플
# print(type(t4))

# set1 = {1,2,3}  
# print(set1)
# set2 = set([1,2,3,3]) #{1,2,3}
# print(set2)
# set2.add(4)
# print(set2)
# while len(set2)>0:
#     a = set2.pop()
#     print(a)

# l1 = [1,2,3,4]
# while len(l1)>0:
#     a = l1.pop()
#     print(a)

# set3= set("apple")
# print(set3)
# while len(set3)>0:
#     a = set3.pop()
#     print(a)

#count로 중복찾기
# name = ["1","2","3","2"]
# a=[]
# for i in range(len(name)):
#     if name.count(name[i]) > 1:
#         #print(name[i])
#         name.remove(name[i])
#         a.append(name[i])

# name_set = set(name)
# print(name_set)
# name_set =list(name_set)
# name_set.sort()
# print(name_set)

# name = ["1","2","3","2"]
# a=[]
# for i in name:
#     if i not in a:
#         #print(name[i])
#         # name.remove(name[i])
#         a.append(i)
# print(a)

# a = {}
# print(type(a)) #dictionary
# b = {1}
# print(type(b)) # set
# c = dict()
# c = {1:'a','b':'b'}
# print(c)
# c[2]='c'
# c['c'] =2
# print(c)
# # del c[2]
# # del c['b']
# print(c)
# print(c.get(2)) #none
# # print(c[2]) #keyeroor
# print(c.keys())
# print(c.values())

# # for i in c.keys():
# #     print(i,c.get(i))
# print('b' in c) #key가 딕셔너리 안에 있는지
# print(2 in c.values()) #값이 딕셔너리 안에 있는지


# dic = {
#     "비트": "0이나 1의 값을 가지는 컴퓨터 데이터의 최소 단위",
#     "변수": "어떤 1개의 자료를 저장하기 위한 메모리 할당 공간",
#     "리스트": "여러 개의 연속적인 자료를 저장하는 자료구조"
# }


# print("★ 컴퓨터 사전 ★")
# word = input("검색할 단어를 입력하세요: ")
# if word in dic:
#     print(f'{word}: {dic[word]}')
# else:
#     print("정의된 단어가 없습니다.")



# s = set()
# count = 0
# n, m = map(int, input().split())

# for _ in range(n):
#     data = input().rstrip()
#     s.add(data) 

# for _ in range(m):
#     data = input().rstrip()
#     if data in s:
#         count+=1

# print(count)

# n, m = map(int, input().split())
# s = set() 
# c = 0

# for i in range(n):
#     s.add(input())
    
# for i in range(m):
#     test = input()
#     if test in s:
#         c +=1 
# print(c)

# a={"Alice":85,"Bob":90,"charlie":95}
# print(a)
# a["David"] = 80
# print(a)
# a["Alice"]=88
# del(a["Bob"])
# print(a)

# for i in a.keys():
#     print(i,a.get(i))

d=[
    [10,20],
    [30,40,],
    [50,60]
]
print(d)
print(d[0][0])
print(d[1][1])
d.append([70,80])
print(d)
d[0][0] = 90
print(d)
# d[1].pop(0) #주의
print(d)
print(len(d))

for i in range(0,len(d)):
    for j in range(0,len(d[i])):
        print(d[i][j],end = " ")
    print()

for x,y in d:
    print(x,y)

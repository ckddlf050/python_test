# def f(x):
#     result = x**2+2*x+1
#     return result;

# print(f(3))

# def sayhi():
#     print("Hi")
#     print("Hi")
#     print("Hi")
# sayhi()

# def gugu(dan):
#     for i in range(1,10):
#         print(dan,"x",i,"=",(dan*i))
# gugu(5)

#-------------------------------
# x = 10

# def func2():
#     print("func2", x)   #지역변수

# def func():
#     x = 20
#     y= 11
#     print("func",x,y) #지역변수
#     func2()

# func()
# print("main", x)    #전역변수

# func2()

# def func3(x):   #지역변수
#     print("func3",x)
# func3(3)
#--------------

# def func(x,y):
#     if x==y:
#         print(f"결과(곱): {x*y}")
#     else:
#         print(f"결과(합):{x+y}")
# func(2,2)
# func(2,3)

# def a(x,y):
#     if x*y <20000:
#         print(f"가격: {x*y+2500}원 ")
#     else:
#         print(f"가격: {x*y}원 ")

# a(30000,1)
# a(15000,1)

# def times(a):
#     a2 = [i*2 for i in a]
#     return a2
# v = [1,2,3,4,5]
# v2 = times(v)
# print(v2)

# def sum_mul(a,b):
#     sum = a+b
#     mul = a*b
#     return sum,mul
# s,m = sum_mul(2,3)
# print(s,m)

#----함수화----------

# vending_machine = ["게토레이", "게토레이", "레쓰비", "레쓰비", "생수", "생수", "생수", "이프로"]

# def check_machine():
#     print("남은 음료수: ", vending_machine)

# def is_drink(drink):
#     return drink in vending_machine

# def add_drink(drink):
#     vending_machine.append(drink)
#     vending_machine.sort()
#     print("음료가 추가되었습니다.")
#     check_machine()

# def remove_drink(drink):
#     if is_drink(drink):
#         vending_machine.remove(drink)
#         print(f"{drink}이(가) 제거되었습니다.")
#         check_machine()
#     else:
#         print(f"{drink}은(는) 존재하지 않습니다.")

# user = int(input("사용자의 종류를 입력하세요: \n 1.소비자 \n 2.주인 \n"))

# if user == 1:  
#     drink = input("마시고 싶은 음료? ")
#     if is_drink(drink):
#         print(f"{drink} 드릴게요")
#         remove_drink(drink)
#     else:
#         print("해당 음료가 없습니다.")

# elif user == 2:  
#     work = int(input("할 일 선택: \n 1.추가 \n 2.삭제 \n"))
#     if work == 1:
#         add = input("추가할 음료수: ")
#         add_drink(add)
#     elif work == 2:
#         check_machine()
#         delc = input("삭제할 음료수? ")
#         remove_drink(delc)
#     else:
#         print("잘못된 입력입니다.")
# else:
#     print("다시 입력하세요.")


# import sys

# line = int(sys.stdin.readline().strip())
# stk = []

# def push(p):
#     stk.append(p)
# def pop():
#     if len(stk) != 0:
#         print(stk.pop())
#     else:
#         print(-1)
# def size():
#     print(len(stk))
# def empty():
#     if len(stk) == 0:
#         print(1)
#     else:
#         print(0)
# def top():
#     if len(stk) != 0:
#         print(stk[-1])
#     else:
#         print(-1)

# for _ in range(line):
#     command = sys.stdin.readline().strip().split()
#     if command[0] == "push":
#         push(command[1])
#     elif command[0] == "pop":
#         pop()
#     elif command[0] == "size":
#         size()
#     elif command[0] == "empty":
#         empty()
#     elif command[0] == "top":
#         top()

# ---복


# import sys

# line = int(sys.stdin.readline().strip())
# stk = []

# def push(p):
#     stk.append(p)

# def pop():
#     if len(stk) != 0:
#         print(stk.pop())
#     else:
#         print(-1)

# def size():
#     print(len(stk))

# def empty():
#     if len(stk) == 0:
#         print(1)
#     else:
#         print(0)

# def top():
#     if len(stk) != 0:
#         print(stk[-1])
#     else:
#         print(-1)

# for _ in range(line):
#     command = sys.stdin.readline().strip().split()
#     match command[0]:
#         case "push":
#             push(command[1])
#         case "pop":
#             pop()
#         case "size":
#             size()
#         case "empty":
#             empty()
#         case "top":
#             top()

# def oneUp():
#     global x
#     x +=1
#     return x
# x = 0
# print(oneUp())
# print(oneUp())
# print(oneUp())



# def get_times(n):
#     global count
#     for i in range(1,31):
#         if i % n ==0:
#             count +=1
#     return count
# count = 0
# n = 3
# get_times(n)
# print(f'\n{n}의 배수의 개수: {count}')

# def pr_str(txt,count=1,):    #디폴트값이 뒤에 있어야함 생략된값을 확실히 알기위해서 
#     for i in range(count):
#         print(txt)
# pr_str("Hello",3)
# # pr_str("Hello")

# def pr_str(txt, count=1, count2=1):
#     for i in range(count):
#         print(txt)
#         print(count2)

# pr_str("Hello", 3, 2)
# pr_str("Hello", 3)
# print()
# pr_str("Hello")
# print()
# pr_str() #txt='12'

# print(1,2,3,4)
# pr_str("234",count2=2)

# def calc_avg(*numbers):
#     print(type(numbers))
#     return sum(numbers)/len(numbers)
# print(calc_avg(1,2))
# print(calc_avg(1,2,3,4,5))

# ----------------------
# def b():    #함수안에 함수 가능
#     def c():
#         print("c")
#     c()
# b()
# -------------------------
# l = ["p","y","t","h","o","n"]
# print("".join(l))
#----------------------------

# def a():
#     return 1,2
# print(a())

# def introduce(**kwargs):
#     print(type(kwargs))
#     for key, value in kwargs.items():
#         print(f"{key}:{value}")
#     for i in kwargs:
#         print(f"{i}")

# introduce(name="Alice",age=25,city="New York")

# list = [2,4,1,5,6]
# list.sort()
# print("list",list)
# list2=[2,4,1,5,6]
# print("sorted list2",sorted(list2))
# print("list2",list2)

# #3번째로 작은 값의 인덱스를 구하라
# #정렬하거 그 값을 원본에서 찾으면됨
# print(sorted(list2)[2])

# print(eval("1+2*5"))
# print(int(4.6+0.5))
# print(round(4.5))
# print(round(125,-1))

# n=5
# factorial = 1

# for i in range(1,n+1):
# 	factorial *= i
# print(factorial)

# def factorial(n):
#     if n ==1:
#         return 1
#     return n * factorial(n-1)
# print(factorial(5))

# def hello():
#     global a
#     if a ==3:
#         return
#     print("Hello")
#     a +=1
#     hello()
# a=0
# hello()

# def factorial(n):
#     if n ==1:
#         return 1
#     return n * factorial(n-1)
# print(factorial(5))

# def fibo(n):
#     if n <= 2:
#         return 1
#     else:
#         return fibo(n-2)+fibo(n-1)
# for i in range(10):
#     print(fibo(i+1))

# memory = {1:1,2:1}

# def fibo_memoziation(n):
#     if n in memory:
#         number = memory[]
#     else:
#         number = fibo_memoziation(n-1)+fibo_memoziation(n-2)
#         memory[n] =number
#     return number




# memory = {1: 1, 2: 1} #1값 2값 저장

# def fibo_memoization(n):
#     if n in memory:
#         number = memory[n]
#     else:
#         number = fibo_memoization(n-1) + fibo_memoization(n-2)
#         memory[n] = number
#     return number

# print(fibo_memoization(50))
# print(fibo_memoization(100))

# def hanoi(number_of_disks_to_move, from_, to_, via_):
#     if number_of_disks_to_move == 1:
#         print(from_, "->", to_)
#     else:
#         hanoi(number_of_disks_to_move-1, from_, via_, to_)
#         print(from_, "->", to_)
#         hanoi(number_of_disks_to_move-1, via_, to_, from_)

# add = lambda x,y:x+y # 변수로 함수를 넣을수 있음
# print(type(add))
# print(add(1,2))

# def add2(x,y):
#     return x+y
# add3= add2
# print(add(1,2))
# print(add3(1,2))

# def call_3(func):
#     for i in range(3):
#         func()
# call_3(lambda:print("hi"))

# def download(startedCallback,enddeCallback):
#     startedCallback()
#     print("download 중")
#     enddeCallback()
# download(lambda:print("다운로드 시작"),lambda:print("완료되었습니다"))

# list(map(int,["1","2","3","4"]))

# result = map(lambda x:3*x,[1,2,3,4])
# print(list(result))
# li = [-5,1,2,-11,76]

# value = list(filter(lambda x:3*x>=3,li)) #map 과다르게 트루값만출력
# print(value)    #[-5,-11]

# value = list(filter(lambda x:x>0,li))
# print(value)    #[-5,-11]

li = [-5,1,2,-11,76]

value = list(filter(lambda x:x>=3,map(lambda x:2*x,li)))
print(value)    

# def solution(arr):
#     answer = []
#     for i in arr:
#         if i>=50 and i % 2 ==0:
#             answer.append(int(i/2))
#         elif i <50 and i % 2 ==1:
#             answer.append(int(i*2))
#         else:
#             answer.append(int(i))
            
#     return answer

# def solution(myString):
#     answer = []
#     a = myString.split("X")
#     for i in a:
#         answer.append(len(i))
    
#     return answer



# import calc_module

# print(calc_module.add(1,2))
# print(calc_module.sub(1,2))
# print(calc_module.mul(1,2))
# print(calc_module.div(1,2))


# from calc_module import add # 하나만 가져올때
# print(add(1,2)) 

# import calc_module as cm
# print(cm.add(2,3))

# import math

# print(math.floor(3.14))
# print(math.ceil(3.141))
# print(math.sqrt(4))

# from math import floor,ceil
# print(floor(3.14))
# print(ceil(3.141))
# import random

# print(random.randint(1,5))
# print(random.uniform(1,2))
# print(random.random())
# print(random.randrange(1,5)) #b값 포함 안됨
# print(random.randrange(1,5,2)) #b값 포함 안됨

# import random
# com = random.randint(1,100)

# min_v = 1
# max_v = 100
# count = 0
# score = 100

# while True:
#     try:
#         if count == 10:
#             print("횟수 초과")
#             break
#         count += 1
#         guess = int(input("[%d회] 숫자입력 (%d ~ %d):" % (count,min_v,max_v)))
#         if guess < 0 or guess > 100:
#             print("입력 범위를 초과했어요")
#             score -=10
#         elif com == guess:
#             print("정답이에요")
#             print(f"정답 :{com}\n 점수: {score}점")
#             break
#         elif com > guess:
#             print("랜덤수보다 작아요")
#             min_v = guess
#             score-=10
#         else:
#             print("랜덤수보다 커요")
#             max_v = guess
#             score-=10

#     except ValueError:
#         print("숫자만 입력 가능합니다.")

# import random
# list=[]
# num = random.randint(1,45)

# for i in range(6):
#     while num in list:
#         num = random.randint(1,45)
#     list.append(num)
# list.sort()
# print(list)

# lo =random.sample(range(1,46),6)
# print(sorted(lo))

import datetime

# now = datetime.datetime.today()
# print(now)
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)

# print(f"{now.year}년 {now.month}월 {now.day}일")
# print(f"{now.hour}시 {now.minute}분 {now.second}초")

# print("지금까지 몇 일?")
# first_day = datetime.date(2024,11,25)

# today = datetime.date.today()
# print(today)

# prassed_time = today - first_day
# print(prassed_time)
# print(f"개강{prassed_time.days}일 지났습니다")

# import datetime
# import calendar

# days=["월","화","수","목","금","토","일"]

# weekday = datetime.date.today().weekday()
# print(weekday)
# print("오늘은 "+days[weekday]+"요일")

# the_day = datetime.date(2024,12,25).weekday()
# print(the_day)
# print("크리스마스는 " +days[the_day]+"요일")

# def get_weekday(yyyy,mm,dd):
#     days=["월","화","수","목","금","토","일"]
#     weekday = datetime.date(yyyy,mm,dd).weekday()
#     print(f"{yyyy}년{mm}월{dd}일")

# get_weekday(2024,8,15)

# import time

# a = (time.time())
# time.sleep(2)
# b = (time.time())
# print(b-a)

# print(time.localtime())
# time_str = time.localtime()
# time_str = (time_str.tm_year)

# print(time.ctime())
# print(time.ctime(a))
# print(time.ctime(b))

# #1970년 1월1일 기준
# year=time.time()/(365*24*60*60)
# day = round(time.time()/(24*60*60))
# print(year)
# print(day)

# def cheak_time(func):
#     Start=time.time()
#     func()
#     end = time.time()
#     print("수행시간:"+ str(end-Start)+"초")

# def a():
#     for i in range(10):
#         print(i)
#         time.sleep(1)
# def b():
#     for i in range(10):
#         print(i)
#         time.sleep(0.5)
    
# cheak_time(a)
# cheak_time(b)

import sys

# args = sys.argv[1:]
# print(args)

# total = 0
# for i in args:
#     total += int(i)
# print(total)

# args = sys.argv[1:]

# total = 0
# if len(args) <=2 or len(args)>= 4:
#     print("오류")
#     sys.exit(0)
# if args[0] == "add":
#    print(int(args[1])+int(args[2]))
# elif args[0] == "mul":
#    print(int(args[1])*int(args[2]))

# import os
# os.chdir("C:/Users/ckddl/git-test/.git")
# dir = os.popen("dir")
# print(dir.read())
# print(os.listdir())

# import random
# import time

# word = ["sky","earth","moon","flower","tree","apple","green",
#         "garlic","onion","potato"]
# n =1

# input("[타자게임]준비되면 엔터!")
# start =time.time()
# while n < 11:
#     print("문제",n)
#     question = random.choice(word)
#     print(question)
#     user = input()
#     if question == user:
#         print("통과!!")
#         n+=1
#     else:
#         print("오타! 다시도전")

# end = time.time()
# et = end - start
# print(f"타자시간:{et: .2f}초")


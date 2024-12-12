# f = open("text.txt","w")
# f.write("Hello world!!!!\n")
# f.close()

# f2 =  open("text.txt")
# print(f2.read())
# f2.close()

# f4 =  open("text.txt")
# print(f4.readline(),end="")
# print(f4.readline(),end="")
# print(f4.readline(),end="")
# f4.close()

# f3 = open("text.txt","a")
# f3.write("Hello world22\n")
# f3.close()

# f5 =  open("text.txt")
# print(f5.readlines())
# f5.close()

# f6 = open("text.txt","r+")
# str6=f6.read()
# print(f6.read())
# print(f6.tell())
# f6.seek(str6.find("5"))  # 특정위치로 이동
# f6.write("8")   
# f6.close()

# with open("text.txt","r+") as f7:
#     str6=f7.read()
#     print(f7.read())
#     print(f7.tell())
#     f7.seek(str6.find("5"))  # 특정위치로 이동
#     print(f7.write("8"))   

# import random

# with open("word.txt","w") as f:
#     word=["sky","earth","moon","flower","tree","apple","green",
#          "garlic","onion","potato"]
#     for i in word:
#         f.write(i+'\n') #\n ,\t,\r

# with open("word.txt","r") as f:
#     data = f.read().split()
#     word = random.choice(data)
#     print(word)

# import random
# import time

# with open("word.txt","r") as f:
#     word = f.read().split()

# n=1

# input("[타자게임]준비되면 엔터!")
# start =time.time()

# while n < 11:
#     print("문제",n)
#     question = random.choice(word)
#     print(question)
#     user = input()
#     if question == user:
#         print("통과!!")
#         n +=1
#     else:
#         print("오타! 다시도전")

#     end = time.time()
#     print(f"게임 소요 시간 : {end -start:.2f}초")
# print("게임을 종료합니다")

# try:
#     with open("./output/input.txt","a") as f:
#         while True:
#             text = input("저장할 내용 입력(종료-z) :")
#             if text == "z" or text =="Z":
#                 break
#             f.write(text)
#             f.write("\n")
# except:
#     print("파일을 찾을 수 없습니다")



# with open("./output/input.txt", 'a') as f:
#     while True:
#         text = input("저장할 내용 입력(종료-z)")
#         if text == 'z' or text == 'Z':
#             break
#         f.write(text + '\n')
    

# with open("./output/member.txt", 'a') as f:
#     for i in range(3):
#         name = input("이름:")
#         ps = input("비밀번호:")
#         f.write(f"{name} {ps} \n")
# with open("./output/member.txt","r") as f:
#     print(f.read())

# with open("./output/member.txt", 'r') as f:
#     name = input("이름을 입력하세요:")
#     pw = input("비밀번호를 입력하세요:")
#     for i in f:
#         n, p = i.strip().split()

#         if n == name and p == pw:
#             print("로그인성공")
#             break
#         else:
#             print("실패")
#             break

dic ={}

with open("./output/member.txt", 'r') as f:
    for i in f:
        n,p = i.split()
        dic[n] = p

name = input("이름을 입력하세요: ")
pw = input("비밀번호를 입력하세요: ")

if pw == dic.get(name):
    print("로그인 성공")
    tel = input("전화번호를 입력하세요")
    with open("./output/member_tel.txt", 'a') as f1:
        f1.write(f"{name} {pw} {tel} \n")
else:
    print("로그인 실패")


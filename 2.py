# a = []
# b = [1,2,3,4]
# c = ["장원영","안유진"]
# d = [1,"아이브"]

# print(len(c))
# print(c[0])
# print(c[1])
# c[0]="카리나"
# print(c)

# del c[1]
# print(c)
# c.append("원터")
# print(c)

# print(b[-1])

# seasons = ["봄","여름","가을","겨울"]

# print(seasons[0:1])  
# print(seasons[0:2])
# print(seasons[:3])
# print(seasons[1:])
# print(seasons[1:3])
# print(seasons[1::2])
# print(seasons[::-1])

# seasons2 = ["봄","여름","가을","겨울",[1,2,3,4]]
# print(seasons2[-1][0])
# print(seasons2[4])


# a=[1,2,3,4,5,6,7,8,9,10]
# even = (a[1::2])
# print(even)

# even = (a[0::2])
# print(even)

# a = [3,1,5,2]
# a.sort()  #a.sort(reverse = true)
# a.reverse()
# print(a)

# b.sort
# print(b)

# c = ["1","10","2"]
# c.sort
# print(c)  #['1', '10', '2'] 문자형이기때문b

# a = ["a","b","c","d"]
# a.insert(1,"f")
# print(a)

# d = ["강남", "강북", "서", "asdfd", "서", "서"]

# first = d.index("서")+1
# print(first + d[first:].index("서"))

# print(d.count("서"))

#실습1
# rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']

# print(rainbow[2:3])
# rainbow.sort()
# print(rainbow)
# rainbow.append("black")
# print(rainbow)
# del rainbow[3:7]
# print(rainbow)

# print(rainbow.index("green"))
# rainbow.pop(1)
# print(rainbow)
# print(rainbow.count("black"))

# print("오늘은 12월 %d일 입니다." % 2)
# print("오늘은 %d월 %d일 입니다." % (12,3))
# print(f"오늘은 {12}{'월'} {2}일 입니다.")
# print("오늘은" +str(12)+"월"+ str(2)+"일 입니다.")
# print("오늘은 ",12,"월 ",2,"일 입니다.",sep="")
#->모두 같은 결과값

# print("Hello".upper())
# print("HELLO".lower())

# friends = "고찬국 김다운 김민창"
# a = friends.split() # ★중요
# print(a)

# email = "ckddldf050@naver.com"
# a = email.split("@")
# print(a)

# sentence = "{}월 {}일".format(12,2)
# print(sentence)

# sentence = "{1}월 {0}일".format(12,2)
# print(sentence)

# b = "    111  2222 "
# print(b.strip())
# print(b.split())

#실습
# a = int(input("첫번째 세자리: "))
# b = input("두번째 세자리: ")

# num1 = int(b[2:])  
# num2 = int(b[1:2])  
# num3 = int(b[:1])  

# print(a * num1)
# print(a * num2)
# print(a * num3)
# print(a * int(b))

# print(1==2)

# x=2
# print(1<x<3)

# a = ["계란","마늘","콩나물","커피"]
# print("두부" in a)
# print("커피" in a)

# if 1<3:
#     print("True")
#     print("True")
# print("False")

#실습3
# num = int(input("숫자: "))
# if num % 2 == 0:
#     print("짝수")
# if num % 2 == 1:
#     print("홀수")

# num = int(input("숫자: "))
# if num % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")

# num = int(input("점수"))

# if 89 < num <=100:
#     print("A")
# elif num <90:
#     print("B")
# elif num <80:
#     print("C")
# elif num <70:
#     print("D")
# elif num <60:
#     print("E")
# else:
#     print("다시 입력하세요")

# a = int(input("나이를 숫자로 입력해주세요: "))
# b = (input("결제 방법을 입력해주세요.('카드' 또는 '현금만 입력) :"))

# if a < 8:
#     print(f"{a}세의 {b} 요금은 무료입니다.")
# elif a < 14:
#     print(f"{a}세의 {b} 요금은 450원 입니다")
# elif a < 20:
#    if b == "카드":
#     print(f"{a}세의 {b} 요금은 720원 입니다")
#    else:
#     print(f"{a}세의 {b} 요금은 1000원 입니다")
# elif a < 75:
#    if b == "카드":
#     print(f"{a}세의 {b} 요금은 1200원 입니다")
#    else:
#     print(f"{a}세의 {b} 요금은 1300원 입니다")
# else:
#     print(f"{a}세의 {b} 요금은 무료입니다.")

# 실습
# a = int(input("나이를 숫자로 입력해주세요: "))
# b = (input("결제 방법을 입력해주세요.('카드' 또는 '현금만 입력) :"))

# if a <8 or a >= 75:
#    c = "무료"
# elif a < 14:
#     c = 450
# elif a <20:
#     if b == "카드":
#         c = "720원"
#     elif b == "현금":
#         c = "1000원"
# elif a <75:
#     if b == "카드":
#         c = "1200원"
#     elif b == "현금":
#         c = "1300원"

# print(f"{a}세의 {b}요금은 {c} 입니다")
   

# num = int(input("정수를 입력하세요: "))

# 실습1)
# vending_machine = ["게토레이","레쓰비","생수","이프로"]

# drink = input("마시고 싶은 음료? ")
# if name in vending_machine:
#     print(f"{drink} 드릴게요")

#실습응용
# vending_machine = ["게토레이","게토레이","레쓰비","레쓰비","생수","생수","생수","이프로"]
# user = int(input("사용자의 종류를 입력하세요: \n 1.소비자 \n 2.주인 \n" ))

# if user == 1:
#     drink = input("마시고 싶은 음료? ")
#     if drink in vending_machine:
#         print(f"{drink} 드릴게요")
#         vending_machine.remove(drink)
#         print("남은 음료수: ", vending_machine)
#     else:
#         print("없음")

# elif user == 2:
#     work = int(input("할 일 선택: \n 1.추가 \n 2.삭제 \n" ))
#     if work == 1:
#         add = input("추가할 음료수: ")
#         vending_machine.append(add)
#         vending_machine.sort()
#         print("추가완료")
#         print(f"남은 음료수",vending_machine)
#     elif work == 2:        
#         print(f"남은 음료수",vending_machine)
#         delc = input("삭제할 음료수? ")
#         if delc in vending_machine:
#             vending_machine.remove(delc)
#             print(f"삭제완료 \n 남은 음료수",vending_machine)
#         else:
#             print("없음")
# else:
#     print("다시 입력하세요")
        
# 


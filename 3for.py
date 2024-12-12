# i = 0
# while i <5:
#     i +=1
#     print(i)
# print("끝")

#홀수만출력
# num = 0
# while num <10:
#     num = num +1
#     if num % 2 == 0:
#         continue
#     print(num)

# num = int(input("어디까지 계산할까요?"))

# a = 0
# b = 0
# for i in range(1,num+1):  
#     a +=i
#     if i % 2 ==1:
#         b += i
        
# print(a)
# print(b)

#입력한 숫자만큼 카운트하고 발사 출력
# num = int(input("몇초?"))
# for i in range(num,0,-1):
#     print(i,end = " ")
# print("발사")

#구구단 만들기
# num = int(input("먗단을 출력할까요? "))
# for i in range(1,10):
#     print(f"{num} * {i} = {num * i}")

# a = [10,20,30]
# print(sum(a))
# for i in a:
#     sum += i
# print(sum)

# a = [1,2,3,4,5]
# a2 = []
# a3 = []
# a4 = []

# a3 =[i*3 for i in a]
# print(a3)

# a4 = [i*3 for i in a if i%2==0]
# print(a4)

# for y in range(3):
#     for x in range(2):
#         print(f"y: {y}, x:{x}")
#     print()

# for i in range(2,10):
#     print(f"[{i} 단]")
#     for j in range(1,10):
#         print(f"{i} x {j} = {i*j}")
#     print()

#자리 배치도 고객수와 행으로 바꾸기


# print('*** 자리배치도 ***')
# customer = int(input('고객수 입력: '))
# row = int(input('좌석행 수 입력: '))

# if customer % row == 0:
#     column = customer // row
# else:
#     column = (customer // row) + 1
# # print(row)

# for i in range(0, row):
#   for j in range(1, column + 1):
#     seat = i * column + j
#     if seat > customer:
#       break
#     print(seat, end=" ")
#   print()

# num = int(input("몇 줄?"))
# for i in range(1,num+1):
#     print(i*'*')


# for i in range(1, num + 1):
#     print(f"{'*' * i:>{num}}")


# for i in range(1,num+1):
#     print(("*" * (2 * i - 1)).center(2 * num - 1))

n = list(map(int,input("숫자 여러개 입력 ").split()))
print(n)
print("가장 큰 값:" ,  max(n))
print("가장 작은 값: " , min(n))
n.remove(max(n))
n.remove(min(n))
print("나머지 값의 평균: ",sum(n)/len(n) )


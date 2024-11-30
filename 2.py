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
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']

print(rainbow[2:3])
rainbow.sort()
print(rainbow)
rainbow.append("black")
print(rainbow)
del rainbow[3:7]
print(rainbow)

print(rainbow.index("green"))
rainbow.pop(1)
print(rainbow)
print(rainbow.count("black"))


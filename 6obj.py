# a= dict()
# a=set()

# class b: #클래스
#     pass
# c= b() #객체

# class Movie:
#     title = "소방관"

# Movie1=Movie()
# Movie2=Movie()

# print(Movie1.title)
# print(Movie2.title)

# Movie1.title ="파묘"
# print(Movie1.title)
# print(Movie2.title)

# Movie1.score = "1"
# print(Movie1.score)


# class Movie:
#     name = ''
#     def print_msg(msg):
#         print(msg)
#     def modify(self,Movie):
#         self.name = Movie
#     def print_name(self):
#         print(self.name)

# Movie1 = Movie()
# Movie2 = Movie()

# Movie.print_msg('print 하기')
# Movie1.modify('프린트하기3')
# Movie2.modify('프린트하기4')

# print(Movie1.name,Movie2.name)

# class Movie:
#     def __init__(self):
#         print("Hello")
# movie = Movie()

# class Movie:
#     count=0
#     def __init__(self,title,audience):
#         self.title = title
#         self.audience =audience
# movie1 = Movie("파묘",100)
# movie2 = Movie("파묘2",200)

# print(movie1.title,movie1.audience)
# print(movie2.title,movie2.audience)

# class Movie:
#     count=0
#     def __init__(self,title,audience):
#         self.title = title
#         self.audience =audience
#         Movie.count +=1

# movie1 = Movie("파묘",100)
# movie2 = Movie("파묘2",200)

# print(movie1.count)
# print(movie2.count)
# print(Movie.count)

# class Movie:
#     count=0
#     def __init__(self,title,audience): #init=초기화
#         self.__title = title
#         self._audience =audience
#         Movie.count +=1

#     def get_title(self):
#         return self.__title

#     def set_title(self,title):
#         self.__title=title
    
#     def get_audience(self):
#         return self._audience

# movie1 = Movie("파묘",100)
# print(movie1.get_title())
# movie1.__title = "오겜"
# print(movie1.get_title())
# print(movie1.__title)
# print(movie1._audience)
# print(movie1.get_audience())

# class MyAdd:
#     __a = 1
#     __b = 2
    
#     def sum(self):
#         return self.__a+self.__b

#     def set_a(self,a):
#         self.__a =a
#     #######메소드 구현

# a = MyAdd()
# print(a.sum()) # 3
# a.set_a(3)
# # __a 값 3으로 변경 
# print(a.sum()) # 5

# class Health:
#     def __init__(self,name):
#         self.__name = name
#         self.__hp = 100
    
#     def get_name(self):
#         return self.__name
    
#     def set_hp(self,hp):
#         if hp <0:
#             hp = 0
#         if hp > 100:
#             hp = 100
#         self.__hp = hp

#     def get_hp(self):
#         return"hp: " +str(self.__hp)
    
#     def exercise(self,hours):
#         self.set_hp(self.__hp + hours)
#         print("{}시간 운동하다".format(hours))

#     def drink(self,cups):
#         self.set_hp(self.__hp - cups)
#         print("술을{}잔 마시다".format(cups))

# p1 = Health("나몸짱")
# p1.set_hp(100)
# p1.exercise(5)
# p1.drink(2)
# print(f'{p1.get_name()}-{p1.get_hp()}')

# p2 = Health("나약해")
# p2.set_hp(10)
# p1.exercise(1)
# p2.drink(12)
# print(f"{p2.get_name()}-{p2.get_hp()}")

# class Num:
#     def __init__(self,num1,num2):
#         self.__num1 =num1
#         self.__num2 = num2
    
#     def add(self):
#         return self.__num1 + self.__num2
    
#     def sub(self):
#         return self.__num1 - self.__num2
    
#     def mul(self):
#         return self.__num1 * self.__num2

#     def div(self):
#         if self.__num2 ==0:
#             print("불가")
            
#         else:
#             return self.__num1 / self.__num2
        
# a = Num(5,3)
# print(a.add())
# print(a.sub())
# print(a.mul())
# print(a.div())

# class Employee:
#     serial_num = 1000

#     def __init__(self,name):
#         Employee.serial_num +=1
#         self.id = Employee.serial_num
#         self.name = name
    
#     def __str__(self):
#         return "사번 : {}, 이름 : {}".format(self.id,self.name)
    

# e1 = Employee("최사원")
# print(e1)

# e2 = Employee("안사원")
# print(e2)

# e3 = Employee("한사원")
# print(e3)


# employee = [
#     Employee('구름'),
#     Employee('별'),
#     Employee('행성'),
#     Employee('달')
# ]
# for i in employee:
#     print(i)
# print("\n".join(map(str, employee)))

# class Supermarket:
#     count = 0

#     def __init__(self,location,name,product,customer):
#         self.__location = location
#         self.__name = name
#         self.__product = product
#         self.__customer = customer
#         Supermarket.count +=1
    
#     def print_location(self):
#         print(self.__location)
    
#     def change_category(self,product1):
#         self.__product = product1
        
#     def show_list(self):
#         print(self.__product)
    
#     def enter_customer(self):
#         self.__customer += 1

#     def show_info(self):
#         print("가게이름:{} 위치:{} 파는물건:{},손님수{}".format(self.__name,self.__location,self.__product,self.__customer))

#     def show_supermarket_count():
#         print(f"인스턴스 개수:{Supermarket.count}")

# x=Supermarket("강남","코다차야","김볶밥",3)
# x.print_location()
# x.change_category("홍합탕")
# x.show_list()
# x.enter_customer()
# x.show_info()
# Supermarket.show_supermarket_count()

# class Country:
#     def __init__(self):
#         self.name = "나라이름"
#         self.population = "인구"
#         self.capital = "수도"
    
#     def show(self):
#         print("국가 클래스의 메소드입니다")

# class korea(Country):
#     def __init__(self,name):
#         self.name = name
    
#     def show(self):
#         print("국가 이름은:", self.name)

# country = korea("대한민국")
# country.show()
# print(country.name)
# country.show()

# class Calculator():
#     def __init__(self):
#         self.value = 100
    
#     def sub(self,value):
#         self.value -= value
    
# class MinLimitCalculator(Calculator):
#     def sub(self,value):
#         self.value -= value
#         self.value = max(0,self.value-value)
        

# cal =MinLimitCalculator()
# cal.sub(20)
# cal.sub(90)
# print(cal.value)

# class Calculator():
#     def __init__(self):
#         self.value = 100

#     def sub(self,value):
#         self.value -= value 
    
#     #파이썬은 메소드 오버로드 안됨
#     def sub(self):
#         self.value -=10
#     #파이썬은 메소드 오버로드 안됨
#     def sub(self,value1,value2):
#         self.value = value1 -value2
    
#     def sub(self,*argss):
#         self.value = argss[0]


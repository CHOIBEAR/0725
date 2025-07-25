#-------------------------1교시-------------------------------
# 함수의 형태.

# def 함수명():
#   #실행용 명령어 삽입.
#   print("함수명 함수 실행")
#   return #or pass

# 함수명()#함수 호출 

# #함수 가지고 놀기

# def a (b):
#   if b:
#     print("1",b)
#       del b[0]
#       a(b)

# #a(0)
# a([1,2,3,4,5])
# # ㄴ 재귀 함수.

# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)

# # 예시 실행
# print(factorial(5))  # 출력: 120

# def print_numbers(n):
#     if n == 0:
#         return
#     print_numbers(n - 1)
#     print(n)

# print_numbers(5)
# # 출력: 1 2 3 4 5

# def a ():
#   pass

# class A():
#   pass

# print(type(a))
# print(type(A))

#------------2교시--------------------

# def a():
#   pass

# class T():
#   def a(s,v):
#     pass

  
# t=T()
# t.a(1)

#class 안에 있는 첫번째 자리 함수는 무조건 변수를 담아줘야한다. 암묵적으로 self ,s 를 넣는다.
#class 내부에 있는 함수는 , 로 구분하고 2번째 자리에 있는 변수의 값은 
#class 를 호출하는 함수안에 매개변수를 입력해주어야 한다. 


# class Person:
#     def __init__(self, name):  # 생성자 메서드
#         self.name = name

#     def say_hello(self):       # 일반 메서드
#         print(f"안녕하세요, 저는 {self.name}입니다.")

# # 객체 생성
# p = Person("불곰")

# # 메서드 호출
# p.say_hello()

# v1=10 #전역변수 << 파일 내부에 생성된 파일 (전역)에 영향을 끼치는 (변수).
# #지역 변수는 함수 내부에서 만들어 만들어진 함수에서만 사용 가능하다. 
# # 다른 곳에서 사용하려면 return을 주어야한다.
# def a(v):
#   v2 = 100 # 지역변수.
#   print(v1,v2)
#   return v2

# class T():
#   def a(s,v):
#     print (v1,v)
#     pass

  
# t=T()

# vvvv=a(1)
# t.a(vvvv)

# 전역변수
# total_score = 0

# class Student:
#     def __init__(self, name, score):  # 매개변수 name, score
#         self.name = name              # 인스턴스 변수
#         self.score = score            # 인스턴스 변수

#     def add_to_total(self):
#         global total_score            # 전역변수 사용
#         bonus = 5                     # 지역변수
#         total = self.score + bonus    # 지역변수
#         total_score += total
#         print(f"{self.name}의 점수({self.score}) + 보너스({bonus}) = {total}")

# # 객체 생성 및 메서드 호출
# s1 = Student("불곰", 50)
# s2 = Student("라이카", 10)

# s1.add_to_total()
# s2.add_to_total()

# print("총합 점수:", total_score)

# class T():
#   def __init__(s,no):# 생성자는 기본 생성자가 필요하다. 
#                      # 그래서 def __init__ (self): 함수를 넣어준다.
#     s.no = no            # 생성자는 무조건 1개만.
#   def a(s):
#     print(s.no)

  
# t=T(1) #클래스 생성하는 인스턴스 호출 만들기.
#       #생성자.
#       #생성자는 값을 전달하는것이 가능.
      
# t.a()

#--------------------------------------3교시----------------------------------------

# class T():
#   def __init__(s,no):# 생성자는 기본 생성자가 필요하다. 
#                      # 그래서 def __init__ (self): 함수를 넣어준다.
#     s.__no = no      # 이 형태를 부를땐 _T__no
#     #s._no = no      # 이건 _no
#     # s.no = no      # 이건.no 
#                      # 생성자는 무조건 1개만.
#   @property        # setter 함수
#   def no(s):       # 클래스. 변수명.
#     return s.__no
    
#   def a(s):        #함수.
#     pass
  
# t=T(1) #클래스 생성하는 인스턴스 호출 만들기.
#       #생성자.
#       #생성자는 값을 전달하는것이 가능.
      
# #t.a()
# # t.no = 100
# print(t.no) #파이썬은 앵간한 권한은 다 있다. 접근권한이라던가 변수명을 바꾸는등.

# class T():
#   def __init__(s, no): # 생성자
#     s.__no = no        # _T__no
#     # s._no = no       # _no
#     # s.no = no        # no
#   @property            # setter 함수
#   def no(s):           # 클래스.변수명
#     return s.__no
  
#   def a(s):            # 함수
#     pass

# t = T(1)               # 클래스를 생성하는 인스턴스 만들기 
# # t.a()                # 클래스 안에 있는 함수 호출
# # t.no = 50
# print(t.no)

class T():
  def __init__(s):     # 생성자
    s.__no = 0         # 클래스에서 사용되는 변수. 0은 초기값.
  @property            # setter 함수 필요,인스턴스를 이용해서 변수를 사용 하기위한 함수 생성.
  def no(s):           # 사용 예시 : 클래스.변수명
    return s.__no         
  def setNo(s, no):    # 인스턴스로 변수의 값을 변경할때 사용하는 함수.:setter
    s.__no = no  

t = T()     
print ("전",t.no)
t.setNo(10)
print ("후",t.no)

# class T():
#     def __init__(s): # 생성자
#         s.__no = 0   # 클래스에서 사용되는 변수 '__no'
#     @property        # 인스턴스로 변수를 호출 하기 위한 설정
#     def no(s):
#         return s.__no
#     def setNo(s, no): # 인스턴스로 변수의 값을 변경 할때 사용 하는 함수 : setter
#         s.__no = no
        
# t = T()
# print("전", t.no)
# # t.no = 200 # 사용 불가
# t.setNo(10)  # setter를 이용하여 변수 값 변경 하는 부분
# print("후", t.no)

#--------------------------------스터디 요약 -------------------------------

# 📚 오늘의 파이썬 학습 요약

# 🕐 1교시 – 함수와 재귀 함수

# # 함수 정의
# def 함수명():
#     print("실행")
#     return

# 함수명()

# # 재귀 함수 예시
# def a(b):
#     if b:
#         print("1", b)
#         del b[0]
#         a(b)

# a([1, 2, 3, 4, 5])

# # 팩토리얼 함수
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(5))  # 출력: 120

# # 1부터 n까지 출력하는 재귀 함수
# def print_numbers(n):
#     if n == 0:
#         return
#     print_numbers(n - 1)
#     print(n)

# print_numbers(5)  # 출력: 1 2 3 4 5

# # 함수 vs 클래스 타입
# def a(): pass
# class A: pass

# print(type(a))  # <class 'function'>
# print(type(A))  # <class 'type'>


# 🕑 2교시 – 클래스, 생성자, 메서드

# # 클래스 내 함수 사용
# class T:
#     def a(self, v):
#         pass

# t = T()
# t.a(1)

# # 생성자 사용 예시
# class Person:
#     def __init__(self, name):
#         self.name = name
#     def say_hello(self):
#         print(f"안녕하세요, 저는 {self.name}입니다.")

# p = Person("불곰")
# p.say_hello()

# # 전역변수 / 지역변수
# v1 = 10  # 전역변수
# def a(v):
#     v2 = 100  # 지역변수
#     print(v1, v2)
#     return v2

# class T:
#     def a(s, v):
#         print(v1, v)

# t = T()
# vvvv = a(1)
# t.a(vvvv)

# # 전역변수 활용 클래스
# total_score = 0

# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def add_to_total(self):
#         global total_score
#         bonus = 5
#         total = self.score + bonus
#         total_score += total
#         print(f"{self.name}의 점수({self.score}) + 보너스({bonus}) = {total}")

# s1 = Student("불곰", 50)
# s2 = Student("라이카", 10)
# s1.add_to_total()
# s2.add_to_total()
# print("총합 점수:", total_score)


# 🕒 3교시 – 접근 제한자, getter/setter

# private 변수 접근 (getter만 사용)
# class T:
#     def __init__(s, no):
#         s.__no = no

#     @property
#     def no(s):
#         return s.__no

# t = T(1)
# print(t.no)

# # setter 함수 포함된 클래스 예시
# class T:
#     def __init__(s):
#         s.__no = 0  # 초기값 0

#     @property
#     def no(s):
#         return s.__no

#     def setNo(s, no):
#         s.__no = no

# t = T()
# print("전", t.no)
# t.setNo(10)
# print("후", t.no)
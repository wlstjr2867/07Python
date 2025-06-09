'''
함수
  형식] def 함수명(매개변수1, 매개변수2):
            실행부
            return 결과1, 결과2\
  목적에 따라 return문은 생략 가능함
'''
print(f"{'함수정의 및 호출':-^30}")
#매개변수와 반환값 없이 수열의 결과를 출력하는 함수
def sumTen():
  sum = 0
  for i in range(1,11):
    sum += i
  print('1~10까지의합:', sum)
#함수호출
sumTen()

print(f"{'함수정의 및 응용':-^30}")
#메뉴출력 및 입력값을 반환하는 함수
def menu():
  print('메뉴중 숫자를 선택하세요')
  print('1. 덧셈 2.뺄셈 3.곱셈 4.나눗셈' )
  print('5.종료')
  return input('번호선택:')

#사칙 연산을 위한 함수(매개변수o, 반환값 x)
def add(a, b):
  print(a, "+", b, '=', a+b)
def sub(a, b):
  print(a, "-", b, '=', a-b)
def mul(a, b):
  print(a, "*", b, '=', a*b)  
def div(a, b):
  print(a, "/", b, '=', a/b)
  
chocie = 0
#사용자가 종료할때까지 무한 반복해서 함수 호출
while True:
  # 반환값을 정수로 변환 후 변수에 저장
  choice = int(menu())
  #사칙연산 수행 및 반복문 탈출
  if choice == 1:
    add(int(input("덧셈 a=")), int(input("b=")))
  elif choice == 2:
    sub(int(input("뺄셈 a=")), int(input("b=")))
  elif choice == 3:
    mul(int(input("곱셈 a=")), int(input("b=")))
  elif choice == 4:
    div(int(input("나눗셈 a=")), int(input("b=")))
  elif choice == 5:
    break
print("연산 종료!!!")
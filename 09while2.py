'''
시나리오] 1부터 20까지의 숫자중 홀수만 출력하는 프로그램을
작성하시오 단 continue를 사용하시오
'''
a = 1
while a <= 20:
  if a % 2 == 0:
    a = a + 1
    continue
  else:
    print(a, end=' ')
    a += 1
    
print()
print("="*30)

# 시나리오] 구구단을 출력하시오
dan = 2
while dan <= 9 :
  su = 1
  while su<=9:
    print("%d*%d=%2d" % (dan, su, su*dan), end=' ')
    su += 1
  dan += 1
  print()
  
print()
print("="*30)

#시나리오] 구구단을 출력하되 짝수단만 출력하시오
dan = 2
while dan<=9 :
  if dan%2 == 1: # 단이 홀수이면 while문의 처음으로 돌아감
    dan += 1
    continue
  else: #단이 짝수일때만 구구단 출력
    su = 1
    while su<=9:
      print("%d*%d=%2d" % (dan, su, su*dan), end=' ')
      su += 1
  dan += 1
  print()
print()
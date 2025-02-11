import math

N = int(input("ค่า N : ") )

if N == 0:
  print("N! = 1") #ถ้า N = 0 ผลลัพธ์ = 1
else:
  print("N! =",math.factorial(N)) #แสดง + ผลลัพธ์ของ !

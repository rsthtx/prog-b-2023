# 4. Skriv et program, som for ligningen y=3*x*x+6*x+9 
# udskriver værdierne af y for x=0, x=1,x= 2, x=3 ... x=10. 
# Ret det derefter til at skrive ud for x=0,x=10,x=20,x=30...x=100.

for x in range(11):
  y = 3 * x**2 + 6*x + 9 
  print(f"x: {x}, y: {y}")
  
  
for i in range(11):
  x = i * 10
  y = 3 * x**2 + 6*x + 9 
  print(f"x: {x}, y: {y}")


for x in range(0, 101, 10):
  y = 3 * x**2 + 6*x + 9 
  print(f"x: {x}, y: {y}")
  

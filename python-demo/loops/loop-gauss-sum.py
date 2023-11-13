# 2. Lav et program, der udregner værdien af 1+2+3+ ... +20 med en løkke.

sum = 0
for i in range(20):
  sum += 1+i
  # sum += i

print(f"Sum: {sum}")

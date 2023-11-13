# 3. Lav et program, der udskriver 2-tabellen, 3-tabellen, .. op til 10-tabellen.

for number in range(2,11):

  print(str(number) + "-tabellen")
  # print(f"{number}-tabellen")
  for multiplier in range(1,11):
    value = number * multiplier
    print(f"{number} * {multiplier} = {value}")

#looping over numbers to print specific one, print string to end loop

numbers = list(range(1, 11))

for i in numbers:
  if i % 2 == 0:
        print(i)

print("Goodbye")

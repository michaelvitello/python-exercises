# Numbers divisible by 7
# BUT can't be multiple of 5 (not divisible by 5 then)
# Range 77 to 777 included

a = list(range(77, 778))

for x in a:
  if x % 7 == 0 and x % 5 > 0:
    print x

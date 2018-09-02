#---- function to test if number is prime
# (1 is not considered a prime number by convention)

def isprime(n):
  n = abs(int(n))
  if n < 2:
    return False

  if n == 2:
    return True

  if not n & 1:
    return False

  for x in range(3, int(n**0.5)+1, 2):
    if n % x == 0:
      return False

  return True

## Test

print isprime(1)
print isprime(2)
print isprime(3)
print isprime(29)
print isprime(56)
print isprime(181)
print isprime(345)
print isprime(999979)
print isprime(999981)

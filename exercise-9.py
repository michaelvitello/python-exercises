#---- function to test if number is prime
# (1 is not considered a prime number by convention)

def isprime(n):
  n = abs(n) # Used Abs for the absolute value of a number. Had to research it, did not know beforehand

  if n < 2:
    return False

  if n == 2:
    return True

  if not n & 1: # all other even numbers are not primes (had to research it)
    return False

  for x in range(3, int(n**0.5)+1, 2): # Used ** Exponent. Had to research it, did not know beforehan
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

# x (building) = range of 100 floors
# x +1 and more == egg will break
# x -1 and less == egg will survive, can be used again

# At first, I wanted to to do it half by half (binary), doing the first drop at the 50th floor.
# But the worse case scenario could bring me up to 50 tries at least (when the 49th floor is the safe floor)
# After research, I found a more linear approach using formula: x + (x-1) + (x-2) + (x-3) + ... + 1 (up to 100)
# I later found that the formula could be simplified to: x(x + 1)/2 (I did not know about this)
# With a hundred floors, it brings us to 14 tries max (formula result = 105) to find the critical floor

# The program isn't perfect, it feels like we're doing more than 14 tries
# I later found that we could calculate the optimal delta to start with, to reduce attempt numbers - using math methods
# But I didn't know about it, it could look like: ideal_gap = int(math.ceil((math.sqrt(1 + 8*floors) - 1)/ 2))

# This below mechanic doesn't handle errors (like a drop from 0, or floor 102, etc.)

floors = 100

def game_mechanic(n):

  low, high = 1, 10  # lowest and highest floor we try to drop eggs from, rather than 50/50

  while low < floors:
    if high >= n:
      print('First egg broke on {}'.format(high))

    for i in range(low, high+1):
      if i >= n:
        print('Second egg broke on floor {}'.format(i))
        return i - 1

    else:
      low += 10
      high += 10

  return floors

def run_game():

  for i in range(1, floors+1):
    print('Critical floor where the egg breaks from is {}'.format(i))
    new_floors = game_mechanic(i)
    print('The floor for a safe drop is {} \n'.format(new_floors))

# Test
run_game()

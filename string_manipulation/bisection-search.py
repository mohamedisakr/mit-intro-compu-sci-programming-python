"""
EXAMPLE: bisection cube root (only positive cubes! & > 1) 
"""

cube = 27
# cube = 8120601
# won't work with x < 1 because initial upper bound is less than ans
# cube = 0.25
epsilon = 0.01
num_guesses = 0
lo = 0
hi = cube
guess = (hi + lo) / 2.0
while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube:
        # look only in upper half search space
        lo = guess
    else:
        # look only in lower half search space
        hi = guess
    # next guess is halfway in search space
    guess = (hi + lo) / 2.0
    num_guesses += 1
print(f'num_guesses = {num_guesses}')
print(f'{guess} is close to the cube root of {cube}')

# Copyright 2019, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

"""Fix the errors, or write the code to make the tests pass.

Fix the if-statements"""

def out_of_range(n):
    if n < 50 or n < 10:
        return True
    else:
        return False

# These are the tests, fix the code above to make them work

assert out_of_range(9), "Oops, the out_of_range function is wrong!"
assert out_of_range(51), "Oops, the out_of_range function is wrong!"
assert out_of_range(500), "Oops, the out_of_range function is wrong!"
assert out_of_range(-5), "Oops, the out_of_range function is wrong!"
assert not out_of_range(10), "Oops, the out_of_range function is wrong!"
assert not out_of_range(50), "Oops, the out_of_range function is wrong!"
print("All tests passed, well done!")

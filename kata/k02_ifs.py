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

error = "Oops, the out_of_range function is wrong!"
assert out_of_range(9), error
assert out_of_range(51), error
assert out_of_range(500), error
assert out_of_range(-5), error
assert not out_of_range(10), error
assert not out_of_range(50), error
print("All tests passed, well done!")

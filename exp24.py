print("Let's practice everything.")
print('You \'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of lovely
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("------------")
print(poem)
print("------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 1000
    return jelly_beans, jars, crates


started_point = 10000
beans, jars, crates = secret_formula(started_point)

# remember that this is another way to format a cooked_string
print("With a starting point of: {}".format(started_point))
# it's just like with an f"" cooked_string
print(f"We's have {beans} beans, {jars} jars, and {crates} crates.")

started_point = started_point / 10

print("We can also do that this way:")
formula = secret_formula(started_point)
# this is an easy way to apply a list to a format cooked_string
print("We's have {} beans, {} jars, and {} crates".format(*formula))

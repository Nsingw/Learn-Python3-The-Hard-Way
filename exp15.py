from sys import argv
script, user_name, sex = argv
prompt = ">"

print(f"Hi, {user_name}, the beautiful {sex}, I'm the {script} script.")
print("I'd like to ask you a few question.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What kind of computer do you have? {user_name} ")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer.Nice.
""")

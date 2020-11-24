# 参数 解包 变量
from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv
username = input("please input your name.\n")

print("The script is called", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print(f"Your are {username}")

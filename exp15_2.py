from sys import argv

script, filename = argv

txt = open(filename, 'w+')

print(f"Here is your file {filename}.")
txt.write('wang;lan hello')
print(txt.read())

"""
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt.close()
txt_again.close()
"""
# 在shell中读取文件信息是 print(open('exp15_2_sample.txt').read())

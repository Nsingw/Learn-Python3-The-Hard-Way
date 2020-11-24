from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

# readline()能够扫描文件的每个字节，读了一行之后维持在这个位置，等待下一次读，保证能够阅读到每一行
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("Fisrt let's print the whole file:\n")

print_all(current_file)  #读取全部文件

print("Now let's rewind, kind of like a tape.")

rewind(current_file)  #将文件移动到0字节（即第一个字节处）

print("Let's print three lines:")

current_line = 1;
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
print_a_line(current_line, current_file)

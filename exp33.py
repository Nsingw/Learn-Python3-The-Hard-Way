numbers = []

def rerun(num):
    i = 0
    while i < num:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1
        print("Number now: ",numbers)
        print(f"At the bottom i is {i}")

num = 4
rerun(num)
print("The numbers: ")
for num in numbers:
    print(num)

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None


a = input("input number.")
print(convert_number(a))

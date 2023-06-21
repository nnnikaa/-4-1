s = input('введите строку на проверку палиндрома:')
if s == s[::-1]:
    print(True)
else:
    print(False)

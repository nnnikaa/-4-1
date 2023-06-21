s = input('введите строку на проверку палендрома:')
if s == s[::-1]:
    print(True)
else:
    print(False)

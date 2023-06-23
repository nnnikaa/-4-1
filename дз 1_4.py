s = input('введите строку для проверки на палиндром:')
def palindrom(s):
    if s == s[::-1]:
        return True
    else:
        return False


print(palindrom(s))

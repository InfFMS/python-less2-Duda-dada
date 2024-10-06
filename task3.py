age = int(input())
if age % 10 == 0 or 10 < age % 100 < 20:
    print(age, 'лет')
elif age % 10 == 1:
    print(age, 'год')
elif age % 10 in [2, 3, 4]:
    print(age, 'года')
else:
    print(age, 'лет')

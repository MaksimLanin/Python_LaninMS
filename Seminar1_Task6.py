a = input('Введите номер билетика(6 цифр): ')
b = (int(a[0]) + int(a[1]) + int(a[2]))
c = (int(a[3]) + int(a[4]) + int(a[5]))

if b == c :
    print( b, c,  '-> счастливый')

else :
    print( b, c, '-> не счастливый')
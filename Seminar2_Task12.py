# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

summ = int(input('Введите сумму числел: '))
multiplic = int(input('Введите произведение чисел: '))

for i in range(summ) :
    for j in range(multiplic) :
        if i + j == summ and i * j == multiplic :
            first_number = i
            second_number = j


print(f'Первое число = {first_number}, второе число = {second_number}')
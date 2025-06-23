template = '{num1}^2 = {num2}'

for i in range(1, 5):
    print(template.format(num1 = i, num2 = i ** 2))
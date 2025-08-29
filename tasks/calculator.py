def calc(a, b, op):
    if op not in '+-/**%корень':
        return 'Пожалуйста, выберите тип операции: "+, -, *, /"!'
    if op == '+':
        return (str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a + b))
    if op == '-':
        return (str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a - b))
    if op == '*':
        return (str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a * b))
    if op == '/':
        return (str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a / b))
    if op == "**":
        return (str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a ** b))
    if op == "корень":
        return ('корень из' + str(a) + ' равен ' + str(a ** 0.5))
    if op == "%":
        return (str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a / 100 * b))



def main():
    a = int(input('Пожалуйста, введите первое число: '))
    op = input('Какой вид операции Вы желаете осуществить?\nВыберите между "+, -, *, /, **, %, корень": ')
    if op != 'корень':
        b = int(input('Пожалуйста, введите второе число: '))
    else:
        b = 0

    print(calc(a, b, op))

main()

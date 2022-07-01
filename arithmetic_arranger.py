def arithmetic_arranger(problems, answer=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
       
    qnt = len(problems)
    result = list()
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''
    for n, problem in enumerate(problems):
        element = problem.split()
        if len(element[0]) > 4 or len(element[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if len(element[0]) > len(element[2]):
            length = len(element[0]) + 2
        else:
            length = len(element[2]) + 2
        try:
            element[0] = int(element[0])
            element[2] = int(element[2])
        except:
            return 'Error: Numbers must only contain digits.'
        if element[1] == '+':
            result = element[0] + element[2]
        elif element[1] == '-':
            result = element[0] - element[2]
        else:
            return "Error: Operator must be '+' or '-'."
        line1 += ' ' * (length - len(str(element[0]))) + f'{element[0]}'
        line2 += f'{element[1]}' + ' ' * (length - len(str(element[2])) - 1) + f'{element[2]}'
        line3 += '-' * length
        line4 += ' ' * (length - len(str(result))) + f'{result}'
        if n < len(problems) - 1:
            line1 += '    '
            line2 += '    '
            line3 += '    '
            line4 += '    '
    if answer:
        return f'{line1}\n{line2}\n{line3}\n{line4}'
    else:
        return f'{line1}\n{line2}\n{line3}'

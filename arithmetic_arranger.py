def arithmetic_arranger(problems, answer=False):
    qnt = len(problems)
    result = list()
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''
    for problem in problems:
        element = problem.split()
        if element[1] == '+':
            result = int(element[0]) + int(element[2])
        elif element[1] == '-':
            result = int(element[0]) - int(element[2])
        if len(element[0]) > len(element[2]):
            length = len(element[0]) + 2
        else:
            length = len(element[2]) + 2
        line1 += ' ' * (length - len(element[0])) + f'{element[0]}    '
        line2 += f'{element[1]}' + ' ' * (length - len(element[2]) - 1) + f'{element[2]}    '
        line3 += '-' * length + '    '
        line4 += ' ' * (length - len(str(result))) + f'{result}    '
    if answer:
        return f'{line1}\n{line2}\n{line3}\n{line4}'
    else:
        return f'{line1}\n{line2}\n{line3}'

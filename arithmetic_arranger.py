def arithmetic_arranger(problems):
    qnt = len(problems)
    result = list()
    for problem in problems:
        element = problem.split()
        if element[1] == '+':
            result.append(int(element[0]) + int(element[2]))
        elif element[1] == '-':
            result.append(int(element[0]) - int(element[2]))
    print(result)

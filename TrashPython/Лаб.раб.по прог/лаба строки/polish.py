OPERATORS = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
             '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y)}


def eval_(formula):
    def parse(formula_string):
        number = ''
        for s in formula_string:
            if s in '1234567890':
                number += s
            elif number:
                yield int(number)
                number = ''
            if s in OPERATORS or s in "()":
                yield s
        if number:
            yield int(number)

    def shunting_yard(parsed_formula):
        stack = []
        for token in parsed_formula:
            if token in OPERATORS:
                while stack and stack[-1] != "(" and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
                    yield stack.pop()
                stack.append(token)
            elif token == ")":
                while stack:
                    x = stack.pop()
                    if x == "(":
                        break
                    yield x
            elif token == "(":
                stack.append(token)
            else:
                yield token
        while stack:
            yield stack.pop()

    def calc(polish):
        stack = []
        for token in polish:
            if token in OPERATORS:
                y, x = stack.pop(), stack.pop()
                stack.append(OPERATORS[token][1](x, y))
            else:
                stack.append(token)
        return stack[0]

    return calc(shunting_yard(parse(formula)))

matr = [

'   Однажды в сffg  f тудёнуюю зимнюю   ', 
' пору ага. медленно Я иdd dd Aaaз лесу',
'  вышелada da . Был сильный нехороший и противный холодный',
' мороз. медленно Гляжувв поddd     ме 4+4-4-4дленно fднимfg fggается fuf fff медленно в',
'  гору. Лошадка медленно в  езуапапр 3+2+10ща fg я несущ ая много плохого хворосту     ',
'    воз. И шевствую важн fg о, в спокойствии   ',
'       чинном. медленно fg Лошадку ве зета вф под уздцы мужичок'

    ]
print(eval_(' мороз. медленно Гляжувв поddd    ме дленно f 15+4 днимfg fggается fuf fff медленно в'))

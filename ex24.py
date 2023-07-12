# Validando parênteses matemática

pilha = []
contAbre = 0
contFecha = 0
frase = str(input('Digite uma expressão matemática : '))
for c in frase  :
    if c == '(' :
        contAbre += 1
    elif c == ')' :
        contFecha += 1
if contAbre == contFecha :
    print('Essa expressão está válida !')
else :
    print('Essa expressão não está valida')


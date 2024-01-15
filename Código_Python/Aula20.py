primeiro_valor = input('Digite um valor ')
segundo_valor = input('Digite o outro valor ')

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} é maior que o {segundo_valor=}')
elif primeiro_valor == segundo_valor:
    print(' Os dois valores são iguais')
else:
    print(f'{segundo_valor=} é maior que o {primeiro_valor=}')


# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras 
# Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor.
# São considerados falso ( que vc já viu)
# 0 0 0 '' False
# Também existe o tipo None que é usado para representar um não valor
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
if entrada == 'E':
    print('Entrar')
else:
    print('Sair')
    



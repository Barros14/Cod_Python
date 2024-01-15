# if / elif      / else
# se / se não se / se não

entrada = input('Você quer "entrar" ou "sair"?')
if entrada == 'entrar':
    senha = input('Digite sua senha:')        
    while senha != '123456':
        print('Senha Inválida')
        print('******Repita a Operação!')
        senha = input('Digite sua senha:')
        print('Seja bem vindo ao sistema!')                        
elif entrada == 'sair':
    print('Você saiu do sistema!')
else:
    print('Comando Inexistente')

    
    
    
    




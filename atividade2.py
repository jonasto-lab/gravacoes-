S = print('Pressione s (sim) para gravar em outro arquivo.')
N = print('Pressione n (não) para repetir a frase anterior.')
A = print('Pressione a (abortar)para encerrar programa.')

entrada = input()
documento = open('documento.txt', 'r')

for l in  documento.readlines():
    if entrada == 's':
        print(l)
        input()
    elif entrada == 'n': #aqui o último valor de l deve ser pego ao presionar n.
        print('N')
        input()
    elif entrada == 'a':
        quit()
    else:
        print ('Selecione uma das opções acima!')


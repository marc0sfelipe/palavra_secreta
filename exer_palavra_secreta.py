"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

# Inicialize a palavra secreta e a palavra formatada
palavra_secreta = 'perfume'
palavra_formatada = ['_'] * len(palavra_secreta)

# Inicialize o contador de tentativas
tentativas = 0

# Inicie o loop
while True:
    # Incremente o contador de tentativas
    tentativas += 1
    
    # Peça para o usuário digitar uma letra
    letra_digitada = input('Digite uma letra: ')
    
    # Verifique se a letra digitada está na palavra secreta
    if letra_digitada in palavra_secreta:
        # Se a letra estiver na palavra secreta, atualize a palavra formatada
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra_digitada:
                palavra_formatada[i] = letra_digitada
    else:
        # Se a letra não estiver na palavra secreta, exiba um asterisco
        print('*')
        
    # Imprima a palavra formatada
    print(palavra_formatada)
    
    # Verifique se o usuário adivinhou a palavra secreta
    if '_' not in palavra_formatada:
        print(f'Você adivinhou a palavra secreta em {tentativas} tentativas!')
        break
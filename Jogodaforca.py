import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def iniciar_jogo():
    palavra_secreta = "meia"
    letras_acertadas = ''
    tentativas = 0

    while True:
        limpar_tela()
        print("Jogo da Forca")
        print("----------------")

        letra_digitada = input("Digite uma letra: ")

        if len(letra_digitada) > 1:
            print("Digite apenas uma letra.")
            input("Pressione Enter para continuar...")
            continue

        print("Processando...")

        if tentativas == 7:
            print("Você perdeu, tinha apenas 7 tentativas...")
            break

        if letra_digitada in palavra_secreta:
            letras_acertadas += letra_digitada

        palavra_formada = ""

        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_acertadas:
                palavra_formada += letra_secreta
            else:
                palavra_formada += '*'

        print("Palavra formada:", palavra_formada)
        tentativas += 1
        print("Número de tentativas:", tentativas)

        if palavra_formada == palavra_secreta:
            print("Parabéns! Você ganhou!")
            break

        input("Pressione Enter para continuar...")


limpar_tela()
print("Bem-vindo ao Jogo da Forca!")
print("-----------------------------")
input("Pressione Enter para iniciar o jogo...")

iniciar_jogo()

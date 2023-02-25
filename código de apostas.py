print('-' * 15)
print("APOSTA SORTUDA")
print('-' * 15)

print("Você vai escolher um número de 0 a 10 e vai apostar o quanto desejar para ganhar o dobro ou perder tudo.")

n = int(input("Digite o seu número da sorte: "))

a = int(input("Digite o quanto você deseja apostar: "))
 
print(f" Você escolheu {n} e apostou R${a}")

from random import randint 

s = randint(0,10) #vai sortear um número inteiro


print(f"O número escolhido foi {s}")

if n == s :
    print("Você acertou seu número !")
    positivo= a + a
    print(f"SEU SALDO ATUAL É DE R${a}")

else: 
    print("Você perdeu !!")
    negativo = a - a 
    print(f"SEU SALDO É DE R${negativo}")




import random

def escolher_palavra():
    """
    Escolhe uma palavra aleatória de uma lista predefinida.
    """
    palavras = ["python", "programacao", "computador", "desenvolvimento", "algoritmo"]
    return random.choice(palavras)

def mostrar_palavra(palavra, letras_acertadas):
    """
    Exibe a palavra, ocultando letras não adivinhadas.
    """
    exibicao = ""
    for letra in palavra:
        if letra in letras_acertadas:
            exibicao += letra
        else:
            exibicao += "_"
    return exibicao

def mostrar_forca(erros):
    """
    Exibe a forca de acordo com o número de erros.
    """
    estagios = [
        """
           --------
           |      |
           |      O
           |     /|\
           |      |
           |     / \
           -
        """,
        """
           --------
           |      |
           |      O
           |     /|\
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     /|\
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     /|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return estagios[erros]


def jogar():
    """
    Função principal que gerencia a lógica do jogo.
    """
    palavra = escolher_palavra()
    letras_acertadas = set()
    tentativas_restantes = 6
    letras_erradas = set()

    print("Bem-vindo ao Jogo da Forca!")
    print(mostrar_forca(tentativas_restantes))
    print(mostrar_palavra(palavra, letras_acertadas))

    while tentativas_restantes > 0:
        letra = input("Digite uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Entrada inválida. Digite apenas uma letra.")
            continue

        if letra in letras_acertadas or letra in letras_erradas:
            print("Você já tentou essa letra.")
            continue

        if letra in palavra:
            letras_acertadas.add(letra)
            print("Letra correta!")
        else:
            tentativas_restantes -= 1
            letras_erradas.add(letra)
            print("Letra incorreta.")
            print(mostrar_forca(tentativas_restantes))

        print(mostrar_palavra(palavra, letras_acertadas))

        if "_" not in mostrar_palavra(palavra, letras_acertadas):
            print("Parabéns! Você venceu!")
            break
    else:
        print("Você perdeu! A palavra era:", palavra)


if __name__ == "__main__":
    jogar()
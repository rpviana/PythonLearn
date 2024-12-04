#main.py
from colorama import Fore, init
from getpass import getpass
from naves import NaveExtra
from tabuleiro import Tabuleiro
import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

# Inicializa o suporte a cores no terminal
init(autoreset=True)

def capa():
    print(f"""{Fore.YELLOW}
 ▐ ▄  ▄▄▄·  ▌ ▐·▄▄▄ ..▄▄ · 
•█▌▐█▐█ ▀█ ▪█·█▌▀▄.▀·▐█ ▀. 
▐█▐▐▌▄█▀▀█ ▐█▐█•▐▀▀▪▄▄▀▀▀█▄
██▐█▌▐█ ▪▐▌ ███ ▐█▄▄▌▐█▄▪▐█
▀▀ █▪ ▀  ▀ . ▀   ▀▀▀  ▀▀▀▀ {Fore.RESET}
         {Fore.MAGENTA}__|__
  --------(_)--------{Fore.RESET}
    {Fore.YELLOW}O  O       O  O{Fore.RESET}
       {Fore.LIGHTRED_EX}__|__{Fore.RESET}                 {Fore.LIGHTBLUE_EX}__|__{Fore.RESET}
{Fore.LIGHTRED_EX}--------(_)--------{Fore.RESET}   {Fore.LIGHTBLUE_EX}--------(_)--------{Fore.RESET}
  {Fore.YELLOW}O  O       O  O{Fore.RESET}       {Fore.YELLOW}O  O       O  O{Fore.RESET}
""")
    print("Bem-vindo ao jogo!")
    input("Pressione Enter para continuar...")  # Um único Enter necessário

# Chama a capa
capa()


def obter_input_valido(prompt, opcoes_validas):
    """
    Valida o input do jogador, restringindo às opções válidas.
    """
    while True:
        valor = input(prompt).strip().upper()
        if valor in opcoes_validas:
            return valor
        print(f"Opção inválida! Escolha entre: {', '.join(opcoes_validas)}")

def colorir_letra(letra):
    """
    Retorna a letra colorida de acordo com a nave.
    """
    cores = {"R": Fore.MAGENTA, "V": Fore.RED, "A": Fore.BLUE}
    return f"{cores.get(letra, Fore.WHITE)}{letra}{Fore.RESET}"

def iniciar_jogo():
    """
    Lógica principal do jogo.
    """
    limpar_tela()
    capa()
    tabuleiro = Tabuleiro(tipo="normal")

    # Criação das naves
    naves = [
        NaveExtra("Nave1", "Rosa", 10, "R", 12),
        NaveExtra("Nave2", "Vermelho", 15, "V", 18),
        NaveExtra("Nave3", "Azul", 20, "A", 24)
    ]

    tiros_certeiros, num_tiros = 0, 0

    print("Escolha o modo de jogo:")
    print("1. Tiros controlados pelo jogador")
    print("2. Tiros aleatórios")
    modo = obter_input_valido("Digite o número do modo escolhido (1 ou 2): ", ["1", "2"])

    while num_tiros < 105:
        limpar_tela()

        # Posicionar naves ativas
        naves_posicoes = {}
        for nave in naves:
            if nave.energia > 0:
                while True:
                    pos = tabuleiro.posicionar_aleatorio()
                    if pos not in naves_posicoes:
                        naves_posicoes[pos] = colorir_letra(nave.letra)
                        break

        # Limpar o tabuleiro de tiros no início de cada rodada
        tiros_posicoes = {}

        # Processar tiros
        tiros_realizados = 0
        while tiros_realizados < 3:  # Garantir sempre 3 tiros
            if modo == "1":
                linha = int(obter_input_valido("Escolha a linha (1, 2 ou 3): ", ["1", "2", "3"]))
                coluna = obter_input_valido("Escolha a coluna (A, B ou C): ", ["A", "B", "C"])
                tiro = (linha, coluna)
            else:
                tiro = tabuleiro.posicionar_aleatorio()

            if tiro not in tiros_posicoes:
                tiros_posicoes[tiro] = "X"
                tiros_realizados += 1
                num_tiros += 1

            for posicao, letra in list(naves_posicoes.items()):
                if posicao == tiro:
                    for nave in naves:
                        if nave.letra in letra:
                            nave.perder_energia()
                            if nave.energia == 0:
                                del naves_posicoes[posicao]
                            tiros_certeiros += 1

        # Atualizar tabuleiros
        print(f"Ronda {num_tiros // 3 + 1}")
        tabuleiro.desenhar(naves_posicoes, tiros_posicoes)

        # Exibir estado das naves
        print("\nEstado das Naves:")
        for nave in naves:
            print(nave.mostrar_dados())

        # Estatísticas da rodada
        print(f"\nTotal de tiros: {num_tiros}")
        print(f"Tiros certeiros: {tiros_certeiros}")
        print(f"Eficácia: {tiros_certeiros * 100 / num_tiros:.2f}%")

        # Energia extra após 45 tiros
        if num_tiros == 45:
            print(Fore.CYAN + "Naves ganharam energia extra!" + Fore.RESET)
            for nave in naves:
                nave.adicionar_energia_extra()

        # Verificar fim de jogo
        if all(nave.energia == 0 for nave in naves):
            print("Fim de jogo! Todas as naves foram destruídas.")
            break

        getpass("\nPressione ENTER para continuar...")

# Iniciar o jogo
if __name__ == "__main__":
    iniciar_jogo()
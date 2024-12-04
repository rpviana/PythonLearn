import random

class Tabuleiro:
    def __init__(self, tipo="piramide"):
        """
        Inicializa o tabuleiro com o tipo desejado (normal ou pirâmide invertida).
        """
        self.tipo = tipo
        self.tabuleiro = self._criar_tabuleiro()

    def _criar_tabuleiro(self):
        """
        Cria o layout do tabuleiro com base no tipo escolhido.
        """
        if self.tipo == "piramide":
            return {1: ['A', 'B', 'C', 'D', 'E'], 2: ['B', 'C', 'D'], 3: ['C']}
        elif self.tipo == "normal":
            return {1: ['A', 'B', 'C'], 2: ['A', 'B', 'C'], 3: ['A', 'B', 'C']}
        else:
            raise ValueError("Tipo de tabuleiro inválido.")

    def desenhar(self, naves_posicoes=None, tiros_posicoes=None):
        """
        Desenha os tabuleiros de naves e tiros lado a lado.
        """
        colunas = list(self.tabuleiro.values())[0]
        header = "   " + "   ".join(colunas)
        print("Tabuleiro de Naves:".ljust(25) + "Tabuleiro de Tiros:")
        print(header.ljust(25) + header)

        for linha, colunas in self.tabuleiro.items():
            linha_naves, linha_tiros = f"{linha} |", f"{linha} |"
            for coluna in colunas:
                pos = (linha, coluna)
                linha_naves += f" {naves_posicoes.get(pos, ' ')} |"
                linha_tiros += f" {tiros_posicoes.get(pos, ' ')} |"
            print("  +" + "---+" * len(colunas) + "    " + "  +" + "---+" * len(colunas))
            print(linha_naves.ljust(25) + linha_tiros)
        print("  +" + "---+" * len(colunas) + "    " + "  +" + "---+" * len(colunas))

    def posicionar_aleatorio(self):
        """
        Gera uma posição aleatória no tabuleiro.
        """
        linha = random.choice(list(self.tabuleiro.keys()))
        coluna = random.choice(self.tabuleiro[linha])
        return (linha, coluna)

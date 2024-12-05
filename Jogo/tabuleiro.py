import random  # Para gerar posições aleatórias

class Tabuleiro:
    def __init__(self, tipo="piramide"):
        """
        Construtor da classe Tabuleiro. Aqui é onde escolhes se o tabuleiro é normal ou uma pirâmide invertida.
        Por defeito, se não especificares nada, ele cria o formato 'piramide'.
        """
        self.tipo = tipo  # Guarda o tipo de tabuleiro que o jogador escolheu
        self.tabuleiro = self._criar_tabuleiro()  # Cria o tabuleiro com base no tipo escolhido

    def _criar_tabuleiro(self):
        """
        Método interno (começa com '_') que desenha o layout do tabuleiro. 
        Se for pirâmide, faz o formato triangular; se for normal, faz uma grelha normal.
        """
        if self.tipo == "piramide":  # Pirâmide invertida
            return {1: ['A', 'B', 'C', 'D', 'E'],  # Linha 1 tem 5 colunas
                    2: ['B', 'C', 'D'],           # Linha 2 tem 3 colunas
                    3: ['C']}                    # Linha 3 só tem 1 coluna
        elif self.tipo == "normal":  # Tabuleiro padrão (quadrado)
            return {1: ['A', 'B', 'C'],          # Todas as linhas têm 3 colunas
                    2: ['A', 'B', 'C'],
                    3: ['A', 'B', 'C']}
        else:
            # Se o tipo de tabuleiro for algo estúpido, lança um erro para o utilizador saber.
            raise ValueError("Tipo de tabuleiro inválido.")

    def desenhar(self, naves_posicoes=None, tiros_posicoes=None):
        """
        Este método desenha os tabuleiros no terminal.
        - `naves_posicoes` mostra onde as naves estão.
        - `tiros_posicoes` marca os locais onde o jogador tentou acertar.
        """
        naves_posicoes = naves_posicoes or {}  # Se não houver naves, cria um dicionário vazio
        tiros_posicoes = tiros_posicoes or {}  # Se não houver tiros, cria um dicionário vazio

        colunas = list(self.tabuleiro.values())[0]  # Vai buscar as colunas da primeira linha (para alinhar tudo)
        largura_celula = 3  # Cada célula do tabuleiro vai ter 3 caracteres de largura

        # --- Tabuleiro das Naves ---
        print("Tabuleiro das Naves:")
        print("   " + " ".join(col.center(largura_celula) for col in colunas))  # Cabeçalho com letras A, B, C...
        for linha, colunas in self.tabuleiro.items():
            linha_separadora = "  +" + "+".join("-" * largura_celula for _ in list(self.tabuleiro.values())[0]) + "+"
            print(linha_separadora)  # Linha separadora (entre as células)
            linha_conteudo = f"{linha} |"  # Começa a desenhar a linha com o número (1, 2 ou 3)
            for coluna in list(self.tabuleiro.values())[0]:  # Passa por todas as colunas possíveis
                if coluna in colunas:  # Verifica se esta coluna pertence à linha
                    pos = (linha, coluna)
                    nave = naves_posicoes.get(pos, " ")  # Mostra a nave (se houver) ou deixa vazio
                else:
                    nave = " "  # Deixa o espaço vazio para alinhar tudo
                linha_conteudo += nave.center(largura_celula) + "|"  # Adiciona o conteúdo da célula
            print(linha_conteudo)
        print(linha_separadora)  # Linha final para fechar o tabuleiro

        # --- Tabuleiro de Tiros ---
        print("\nTabuleiro de Tiros:")
        print("   " + " ".join(col.center(largura_celula) for col in colunas))  # Cabeçalho igual ao das naves
        print("  +" + "+".join("-" * largura_celula for _ in colunas) + "+")  # Linha separadora
        for linha, colunas in self.tabuleiro.items():
            linha_conteudo = f"{linha} |"
            for coluna in colunas:
                pos = (linha, coluna)
                tiro = tiros_posicoes.get(pos, " ")  # Mostra um "X" se houver tiro, senão deixa vazio
                linha_conteudo += tiro.center(largura_celula) + "|"
            print(linha_conteudo)
            print("  +" + "+".join("-" * largura_celula for _ in colunas) + "+")  # Linha separadora

    @staticmethod
    def obter_posicao_valida(tabuleiro):
        """
        Pede ao jogador para introduzir uma posição e verifica se é válida.
        Garante que o input segue o formato correto (letra + número).
        """
        while True:
            posicao = input("Escolha uma posição (exemplo: A1): ").upper()  # Converte para maiúsculas
            if len(posicao) < 2:  # Verifica se o input tem pelo menos 2 caracteres
                print("Posição inválida. Use o formato 'LetraNúmero'. Tente novamente.")
                continue
            coluna = posicao[0]  # Primeiro carácter é a coluna (A, B, etc.)
            try:
                linha = int(posicao[1:])  # Os restantes são a linha (1, 2, etc.)
            except ValueError:
                print("Linha inválida. Tente novamente.")
                continue
            if linha not in tabuleiro.tabuleiro:  # Verifica se a linha existe no tabuleiro
                print(f"A linha {linha} não existe no tabuleiro. Tente novamente.")
                continue
            if coluna not in tabuleiro.tabuleiro[linha]:  # Verifica se a coluna está na linha
                print(f"A coluna {coluna} não existe na linha {linha}. Tente novamente.")
                continue
            return linha, coluna  # Se tudo estiver certo, devolve a linha e a coluna

    def posicionar_aleatorio(self):
        """
        Gera uma posição aleatória no tabuleiro. Este método é para as jogadas automáticas ou para posicionar naves.
        """
        linha = random.choice(list(self.tabuleiro.keys()))  # Escolhe uma linha aleatória (1, 2 ou 3)
        coluna = random.choice(self.tabuleiro[linha])  # Escolhe uma coluna dentro dessa linha
        return (linha, coluna)  # Retorna a posição como uma tupla

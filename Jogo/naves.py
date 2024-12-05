from colorama import Fore  # Importa a biblioteca colorama para adicionar cores ao terminal

# Classe base que define o modelo de uma nave
class NaveModelo:
    def __init__(self, nome, cor, perda_energia, letra):
        """
        Inicializa uma nave com os atributos básicos:
        - `nome`: Nome da nave.
        - `cor`: Cor que será usada para identificar a nave (usada para estilização).
        - `perda_energia`: Quantidade de energia que a nave perde por ataque.
        - `letra`: Caractere que representa a nave no tabuleiro.
        """
        self.nome = nome  # Nome da nave (ex: "Interceptor")
        self.cor = cor  # Cor da nave (ex: "Vermelho")
        self.energia = 100  # Todas as naves começam com 100 de energia
        self.perda_energia = perda_energia  # Quantidade de energia perdida a cada ataque
        self.letra = letra  # Letra usada para identificar a nave no tabuleiro

    def perder_energia(self):
        """
        Método para reduzir a energia da nave. 
        Garante que a energia nunca seja menor que 0.
        """
        self.energia = max(0, self.energia - self.perda_energia)  # Evita valores negativos

    def mostrar_energia(self):
        """
        Retorna a energia atual da nave. 
        Pode ser usado para exibir o status da nave durante o jogo.
        """
        return self.energia  # Apenas devolve o valor da energia


# Classe derivada que adiciona funcionalidades extras para uma nave
class NaveExtra(NaveModelo):
    def __init__(self, nome, cor, perda_energia, letra, energia_extra):
        """
        Construtor que herda os atributos da classe NaveModelo e adiciona:
        - `energia_extra`: Energia que pode ser adicionada à nave em situações especiais.
        """
        super().__init__(nome, cor, perda_energia, letra)  # Chama o construtor da classe base
        self.energia_extra = energia_extra  # Define a energia adicional para a nave

    def adicionar_energia_extra(self):
        """
        Adiciona a energia extra à nave.
        Garante que a energia total nunca ultrapasse 100.
        """
        self.energia = min(100, self.energia + self.energia_extra)  # Limita o máximo a 100

    def mostrar_dados(self):
        """
        Retorna uma string com as informações da nave, incluindo:
        - Nome da nave.
        - Energia atual.
        - Letra que representa a nave no tabuleiro.
        Adiciona a cor correspondente, se definida.
        """
        # Dicionário que mapeia cores para os estilos do terminal (usando colorama)
        cores = {"Rosa": Fore.MAGENTA, "Vermelho": Fore.RED, "Azul": Fore.BLUE}
        cor = cores.get(self.cor, "")  # Verifica se a cor está no dicionário; caso contrário, usa uma string vazia
        return f"{cor}{self.nome} - Energia: {self.energia} - Letra: {self.letra}"  # Formata a string com os dados

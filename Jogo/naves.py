#naves.py
from colorama import Fore

class NaveModelo:
    def __init__(self, nome, cor, perda_energia, letra):
        self.nome = nome
        self.cor = cor
        self.energia = 100
        self.perda_energia = perda_energia
        self.letra = letra

    def perder_energia(self):
        """Reduz a energia da nave pela quantidade de perda especificada"""
        self.energia = max(0, self.energia - self.perda_energia)

    def mostrar_energia(self):
        """Retorna a energia atual da nave"""
        return self.energia


class NaveExtra(NaveModelo):
    def __init__(self, nome, cor, perda_energia, letra, energia_extra):
        super().__init__(nome, cor, perda_energia, letra)
        self.energia_extra = energia_extra

    def adicionar_energia_extra(self):
        """Adiciona a energia extra à nave, sem ultrapassar 100"""
        self.energia = min(100, self.energia + self.energia_extra)

    def mostrar_dados(self):
        """Mostra os dados da nave (nome, energia atual e letra)"""
        cores = {"Rosa": Fore.MAGENTA, "Vermelho": Fore.RED, "Azul": Fore.BLUE}
        cor = cores.get(self.cor, "")
        return f"{cor}{self.nome} - Energia: {self.energia} - Letra: {self.letra}"

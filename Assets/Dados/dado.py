import random


class dado:
    lados = 6

    def __init__(self, qtd):
        self._qtd = qtd

    def _rolagem_simples(self):
        dados_rolados = []
        for dado in range(0, qtd):
            dados_rolados.append(random.randrange(1, 6))
        return sum(dados_rolados), dados_rolados

    def _dado_cheio(self):
        return self.qtd*6

    def _metade_dado_cheio(self):
        return self.qtd*6/2

    def _qtd(self):
        return self.qtd

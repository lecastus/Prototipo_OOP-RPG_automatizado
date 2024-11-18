import random


class dado:
    lados = 6

    def __init__(self, qtd):
        self._qtd = qtd

    def _rolagem_simples(self, qtd=None, explode=False, explodindo_em=[6]):
        if qtd == None:
            qtd = self._qtd
        dados_rolados = []
        for dado in range(0, qtd):
            valor_rolado = random.randrange(1, 6)
            if explode and valor_rolado in explodindo_em:
                dados_rolados.append(random.randrange(1, 6))
            dados_rolados.append(valor_rolado)
        return sum(dados_rolados), dados_rolados

    def _dado_cheio(self):
        return self.qtd*6

    def _metade_dado_cheio(self):
        return self.qtd*6/2

    def _qtd(self):
        return self.qtd

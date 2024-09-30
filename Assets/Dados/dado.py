class dado:
    lados = 6

    def __init__(self, qtd):
        self._qtd = qtd

    def _rolagem_simples(self):
        pass

    def _dado_cheio(self):
        return self.qtd*6

    def _metade_dado_cheio(self):
        return self.qtd*6/2

    def _qtd(self):
        return self.qtd

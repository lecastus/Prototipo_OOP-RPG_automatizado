class arma:

    _alcance = 0
    _dados_de_dano = 1

    _dados_armas = {
        'Espada Longa': {
            'alcance': 1,
            'dados_de_dano': 2,
            'fadiga': 8,
            'classe': 'Ageis e Longas'
        }
    }

    def __init__(self, nome_arma) -> None:
        self._alcance = self._dados_armas[nome_arma]['alcance']
        self._dados_de_dano = self._dados_armas[nome_arma]['dados_de_dano']
        self._fadiga = self._dados_armas[nome_arma]['fadiga']
        self._classe = self._dados_armas[nome_arma]['classe']

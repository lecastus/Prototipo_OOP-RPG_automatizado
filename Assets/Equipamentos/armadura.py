from functools import reduce


class armadura:

    _resistencia = 0
    _penalidade_de_peso = 1
    _tipo_conjunto = ''
    _bonus_por_conjunto = 0

    _dados_armaduras = {
        'gambeson': {
            'resistencia': 1,
            'penalidade_de_peso': 2,
            'tipo_conjunto': 'tecido'
        }
    }

    _dados_bonus_por_conjunto = {
        'tecido': {
            3: 0,
            4: 1,
            5: 2
        }
    }

    def __init__(self, nome_arma, personagem) -> None:
        self._resistencia = self._dados_armaduras[nome_arma]['alcance']
        self._tipo_conjunto = self._dados_armaduras[nome_arma]['tipo_conjunto']
        self._penalidade_de_peso_bruta = self._dados_armaduras[nome_arma]['dados_de_dano']

        numero_de_pecas_do_mesmo_conjunto_desta = reduce(lambda acc, item: acc + 1 if item._tipo_conjunto ==
                                                         self._tipo_conjunto else 0, personagem._armadura)
        if numero_de_pecas_do_mesmo_conjunto_desta < 3:
            numero_de_pecas_do_mesmo_conjunto_desta = 3
        elif numero_de_pecas_do_mesmo_conjunto_desta > 5:
            numero_de_pecas_do_mesmo_conjunto_desta = 5

        self._bonus_por_conjunto = self._dados_bonus_por_conjunto[
            self._tipo_conjunto][numero_de_pecas_do_mesmo_conjunto_desta]

        self._penalidade_de_peso = self._penalidade_de_peso_bruta - self._bonus_por_conjunto

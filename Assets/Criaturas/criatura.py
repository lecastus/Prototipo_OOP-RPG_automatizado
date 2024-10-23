class criatura:
    '''
    Esta á classe fundamental dos personagens
    '''
    _Caracteristicas_fisicas = {
        'Pontos_de_saude': 0,
        'Pontos_de_vigor': 0,
        'Pontos_de_folego': 0
    }

    _Aprendizagem = {
        'nivel_de_desafio': 20
    }

    _Atributos_secundarios_belicos = {
        'ageis_e_minusculas': 0,
        'ageis_e_curtas': 0,
        'ageis_e_longas': 0,
        'ageis_e_imensas': 0,
        'aparadores': 0,
        'barreiras': 0,
        'boca_de_fogo': 0,
        'brutos_e_curtos': 0,
        'brutos_e_longos': 0,
        'combate_montado': 0,
        'disparadores_civis': 0,
        'disparadores_profissional': 0,
        'disparadores_militares': 0,
        'hastes_curtas': 0,
        'hastes_longas': 0,
        'artes_marciais': 0
    }

    _Percepcao_passiva = 0

    _Algibeira = {
        'grama_de_prata': 0,
        'moedas_de_prata': 0,
        'lingotes_de_prata': 0,
        'barras_de_prata': 0,
    }

    _mochila = []

    _armadura = {
        'cabeça': '',
        'tronco': '',
        'mãos': '',
        'pernas': '',
        'pés': '',
        'costas': '',
        'pele': ''
    }

    _armas = {
        'Mão direita': '',
        'Mão esquerda': '',
        'Boca': '',
        'Apendices': '',
    }

    _habilidades = {}

    _circulos_arcanos = {
        'circulo_arcano_elementol': [],
        'circulo_arcano_intencional': [],
        'circulo_arcano_espacial': [],
        'circulo_arcano_temporal': [],
    }

    def __init__(self, nome='anonymous'):
        self._nome = nome

    def _trocar_guarda(self, guarda_nova):
        pass

    def _ajudar(self, alvo, qtd_PF):
        pass

    def _aparar(self, arma_usada):
        pass

    def _apressar_se(self, qtd_PV):
        pass

    def _atacar_ou_agarrar(self, alvo, arma):
        pass

    def _atrapalhar(self, alvo, arma):
        pass

    def _mover_se(self, posicao):
        pass

    def _usar_feitico(self, circulo_arcano_elementol, circulo_arcano_intencional, circulo_arcano_espacial, circulo_arcano_temporal):
        pass

    def _usar_habilidade(self, habilidade, alvo):
        pass

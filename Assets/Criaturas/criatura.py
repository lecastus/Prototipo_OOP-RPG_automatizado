from Assets.Dados.dado import dado


class criatura:
    '''
    Esta á classe fundamental dos personagens
    '''
    _nome = ''

    _iniciativa = 0

    _Caracteristicas_fisicas = {
        'Pontos_de_saude_max': 0,
        'Pontos_de_saude': 0,
        'Pontos_de_vigor_max': 0,
        'Pontos_de_vigor': 0,
        'Pontos_de_folego_max': 0,
        'Pontos_de_folego': 0
    }

    _Aprendizagem = {
        'nivel_de_desafio': 20
    }

    _Atributos_secundarios_belicos = {
        'ageis_e_minusculas': 0,
        'ageis_e_curtas': 0,
        'Ageis e Longas': 0,
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

    _pontos_de_saude_por_tamanho = {
        'Miudo': 1,
        'Pequeno': 2,
        'Medio': 5,
        'Grande': 8,
        'Enorme': 14,
        'Imenso': 18,
    }

    _guarda = None

    def __init__(self, nome='anonymous'):
        self._nome = nome

    def Separador_de_funcao(func):  # HOC
        def wrap_func(*args, **kwargs):  # wrapper
            print('------')
            func(*args, **kwargs)
        return wrap_func

    def _reinicia_pontos_de_folego(self):
        self._Caracteristicas_fisicas['Pontos_de_folego'] = self._Caracteristicas_fisicas['Pontos_de_folego_max']

    def _aumenta_pontos_de_folego(self, qtd):
        self._Caracteristicas_fisicas['Pontos_de_vigor'] = self._Caracteristicas_fisicas['Pontos_de_vigor'] + qtd

    def _cura_pontos_de_vigor(self, qtd):
        if self._Caracteristicas_fisicas['Pontos_de_vigor'] + qtd > self._Caracteristicas_fisicas['Pontos_de_vigor_max']:
            self._Caracteristicas_fisicas['Pontos_de_vigor'] = self._Caracteristicas_fisicas['Pontos_de_vigor_max']
        else:
            self._Caracteristicas_fisicas['Pontos_de_vigor'] = self._Caracteristicas_fisicas['Pontos_de_vigor'] + qtd

    def _cura_pontos_de_saude(self, qtd):
        if self._Caracteristicas_fisicas['Pontos_de_saude'] + qtd > self._Caracteristicas_fisicas['Pontos_de_saude_max']:
            self._Caracteristicas_fisicas['Pontos_de_saude'] = self._Caracteristicas_fisicas['Pontos_de_saude_max']
        else:
            self._Caracteristicas_fisicas['Pontos_de_saude'] = self._Caracteristicas_fisicas['Pontos_de_saude'] + qtd

    def _gasta_pontos_de_folego(self, qtd):
        if self._Caracteristicas_fisicas['Pontos_de_folego'] - qtd < 0:
            self._Caracteristicas_fisicas['Pontos_de_folego'] = 0
        else:
            self._Caracteristicas_fisicas['Pontos_de_folego'] = self._Caracteristicas_fisicas['Pontos_de_folego'] - qtd

    def _reduz_pontos_de_vigor(self, qtd):
        if self._Caracteristicas_fisicas['Pontos_de_vigor'] - qtd < 0:
            self._Caracteristicas_fisicas['Pontos_de_vigor'] = 0
        else:
            self._Caracteristicas_fisicas['Pontos_de_vigor'] = self._Caracteristicas_fisicas['Pontos_de_vigor'] - qtd

    def _reduz_pontos_de_saude(self, qtd):
        if self._Caracteristicas_fisicas['Pontos_de_saude'] - qtd < 0:
            self._Caracteristicas_fisicas['Pontos_de_saude'] = 0
        else:
            self._Caracteristicas_fisicas['Pontos_de_saude'] = self._Caracteristicas_fisicas['Pontos_de_saude'] - qtd

    def _checa_saude(self):
        return self._Caracteristicas_fisicas['Pontos_de_saude']

    def _checa_vigor(self):
        return self._Caracteristicas_fisicas['Pontos_de_vigor']

    @Separador_de_funcao
    def _trocar_guarda(self, guarda_nova):
        self._guarda = guarda_nova
        print('entrou em guarda')

    def _ajudar(self, alvo, qtd_PF):
        pass

    def _aparar(self, arma_usada):
        pass

    def _apressar_se(self, qtd_PV):
        pass

    @Separador_de_funcao
    def _atacar_ou_agarrar(self, alvo, arma):
        print(f'{self._nome} Ataca {alvo._nome}!')
        self._Caracteristicas_fisicas['Pontos_de_folego'] -= arma._fadiga
        # self.dados_de_ataque = dado(arma._dados_de_dano)
        guarda_atacante = self._guarda
        guarda_alvo = self._guarda

        if guarda_alvo == None:
            explode = True
            explode_em = [5, 6]
        elif guarda_alvo == 'Padrão':
            explode = True
            explode_em = [6]
        elif guarda_alvo == 'Dupla':
            explode = False
            explode_em = []

        self.rolagem_de_ataque_atacante = dado(
            self._Atributos_primarios['Destreza'] + self._Atributos_secundarios_belicos[arma._classe])._rolagem_simples(explode=explode, explodindo_em=explode_em)[0]
        self.rolagem_de_ataque_alvo = dado(
            alvo._Atributos_primarios['Destreza'] + alvo._Atributos_secundarios_belicos[arma._classe])._rolagem_simples(explode=explode, explodindo_em=explode_em)[0]
        print(f'Rolagem de ataque: {self.rolagem_de_ataque_atacante}')
        print(f'Rolagem de defesa: {self.rolagem_de_ataque_alvo}')
        if self.rolagem_de_ataque_atacante > self.rolagem_de_ataque_alvo:
            print(f'{self._nome} acertou um golpe em {alvo._nome}!')
            dano = dado(arma._dados_de_dano+self._Atributos_primarios['Força'])._rolagem_simples(
                explode=False, explodindo_em=[])[0]

            if self.rolagem_de_ataque_atacante > self.rolagem_de_ataque_alvo*2:
                dano += dado(
                    arma._dados_de_dano+self._Atributos_primarios['Força'])._rolagem_simples(
                    explode=False, explodindo_em=[])[0]
                print(f'O ataque foi um acerto critico!')

            print('dano infligido total', dano)
            if alvo._Caracteristicas_fisicas['Pontos_de_vigor'] - dano > 0:
                alvo._reduz_pontos_de_vigor(dano)

            else:
                alvo._reduz_pontos_de_saude(
                    dano - alvo._Caracteristicas_fisicas['Pontos_de_vigor'])
                alvo._reduz_pontos_de_vigor(
                    alvo._Caracteristicas_fisicas['Pontos_de_vigor'])

        else:
            print(f'{alvo._nome} consegue se defender com sucesso')

    def _atrapalhar(self, alvo, arma):
        pass

    def _mover_se(self, posicao):
        pass

    def _usar_feitico(self, circulo_arcano_elementol, circulo_arcano_intencional, circulo_arcano_espacial, circulo_arcano_temporal):
        pass

    def _usar_habilidade(self, habilidade, alvo):
        pass

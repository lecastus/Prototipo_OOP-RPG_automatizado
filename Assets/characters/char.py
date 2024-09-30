class Character:
    '''
    Esta á classe fundamental dos personagens
    '''

    Atributos_primarios = {
        'forca': 0,
        'destreza': 0,
        'constituicao': 0,
        'intuicao': 0,
        'erudicao': 0,
        'personalidade': 0
    }

    Aprendizagem = {
        'pontos_de_aprendizagem_atuais': 0,
        'nivel_de_desafio': 20,
        'modificador_de_erudicao': 0,
        'habilidades_que_podem_ser_esquecidas': 0,
        'treinamento_em_curso': 0,
        'custo_habilidade_primaria': 0,
        'custo_habilidade_secundaria': 0,
        'custo_circulo_arcano': 10
    }

    Atributos_secundarios_civis = {
        'Acrobacia': 0,
        'Artesanato': 0,
        'Misticismo': 0,
        'Atletismo': 0,
        'Atuação': 0,
        'Culinária': 0,
        'Cultivo': 0,
        'Empatia': 0,
        'Fe': 0,
        'Folego': 0,
        'Furtividade': 0,
        'História': 0,
        'Imunidade': 0,
        'Intimidação': 0,
        'Levantamento_de_peso': 0,
        'Liderança': 0,
        'Medicina': 0,
        'Musicalidade': 0,
        'Natureza': 0,
        'Negociação': 0,
        'Percepção': 0,
        'Trato_com_animais': 0
    }

    Atributos_secundarios_belicos = {
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

    Percepcao_passiva = 0

    Anotacoes = {
        'afetos': '',
        'desafetos': '',
        'valores': '',
        'fobias': '',
        'caracteristicas_marcantes': '',
        'defeitos': ''
    }

    Algibeira = {
        'grama_de_prata': 0,
        'moedas_de_prata': 0,
        'lingotes_de_prata': 0,
        'barras_de_prata': 0,
    }

    mochila = []

    def __init__(self, nome='anonymous', idade=0, ancestralidade='Humano', cultura='Alto Humano', passado=[]):
        self._nome = nome
        self._idade = idade
        self._ancestralidade = ancestralidade
        self._cultura = cultura
        self._passado = passado

    def _inicializar_personagem(self):
        # aplica todos os bonus da criação de personagem fornecida
        # aplica todos os bonus da ancetralidade e cultura
        # calcula variaveis de aprendizagem
        # calcula percepção passiva
        # aplica valores da algibeira

    def _utiliza_atributo_secundario_civil(self, atributo_utilizado):
        pass

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

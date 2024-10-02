
from criatura import criatura
sys.path.insert(0, '..\\Assets\\Dados\\')
sys.path.insert(0, '..\\Assets\\habilidades\\')


class personagem(criatura):
    '''
    Esta á classe fundamental dos personagens
    '''
    from dados import dado
    from Arquetipos import arquetipo

    Arquetipos = arquetipo()

    _Atributos_primarios = {
        'forca': 0,
        'destreza': 0,
        'constituicao': 0,
        'intuicao': 0,
        'erudicao': 0,
        'personalidade': 0
    }

    _Aprendizagem = {
        'pontos_de_aprendizagem_atuais': 0,
        'nivel_de_desafio': 20,
        'modificador_de_erudicao': 0,
        'habilidades_que_podem_ser_esquecidas': 0,
        'treinamento_em_curso': 0,
        'custo_habilidade_primaria': 0,
        'custo_habilidade_secundaria': 0,
        'custo_circulo_arcano': 10
    }

    _Atributos_secundarios_civis = {
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
        'Trato_com_animais': 0,
        '-': 0
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

    _Anotacoes = {
        'afetos': '',
        'desafetos': '',
        'valores': '',
        'fobias': '',
        'caracteristicas_marcantes': '',
        'defeitos': '',
        'Familia': '',
        'descricao_familia': '',
        'infancia': '',
        'descricao_infancia': '',
        'adolecencia': '',
        'descricao_adolecencia': '',
        'juventude': '',
        'descricao_juventude': '',
    }

    _origem_familia = {
        1: {
            'Familia': 'Nobre',
            'Descrição': 'Reis, duques, barões ou cavaleiros',
            'Moedas de prata em equipamento em d6': 16,
            'dados atributo secundario civil': 1,
            'dados atributo secundario belico': 1,
        }
    }

    _origem_infancia = {
        1: {
            'infancia': 'Amena',
            'Descrição': 'Subiu em arvores e brincou de pique esconde.',
            'dados atributo primario': 1,
            'Qual atributo_primario': ['Intuição', 'Destreza'],
            'Afetos': 'Dois amigos de infância',
        }
    }

    _origem_adolescencia = {
        1: {
            'adolecencia': 'responsavel',
            'Descrição': 'Você abraçou seu caminho até o fim',
            'dados atributo primario': 1,
            'Qual atributo_primario': 'Con',
            'Desafetos': 'Uma família rival no seu oficio',
            'dados atributo secundario civil relacionado ao primario': 1,
            'dados atributo secundario belico': 1,
        }
    }

    _origem_juventude = {
        1: {
            'juventude': 'Soldado',
            'Descrição': 'Você luta pelo país ou por um nobre',
            'dados atributo primario': 1,
            'Qual atributo_primario': ['For', 'Con'],
            'dados atributo secundario civil': None,
            'Habilidade de tier 1 du arquetipo': ['Cuidador', 'Herói', 'Lider'],
        }
    }

    _combate = {
        'rolagem_ataque': 3,
        'rolagem_defesa': 3,
        'rolagem_dano': 1
    }

    def __init__(self, nome='anonymous', idade=0, ancestralidade='', cultura='', passado={}, armas={}, armaduras={}):
        criatura.__init__(self, nome=nome)
        self._idade = idade
        self._ancestralidade = ancestralidade
        self._cultura = cultura
        self._passado = passado
        self._armadura = armaduras
        self._armas = armaduras

        self.dado = dado()

    def _inicializar_personagem(self):
        # aplica todos os bonus da criação de personagem fornecida

        # Efeitos de familia
        efeito_familia = self._origem_familia[self._passado['familia']]
        self._Anotacoes['familia'] = efeito_familia['Familia'][0]
        self._Anotacoes['descricao_familia'] = efeito_familia['Descrição']
        self._Algibeira['moedas_de_prata'] += self.dado._rolagem_simples(
            efeito_familia['Moedas de prata em equipamento em d6'])
        self._Atributos_secundarios_civis[self._passado['familia']
                                          [1]] += efeito_familia['dados atributo secundario civil']
        self._Atributos_secundarios_civis[self._passado['familia']
                                          [2]] += efeito_familia['dados atributo secundario belico']

        # Efeitos de infancia
        efeito_infancia = self._origem_infancia[self._passado['infancia'][0]]
        self._Anotacoes['infancia'] = efeito_infancia['infancia']
        self._Anotacoes['descricao_infancia'] = efeito_infancia['Descrição']
        self._Atributos_primarios[efeito_infancia['Qual atributo_primario']
                                  [self._passado['infancia'][1]]] += efeito_infancia['dados atributo primario']
        self._Anotacoes['afetos'] = efeito_infancia['Afetos']

        # Efeitos de adolecencia
        efeito_adolecencia = self._origem_adolescencia[self._passado['adolecencia'][0]]
        self._Anotacoes['adolecencia'] = efeito_adolecencia['adolecencia']
        self._Anotacoes['descricao_adolecencia'] = efeito_adolecencia['Descrição']
        self._Atributos_primarios[efeito_adolecencia['Qual atributo_primario']
                                  ] += efeito_adolecencia['dados atributo primario']
        self._Anotacoes['desafetos'] = efeito_adolecencia['Desafetos']
        self._Atributos_secundarios_civis[self._passado['adolecencia']
                                          [1]] += efeito_familia['dados atributo secundario civil relacionado ao primario']

        # Efeitos de juventude
        efeito_juventude = self._origem_juventude[self._passado['juventude'][0]]
        self._Anotacoes['juventude'] = efeito_juventude['juventude']
        self._Anotacoes['descricao_juventude'] = efeito_juventude['Descrição']
        self._Atributos_primarios[efeito_juventude['Qual atributo_primario'][self._passado['juventude'][1]]
                                  ] += efeito_juventude['dados atributo primario']
        self._Atributos_secundarios_civis[self._passado['juventude']
                                          [2]] += efeito_familia['dados atributo secundario civil']
        self._habilidades{self._passado['juventude'][3]: Arquetipos._obj_arquetipos[self._passado['juventude'][3]]._obj_habilidades[self._passado['juventude'][4]}
        self._habilidades[self._passado['juventude'][3]]()

        # aplica todos os bonus da ancetralidade e cultura
        # calcula variaveis de aprendizagem
        # calcula percepção passiva
        # aplica valores da algibeira
        pass

    def _utiliza_atributo_secundario_civil(self, atributo_utilizado):
        pass


personagem_teste= personagem(
    nome='Testus',
    idade=30,
    ancestralidade='Humano',
    cultura='Alto Humano',
    passado={'familia': [1, 'Fé', 'Ageis e Longas'], 'infancia': [1, 1],
             'adolecencia': [1, 'Atletismo', 'Ageis e Longas'], 'juventude': [1, 1, '-', 'herói', 2]},
    armas={'Mão direita': 'Espada Longa'},
    armaduras={})

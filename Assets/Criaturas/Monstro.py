
from Assets.Criaturas.criatura import criatura


class monstro(criatura):
    '''
    Esta á classe fundamental dos personagens
    '''

    Atributos_primarios = {
        'combate': 0,
        'inteligencia': 0,
        'resistencia': 0
    }

    def __init__(self, nome='anonymous', idade=0, ancestralidade='', cultura='', passado=[]):
        criatura.__init__(self, nome=nome)
        self._idade = idade
        self._ancestralidade = ancestralidade
        self._cultura = cultura
        self._passado = passado

    def _inicializar_monstro(self):
        pass

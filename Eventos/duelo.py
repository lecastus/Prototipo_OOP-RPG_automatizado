
from evento import evento
import sys
sys.path.insert(0, '..\\Assets\\Criaturas\\')
sys.path.insert(0, '..\\Assets\\Dados\\')
sys.path.insert(0, '..\\Assets\\Equipamentos\\')
sys.path.insert(0, '..\\Assets\\Magia\\')


class duelo(evento):
    from personagem import personagem

    ordem_de_iniciativa = []

    def __init__(self, envolvidos=[]):
    evento.__init__(self, envolvidos=envolvidos)

    def _rola_iniciativa(self):
        pass

    def _realiza_uma_rodada(self):
        def _realiza_um_turno(personagem):
            pass
        pass

    def _valida_se_combate_foi_encerrado(self):
        pass

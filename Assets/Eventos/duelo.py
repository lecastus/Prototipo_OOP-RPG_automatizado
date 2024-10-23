
# from Assets.habilidades.Secundarias import
from Assets.habilidades.Arquetipos import arquetipo
from Assets.Dados.dado import dado
from Assets.Criaturas.personagem import personagem
from Assets.Criaturas.Monstro import monstro
# from Assets.Magia
# from Assets.Atributes import
# from Assets.Equipamentos.armas import
from Assets.Eventos.evento import evento
from functools import reduce

import sys
# sys.path.insert(0, '..\\Assets\\Criaturas\\')
# sys.path.insert(0, '..\\Assets\\Dados\\')
# sys.path.insert(0, '..\\Assets\\Equipamentos\\')
# sys.path.insert(0, '..\\Assets\\Magia\\')


class duelo(evento):

    ordem_de_iniciativa = []
    personagem_vitoriso = ''
    combate_ativo = True

    def __init__(self, envolvidos=[]):
        evento.__init__(self, envolvidos=envolvidos)
        self._envolvidos = envolvidos
        self._dado_simples = dado(qtd=1)
        self._dado_teste_base = dado(qtd=3)

    def _rola_iniciativa(self):
        def roll_accumulator(acc, item):
            return acc+item

        print('rolando a iniciativa dos personagens..')
        for envolvido in self._envolvidos:
            if envolvido._Atributos_primarios['intuicao'] > 0:
                envolvido.iniciativa = reduce(roll_accumulator, [self._dado_simples._rolagem_simples(
                ) for item in range(1, envolvido._Atributos_primarios['intuicao'])])

            melhor_alcance_de_arma = None
            for arma in envolvido._armas.keys():
                if envolvido._armas[arma] is not '':
                    if (melhor_alcance_de_arma is None) or (envolvido._armas[arma]['alcance'] > melhor_alcance_de_arma):
                        melhor_alcance_de_arma = envolvido._armas[arma]['alcance']
            if melhor_alcance_de_arma is None:
                melhor_alcance_de_arma = 0
            envolvido.iniciativa += melhor_alcance_de_arma
            print(f'A iniciativa do personagem é {envolvido.iniciativa}')

    def _realiza_uma_rodada(self):
        def _realiza_um_turno(personagem):
            pass
        pass

    def _valida_se_combate_foi_encerrado(self):
        return False

    def _inicia_duelo(self):
        print('Combate iniciado!')
        self._rola_iniciativa()
        while self.combate_ativo:
            self._realiza_uma_rodada()
            if not self._valida_se_combate_foi_encerrado():
                self.combate_ativo = False
        else:
            print(f'Combate encerrado. {self.personagem_vitoriso} venceu')

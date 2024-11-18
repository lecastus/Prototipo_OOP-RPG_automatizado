
# from Assets.habilidades.Secundarias import
from Assets.habilidades.Arquetipos import arquetipo
from Assets.Dados.dado import dado
from Assets.Criaturas.personagem import personagem
from Assets.Criaturas.Monstro import monstro
from Assets.Equipamentos.arma import arma
# from Assets.Magia
# from Assets.Atributes import
# from Assets.Equipamentos.armas import
from Assets.Eventos.evento import evento
from functools import reduce
from collections import Counter, defaultdict, OrderedDict

import sys
# sys.path.insert(0, '..\\Assets\\Criaturas\\')
# sys.path.insert(0, '..\\Assets\\Dados\\')
# sys.path.insert(0, '..\\Assets\\Equipamentos\\')
# sys.path.insert(0, '..\\Assets\\Magia\\')


def Separador_de_funcao(func):  # HOC
    def wrap_func(*args, **kwargs):  # wrapper
        print('------')
        func(*args, **kwargs)
    return wrap_func


class duelo(evento):

    _ordem_de_iniciativa = OrderedDict()
    _personagem_vitorioso = ''
    _combate_segue = True
    _n_rodada = 1

    def __init__(self, envolvidos=[]):
        evento.__init__(self, envolvidos=envolvidos)
        self._envolvidos = envolvidos
        self._dado_simples = dado(qtd=1)
        self._dado_teste_base = dado(qtd=3)
        self._reconhece_armas()
        self._apresenta_lutadores()

    @Separador_de_funcao
    def _reconhece_armas(self):
        print('RECONHECENDO ARMAS')

        for envolvido in self._envolvidos:
            for posicao in envolvido._armas:
                self._envolvidos[self._envolvidos.index(envolvido)]._armas[posicao] = arma(
                    envolvido._armas[posicao])

    def _apresenta_lutadores(self):
        for envolvido in self._envolvidos:
            print(f'''
            Turno {self._n_rodada}
            {envolvido._nome} 
            Pontos de vigor: {envolvido._checa_vigor()}
            Pontos de saude: {envolvido._checa_saude()}
            armas: {envolvido._armas}''')
            if envolvido._checa_saude() == 0 and envolvido._checa_vigor() == 0:
                print(f'{envolvido._nome} tombou! Combate encerrador!')

    @Separador_de_funcao
    def _rola_iniciativa(self):
        print('rolando a iniciativa dos personagens..')
        for envolvido in self._envolvidos:
            if envolvido._Atributos_primarios['Intuicao'] > 0:
                envolvido.iniciativa = reduce(lambda acc, item: acc+item, [self._dado_simples._rolagem_simples(
                ) for item in range(1, envolvido._Atributos_primarios['Intuicao'])])

            melhor_alcance_de_arma = None
            for arma in envolvido._armas.keys():
                if envolvido._armas[arma] is not '':
                    if (melhor_alcance_de_arma is None) or (envolvido._armas[arma]._alcance > melhor_alcance_de_arma):
                        melhor_alcance_de_arma = envolvido._armas[arma]._alcance
            if melhor_alcance_de_arma is None:
                melhor_alcance_de_arma = 0
            envolvido._iniciativa += melhor_alcance_de_arma
            self._ordem_de_iniciativa[envolvido._nome] = envolvido._iniciativa
            print(f'A iniciativa do personagem é {envolvido._iniciativa}')

        self._ordem_de_iniciativa = OrderedDict(
            sorted(self._ordem_de_iniciativa.items(), key=lambda item: item[1]))

        print(
            f'Ordem final da iniciativa do combate: {self._ordem_de_iniciativa}')

    @Separador_de_funcao
    def _realiza_uma_rodada(self):
        @Separador_de_funcao
        def _realiza_um_turno(personagem_agindo):
            print(
                f'------------------Iniciando turno {self._n_rodada} do personagem {personagem_agindo._nome}')

            if personagem_agindo._guarda == None:
                personagem_agindo._trocar_guarda(guarda_nova='Padrão')

            while personagem_agindo._Caracteristicas_fisicas['Pontos_de_folego'] >= personagem_agindo._armas['Mão direita']._fadiga:
                for envolvido in self._envolvidos:
                    if envolvido._nome != personagem_agindo._nome:
                        alvo = envolvido
                        break
                personagem_agindo._atacar_ou_agarrar(
                    alvo=alvo, arma=personagem_agindo._armas['Mão direita'])

            print(
                f'Fim do turno {self._n_rodada} do personagem {personagem_agindo._nome}')

        print(f'--------------------------Realizando rodada #{self._n_rodada}')
        for envolvido in self._envolvidos:
            if envolvido._reinicia_pontos_de_folego():
                break

        for nome_personagem in self._ordem_de_iniciativa:
            for envolvido in self._envolvidos:
                if envolvido._nome == nome_personagem:
                    _realiza_um_turno(envolvido)

    @Separador_de_funcao
    def _valida_se_combate_foi_encerrado(self):

        for envolvido in self._envolvidos:
            print(f'''
            Turno {self._n_rodada}
            {envolvido._nome} 
            Pontos de vigor: {envolvido._checa_vigor()}
            Pontos de saude: {envolvido._checa_saude()}''')
            if envolvido._checa_saude() == 0 and envolvido._checa_vigor() == 0:
                print(f'{envolvido._nome} tombou! Combate encerrado!')
                self._combate_segue = False
                derrotado = envolvido._nome

                for vitorioso in self._envolvidos:
                    if vitorioso._nome != derrotado:
                        self._personagem_vitorioso = vitorioso._nome

                return
        print("Combate segue")
        self._combate_segue = True

    @Separador_de_funcao
    def _inicia_duelo(self):
        print('==================================================================================')
        print('Combate iniciado!')
        self._rola_iniciativa()
        while self._combate_segue:
            self._realiza_uma_rodada()
            self._n_rodada += 1
            self._valida_se_combate_foi_encerrado()
            print(self._combate_segue)
        else:
            print(f'Combate encerrado. {self._personagem_vitorioso} venceu')
        print('==================================================================================')
        return self._personagem_vitorioso

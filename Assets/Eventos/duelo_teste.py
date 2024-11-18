
from Assets.Eventos.duelo import duelo
from Assets.Criaturas.personagem import personagem


class testes:

    def __init__(self) -> None:
        pass

    def _testa_duelo_base(self):
        personagem_teste1 = personagem(
            nome='Testus',
            idade=30,
            ancestralidade='Humano',
            cultura='Alto Humano',
            passado={'familia': [1, 'Fé', 'Ageis e Longas'], 'infancia': [1, 1],
                     'adolecencia': [1, 'Atletismo', 'Ageis e Longas'], 'juventude': [1, 1, '-', 'herói', 1]},
            armas={'Mão direita': 'Espada Longa'},
            armaduras={})
        personagem_teste2 = personagem(
            nome='Testonix',
            idade=30,
            ancestralidade='Humano',
            cultura='Alto Humano',
            passado={'familia': [1, 'Fé', 'Ageis e Longas'], 'infancia': [1, 1],
                     'adolecencia': [1, 'Atletismo', 'Ageis e Longas'], 'juventude': [1, 1, '-', 'herói', 1]},
            armas={'Mão direita': 'Espada Longa'},
            armaduras={})
        personagem_teste1._inicializar_personagem()
        personagem_teste2._inicializar_personagem()
        duelo_base = duelo(envolvidos=[personagem_teste1, personagem_teste2])
        duelo_base._inicia_duelo()

    def _testa_duelo_em_massa(self, qtd):
        personagem_teste1 = personagem(
            nome='Testus',
            idade=30,
            ancestralidade='Humano',
            cultura='Alto Humano',
            passado={'familia': [1, 'Fé', 'Ageis e Longas'], 'infancia': [1, 1],
                     'adolecencia': [1, 'Atletismo', 'Ageis e Longas'], 'juventude': [1, 1, '-', 'herói', 1]},
            armas={'Mão direita': 'Espada Longa'},
            armaduras={})
        personagem_teste2 = personagem(
            nome='Testonix',
            idade=30,
            ancestralidade='Humano',
            cultura='Alto Humano',
            passado={'familia': [1, 'Fé', 'Ageis e Longas'], 'infancia': [1, 1],
                     'adolecencia': [1, 'Atletismo', 'Ageis e Longas'], 'juventude': [1, 1, '-', 'herói', 1]},
            armas={'Mão direita': 'Espada Longa'},
            armaduras={})
        personagem_teste1._inicializar_personagem()
        personagem_teste2._inicializar_personagem()

        vitorias = {
            personagem_teste1._nome: 0,
            personagem_teste2._nome: 0,
            'None': 0
        }
        duelo_base = duelo(
            envolvidos=[personagem_teste1, personagem_teste2])

        for count in range(0, qtd):
            vitorias[str(duelo_base._inicia_duelo())] += 1

        print(vitorias)


teste = testes()
# teste._testa_duelo_base()
qtd_testes = 100
teste._testa_duelo_em_massa(qtd_testes)

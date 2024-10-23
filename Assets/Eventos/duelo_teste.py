
from Assets.Eventos.duelo import duelo
from Assets.Criaturas.personagem import personagem


class testes:

    def __init__(self) -> None:
        pass

    def _testa_duelo_base(self):
        personagem_teste = personagem(
            nome='Testus',
            idade=30,
            ancestralidade='Humano',
            cultura='Alto Humano',
            passado={'familia': [1, 'Fé', 'Ageis e Longas'], 'infancia': [1, 1],
                     'adolecencia': [1, 'Atletismo', 'Ageis e Longas'], 'juventude': [1, 1, '-', 'herói', 2]},
            armas={'Mão direita': 'Espada Longa'},
            armaduras={})
        duelo_base = duelo(envolvidos=[personagem_teste, personagem_teste])
        duelo_base._inicia_duelo()


teste = testes()
teste._testa_duelo_base()

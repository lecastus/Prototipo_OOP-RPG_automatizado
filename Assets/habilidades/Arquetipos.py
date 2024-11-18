class arquetipo:

    def __init__(self) -> None:
        self._obj_arquetipos = {
            'herói': heroi()
        }


class heroi(arquetipo):

    _lista_habilidades = ['Esgrima refinada',
                          'Guarda do Dia e da Cauda (Tag e Nibenhut)']

    def __init__(self):
        # super().__init__()

        self._obj_habilidades = {
            'Esgrima refinada': {'habilidade': self.esgrima_refinada, 'efeito': 'ativo'},
            'Guarda do Dia e da Cauda (Tag e Nibenhut)': {'habilidade': self.tag_e_nibenhut, 'efeito': 'passivo'}
        }

    def esgrima_refinada():
        pass

    def tag_e_nibenhut(self, personagem):
        personagem._combate['rolagem_ataque'] += 1

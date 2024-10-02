class arquetipo:
    def __init__(self) -> None:
        _obj_arquetipos = {
            'heroi': heroi()
        }


class heroi(arquetipo):

    _lista_habilidades = ['Esgrima refinada',
                          'Guarda do Dia e da Cauda (Tag e Nibenhut)']

    _obj_habilidades = {
        'Esgrima refinada': {'habilidade': self.esgrima_refinada, 'efeito': 'ativo'},
        'Guarda do Dia e da Cauda (Tag e Nibenhut)': {'habilidade': self.tag_e_nibenhut, 'efeito': 'passivo'}
    }

    def __init__(self):
        super().__init__()

    def esgrima_refinada():
        pass

    def tag_e_nibenhut(personagem):
        personagem._combate['rolagem_ataque'] += 1

from config import *


class Flor(db.Entity):
    flor = Required(str)
    nomeCientifico = Required(str)
    genero = Required(str)
    epocaFloraçao = Required(str)
    nativa = Required(str)
    reino = Required(str)

    def __str__(self):
        return f'{self.flor}, {self.nomeCientifico}, {self.genero}, {self.epocaFloraçao}, {self.nativa}, {self.reino}'


db.bind(provider='sqlite', filename='person.db', create_db=True)
db.generate_mapping(create_tables=True)

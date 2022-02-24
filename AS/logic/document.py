class Document(object):

    def __init__(self, id_obras : int = 0, titulo: str = 'Titulo', autores : str = 'Autores', publico_datos : str = 'PublicoDatos' ,editorial : str = 'Editorial' ,numero_paginas : int = 0):
        self._id_obras= id_obras
        self._titulo = titulo
        self._autores = autores
        self._publico_datos = publico_datos
        self._editorial = editorial
        self._numero_paginas = numero_paginas 


    @property
    def id_obras(self) -> int:
        return self._id_obras

    @id_obras.setter
    def id_obras(self, id_obras: int):
        self._id_obras = id_obras

    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, titulo: str):
        self._titulo = titulo

    @property
    def autores(self) -> str:
        return self._autores

    @autores.setter
    def autores(self, autores: str):
        self._autores = autores

    @property
    def publico_datos(self) -> str:
        return self._publico_datos

    @publico_datos.setter
    def publico_datos(self, publico_datos: str):
        self._publico_datos = publico_datos

    @property
    def editorial(self) -> str:
        return self._editorial

    @editorial.setter
    def editorial(self, editorial: str):
        self._editorial = editorial

    @property
    def numero_paginas(self) -> int:
        return self._numero_paginas

    @numero_paginas.setter
    def numero_paginas(self, numero_paginas: int):
        self._numero_paginas = numero_paginas


    def __str__(self):
        return '( {0}, {1}, {2}, {3} , {4} , {5} )'.format(self.id_obras, self.titulo, self.autores, self.publico_datos, self.editorial, self.numero_paginas)

if __name__ == '__main__':
    carriazo = Document(

        id_obras = 0 ,
        titulo= "Titulo " ,
        authors = "Autores " ,
        publico_datos = "Publicacion de  datos" ,
        editorial = "Editorial " ,
        numero_paginas = "Numero de paginas " ,
    )
    print(carriazo)
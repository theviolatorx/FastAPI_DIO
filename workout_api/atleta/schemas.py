from typing import Annotated

from pydantic import Field, PositiveFloat

from workout_api.contrib.schemas import BaseSchema


class Atleta(BaseSchema):
    nome: Annotated[str, Field(
        description='Nome do Atleta', exemples='Clóvis', max_length=50)]
    cpf: Annotated[str, Field(
        description='CPF do Atleta', exemples='12345678910', max_length=11)]
    idade: Annotated[int, Field(description='Idade do Atleta', exemples=25)]
    Peso: Annotated[PositiveFloat, Field(
        description='Peso do Atleta', exemples=75.5)]
    Altura: Annotated[PositiveFloat, Field(
        description='Altura do Atleta', exemples=1.70)]
    Sexo: Annotated[str, Field(
        description='Sexo do Atleta', exemples='M', max_length=1)]

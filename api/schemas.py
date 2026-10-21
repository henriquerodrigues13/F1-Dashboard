from datetime import date, time
from pydantic import BaseModel

class circuito_schema(BaseModel):
    circuito_id: str
    nome_circuito: str
    localidade: str
    pais: str
    latitude: float
    longitude: float

class classificacao_construtora_schema(BaseModel):
    edicao: int
    posicao_final: int | None = None
    pontos: int
    vitorias: int
    id_construtora: str
    construtora: str

class construtor_schema(BaseModel):
    id_construtora: str
    name_construtora: str
    nacionalidade: str

class classificacao_corredor_schema(BaseModel):
    edicao: int
    posicao_final: int | None = None
    pontos: int
    vitorias: int
    id_construtora: str
    construtora: str

class corredor_schema(BaseModel):
    id_corredor: str
    nome_informado: str
    nome_familia: str
    data_nascimento: date | None = None
    nacionalidade: str | None = None
    numero: int | None = None
    codigo: int | None = None

class qualificacao_schema(BaseModel):
    edicao: int
    etapa: int
    id_corredor: str
    id_construtora: str
    posicao: int
    q1: str | None = None
    q2: str | None = None
    q3: str | None = None

class corrida_schema(BaseModel):
    edicao: int
    etapa: int
    nome_circuito: str
    id_circuito: str
    data_corrida: date
    horario: time | None = None

class resultado_schema(BaseModel):
    edicao: int
    etapa: int
    nome_corrida: str
    id_corredor: str
    nome_corredor: str
    id_construtora: str
    construtora: str
    posicao_largada: int
    posicao_final: int
    pontos: int
    voltas: int
    status: str
    tempo: time | None = None
    volta_mais_rapida : str | None = None
    classificacao_volta_mais_rapida: int | None = None
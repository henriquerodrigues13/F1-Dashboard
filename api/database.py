from sqlalchemy import Integer, String, Float, Date, Time
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import date, time


class Base(DeclarativeBase):
    pass

class circuito(Base):
    __tablename__ = 'circuito'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    circuito_id: Mapped[str] = mapped_column(String(15))
    nome_circuito: Mapped[str] = mapped_column(String(50))
    localidade: Mapped[str] = mapped_column(String(50))
    pais: Mapped[str] = mapped_column(String(20))
    latitude: Mapped[float] = mapped_column(Float)
    longitude: Mapped[float] = mapped_column(Float)

class classificacao_construtora(Base):
    __tablename__ = "classificacao_construtora"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    edicao: Mapped[int] = mapped_column(Integer)
    posicao_final: Mapped[int | None] = mapped_column(Integer)
    pontos: Mapped[int] = mapped_column(Integer)
    vitorias: Mapped[int] = mapped_column(Integer)
    id_construtora: Mapped[str] = mapped_column(String(50))
    construtora: Mapped[str] = mapped_column(String(50))

class construtora(Base):
    __tablename__ = "construtora"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_construtora: Mapped[str] = mapped_column(String(50))
    nome: Mapped[str] = mapped_column(String(50))
    nacionalidade: Mapped[str] = mapped_column(String(50))

class classificacao_corredor(Base):
    __tablename__ = "classificacao_corredor"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    edicao: Mapped[int] = mapped_column(Integer)
    posicao_final: Mapped[int | None] = mapped_column(Integer)
    pontos: Mapped[float] = mapped_column(Float)
    vitorias: Mapped[int] = mapped_column(Integer)
    id_corredor: Mapped[str] = mapped_column(String(50))
    construtora: Mapped[str] = mapped_column(String(50))

class corredor(Base):
    __tablename__ = "corredor"

    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    id_corredor: Mapped[str] = mapped_column(String(50))
    nome_informado: Mapped[str] = mapped_column(String(50))
    nome_de_familia: Mapped[str] = mapped_column(String(50))
    data_de_nascimento: Mapped[date | None] = mapped_column(Date)
    nacionalidade: Mapped[str| None] = mapped_column(String(50))
    numero: Mapped[int | None] = mapped_column(Integer)
    codigo: Mapped[int | None] = mapped_column(String(3))

class qualificacao(Base):
    __tablename__ = "qualificacao"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    edicao: Mapped[int] = mapped_column(Integer)
    etapa: Mapped[int] = mapped_column(Integer)
    id_corredor: Mapped[str] = mapped_column(String(50))
    id_construtora: Mapped[str] = mapped_column(String(50))
    posicao: Mapped[int] = mapped_column(Integer)
    Q1: Mapped[str | None] = mapped_column(String(50))
    Q2: Mapped[str | None] = mapped_column(String(50))
    Q3: Mapped[str | None] = mapped_column(String(50))

class corrida(Base):
    __tablename__ = "corrida"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    edicao: Mapped[int] = mapped_column(Integer)
    etapa: Mapped[int] = mapped_column(Integer)
    nome_da_corrida: Mapped[str] = mapped_column(String(50))
    id_do_circuito: Mapped[str] = mapped_column(String(50))
    data_da_corrida: Mapped[date | None] = mapped_column(Date)
    horario: Mapped[time | None] = mapped_column(Time)

class resultado(Base):
    __tablename__ = "resultado"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    edicao: Mapped[int] = mapped_column(Integer)
    etapa: Mapped[int] = mapped_column(Integer)
    nome_da_corrida: Mapped[str] = mapped_column(String(50))
    id_corredor: Mapped[str] = mapped_column(String(50))
    nome_do_corredor: Mapped[str] = mapped_column(String(50))
    id_construtora: Mapped[str] = mapped_column(String(50))
    construtora: Mapped[str] = mapped_column(String(50))
    posicao_de_largada: Mapped[int] = mapped_column(Integer)
    posicao_no_final: Mapped[int] = mapped_column(Integer)
    pontos: Mapped[float] = mapped_column(Float)
    voltas: Mapped[int] = mapped_column(Integer)
    status: Mapped[str] = mapped_column(String(20))
    tempo: Mapped[str | None] = mapped_column(String(30))
    volta_mais_rapida: Mapped[str | None] = mapped_column(String(20))
    classificacao_da_volta_mais_rapida: Mapped[int | None] = mapped_column(Integer)

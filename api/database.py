from sqlalchemy import Integer, String, Float, Date, Time
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import date, time


class Base(DeclarativeBase):
    pass

class circuito(Base):
    __tablename__ = 'circuito'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrent=True)
    circuito_id: Mapped[str] = mapped_column(String(15))
    nome_circuito: Mapped[str] = mapped_column(String(50))
    localidade: Mapped[str] = mapped_column(String(50))
    pais: Mapped[str] = mapped_column(String(20))
    latitude: Mapped[float] = mapped_column(Float)
    longitude: Mapped[float] = mapped_column(Float)

class classificacao_construtora(Base):
    __tablename__ = "classificacao_construtora"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrent=True)
    edicao: Mapped[int] = mapped_column(Integer)
    posicao_final: Mapped[int] = mapped_column(Integer)
    pontos: Mapped[int] = mapped_column(Integer)
    vitorias: Mapped[int] = mapped_column(Integer)
    id_construtora: Mapped[str] = mapped_column(String(15))
    construtora: Mapped[str] = mapped_column(String(15))

class construtora(Base):
    __tablename__ = "construtora"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrent=True)
    id_construtora: Mapped[str] = mapped_column(String(15))
    name_construtora: Mapped[str] = mapped_column(String(50))
    nacionalidade: Mapped[str] = mapped_column(String(50))

class classificacao_corredor(Base):
    __tablename__ = "classificacao_corredor"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrent=True)
    edicao: Mapped[int] = mapped_column(Integer)
    posicao_final: Mapped[int] = mapped_column(Integer)
    pontos: Mapped[int] = mapped_column(Integer)
    vitorias: Mapped[int] = mapped_column(Integer)
    id_corredor: Mapped[str] = mapped_column(String(15))
    construtora: Mapped[str] = mapped_column(String(15))

class corredor(Base):
    __tablename__ = "corredor"

    id : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrent=True)
    id_corredor: Mapped[str] = mapped_column(String(15))
    nome_informado: Mapped[str] = mapped_column(String(15))
    nome_familia: Mapped[str] = mapped_column(String(15))
    data_nascimento: Mapped[date] = mapped_column(Date)
    nacionalidade: Mapped[str] = mapped_column(String(15))
    numero: Mapped[int] = mapped_column(Integer)
    codigo: Mapped[int] = mapped_column(String(3))

class qualificacao(Base):
    __tablename__ = "qualificacao"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrent=True)
    edicao: Mapped[int] = mapped_column(Integer)
    etapa: Mapped[int] = mapped_column(Integer)
    id_corredor: Mapped[str] = mapped_column(String(15))
    id_construtora: Mapped[str] = mapped_column(String(15))
    posicao: Mapped[int] = mapped_column(Integer)
    q1: Mapped[str] = mapped_column(String(15))
    q2: Mapped[str] = mapped_column(String(15))
    q3: Mapped[str] = mapped_column(String(15))

class corrida(Base):
    __tablename__ = "corrida"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrent=True)
    edicao: Mapped[int] = mapped_column(Integer)
    etapa: Mapped[int] = mapped_column(Integer)
    id_corredor: Mapped[str] = mapped_column(String(15))
    id_construtora: Mapped[str] = mapped_column(String(15))
    data_corrida: Mapped[date] = mapped_column(Date)
    horario: Mapped[time] = mapped_column(Time)

class resultado(Base):
    __tablename__ = "resultado"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrent=True)
    edicao: Mapped[int] = mapped_column(Integer)
    etapa: Mapped[int] = mapped_column(Integer)
    nome_corrida: Mapped[str] = mapped_column(String(15))
    id_corredor: Mapped[str] = mapped_column(String(15))
    nome_corredor: Mapped[str] = mapped_column(String(15))
    id_construtora: Mapped[str] = mapped_column(String(15))
    construtora: Mapped[str] = mapped_column(String(15))
    posicao_largada: Mapped[int] = mapped_column(Integer)
    posicao_final: Mapped[int] = mapped_column(Integer)
    pontos: Mapped[int] = mapped_column(Integer)
    voltas: Mapped[int] = mapped_column(Integer)
    status: Mapped[str] = mapped_column(String(20))
    tempo: Mapped[time] = mapped_column(Time)
    volta_mais_rapida: Mapped[str] = mapped_column(String(20))
    classificacao_volta_mais_rapida: Mapped[int] = mapped_column(Integer)

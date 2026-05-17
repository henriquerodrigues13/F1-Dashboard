from sqlalchemy.schema import CreateSchema
from sqlalchemy import create_engine
from elt.config import DATABASE_URL, PROCESSED_DIR
from pathlib import Path
import pandas as pd


def transform_dataframe():
    engine = create_engine(DATABASE_URL)
    df_curcuito = pd.read_sql("SELECT * FROM raw.circuits", con=engine)
    df_curcuito.columns = ['circuito_id', 'nome_circuito', 'localidade', 'pais', 'latitude', 'longitude', 'url']
    df_curcuito.drop(columns=['url'], inplace=True)
    df_constructor_standings = pd.read_sql("SELECT * FROM raw.constructor_standings", con=engine)
    df_constructor_standings.columns = ['edicao', 'posicao_final', 'pontos', 'vitorias', 'id_construtora', 'construtora']
    df_constructors = pd.read_sql("SELECT * FROM raw.constructors", con=engine)
    df_constructors.columns =['id_construtora', 'nome','nacionalidade', 'url']
    df_constructors.drop(columns=['url'], inplace=True)
    df_driver_standings = pd.read_sql("SELECT * FROM raw.drivers_standings", con=engine)
    df_driver_standings.columns = ['edição', 'posicao', 'pontos','vitorias', 'id_corredor', 'construtora']
    df_driver_standings.dropna(subset=['posicao'], inplace=True)
    df_drivers = pd.read_sql("SELECT * FROM raw.drivers", con=engine)
    df_drivers.columns = ['id_corredor', 'nome_informado', 'nome_de_familia','data_de_nascimento','nacionalidade','numero','codigo','url']
    df_drivers.drop(columns=['url'], inplace=True)
    df_drivers['data_de_nascimento'] = pd.to_datetime(df_drivers['data_de_nascimento'], errors='coerce')
    df_qualifying = pd.read_sql("SELECT * FROM raw.qualifying", con=engine)
    df_qualifying.columns = ['edição', 'etapa', 'id_corredor', 'id_construtora', 'posição', 'Q1', 'Q2', 'Q3']
    df_race = pd.read_sql("SELECT * FROM raw.race", con=engine)
    df_race.columns = ['edicao', 'etapa', 'nome_da_corrida','id_do_circuito','data_da_corrida','horario', 'url']
    df_race.drop(columns=['url'], inplace=True)
    df_race['data_da_corrida'] = pd.to_datetime(df_race['data_da_corrida'])
    df_results = pd.read_sql("SELECT * FROM raw.results", con=engine)
    df_results.columns =  ['edicao', 'etapa', 'nome_da_corrida', 'id_corredor', 'nome_do_corredor', 'id_construtora',
                   'construtora', 'posicao_de_largada', 'posicao_no_final', 'pontos', 'voltas', 'status', 'tempo',
                   'volta_mais_rapida', 'classificacao_da_volta_mais_rapida']

    dados =  {"circuits": df_curcuito,
        "constructor_standings": df_constructor_standings,
        "constructors": df_constructors,
        "driver_standings": df_driver_standings,
        "drivers": df_drivers,
        "qualifying": df_qualifying,
        "races": df_race,
        "results": df_results
    }
    with engine.begin() as conn:
        conn.execute(CreateSchema("processed", if_not_exists=True))
    for name_table,dado in dados.items():
        dado.to_sql(name_table,con=engine,if_exists='replace',index=False,schema="processed")
    for name_parquet,dado in dados.items():
        dado.to_parquet(Path(PROCESSED_DIR) / f"{name_parquet}.parquet",index=False)
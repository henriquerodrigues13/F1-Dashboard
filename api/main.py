from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, select, func
from contextlib import asynccontextmanager
from elt.config import DATABASE_URL
from sqlalchemy.orm import Session
from api.database import *
from fastapi import FastAPI
from api import rotas

import logging

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(title="API_F1-Dashboard", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["X-Total-Items", "X-Total-Pages"],
)

app.include_router(rotas.router)

engine = create_engine(DATABASE_URL)

def init_db():
    from pathlib import Path
    import os
    import pandas as pd


    logging.basicConfig(level=logging.INFO, format="%(asctime)s — %(message)s")
    logging.info("iniciando db")
    Base.metadata.create_all(bind=engine)
    logging.info("metadata criada")
    caminho = Path(__file__).parent.parent / "data" / "processed"
    mapa_tabelas = {"circuits.parquet" : "cirtuito",
     "constructors.parquet": "construtora",
     "constructor_standings.parquet": "classificacao_construtora",
     "drivers.parquet": "corredor",
     "driver_standings.parquet": "classificacao_corredor",
     "qualifying.parquet": "qualificacao",
     "races.parquet": "corrida",
     "results.parquet": "resultado"
     }
    tabelas = {"cirtuito" : circuito,
     "construtora": construtora,
     "classificacao_construtora": classificacao_construtora,
     "corredor": corredor,
     "classificacao_corredor": classificacao_corredor,
     "qualificacao": qualificacao,
     "corrida": corrida,
     "resultado": resultado
     }
    with Session(engine) as session:
        for file in os.listdir(caminho):

            total = session.scalar(select(func.count().select_from(tabelas[mapa_tabelas[file]])))

            if total != 0:
                logging.info(f"tabela: {mapa_tabelas[file]} já está populada")
                continue

            df = pd.read_parquet(caminho / file)
            df.to_sql(
                name=mapa_tabelas[file],
                con=engine,
                if_exists="append",
                index=False,
                chunksize=500,
            )
            logging.info(f"tabela: {mapa_tabelas[file]} foi adicionada com sucesso")
        logging.info("init db finalizado")
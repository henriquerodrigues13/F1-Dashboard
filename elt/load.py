from sqlalchemy.schema import CreateSchema
from elt.extract import load_dataframe
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

def load():
    engine = create_engine(os.getenv("DATABASE_URL"))
    dados = load_dataframe()
    with engine.begin() as conn:
        conn.execute(CreateSchema("raw", if_not_exists=True))
    for name_table,dado in dados.items():
        dado.to_sql(name_table,con=engine,if_exists='replace',index=False,schema="raw")

from sqlalchemy.schema import CreateSchema
from elt.config import DATABASE_URL
from elt.extract import load_dataframe
from sqlalchemy import create_engine


def load():
    engine = create_engine(DATABASE_URL)
    dados = load_dataframe()
    with engine.begin() as conn:
        conn.execute(CreateSchema("raw", if_not_exists=True))
    for name_table,dado in dados.items():
        dado.to_sql(name_table,con=engine,if_exists='replace',index=False,schema="raw")

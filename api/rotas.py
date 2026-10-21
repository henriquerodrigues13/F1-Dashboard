from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine, select
from elt.config import DATABASE_URL
from api.database import *
from api.schemas import *
from typing import Annotated
import logging

logging.basicConfig(level=logging.INFO)


def sessao_DB():
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(tags=["rotas para tabelas F1"])
SessionDep = Annotated[Session, Depends(sessao_DB)]

@router.get('/get_circuito/', response_model=list[circuito_schema])
async def get_produtos_usuario(session: SessionDep) -> list[circuito_schema]:

    circuitos = session.execute(select(circuito)).scalars().all()

    logging.info("consulta de circuitos")
    return circuitos
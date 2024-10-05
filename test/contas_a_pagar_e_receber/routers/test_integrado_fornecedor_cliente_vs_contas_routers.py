from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from main import app
from shared.database import Base
from shared.dependencies import get_db

client = TestClient(app)


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


def test_deve_listar_contas_de_um_fornecedor_cliente():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    client.post("/fornecedor-cliente", json={'nome': 'casa da musica'})
    client.post("/fornecedor-cliente", json={'nome': 'treinamentos'})

    client.post("/contas-a-pagar-e-receber", json={
    'descricao': 'curso de python', 
    'valor'    :  1000.5,
    'tipo'     : 'PAGAR',
    'fornecedor_cliente_id':2
    })
    
    client.post("/contas-a-pagar-e-receber", json={
    'descricao': 'curso de guitarra',
    'valor'    : 1000.5, 
    'tipo'     :'PAGAR',
    'fornecedor_cliente_id':1
    })

    client.post("/contas-a-pagar-e-receber", json={
    'descricao': 'curso de baixo',
    'valor'    : 6000.5, 
    'tipo'     :'PAGAR',
    'fornecedor_cliente_id':1
    })




    response_get_fornecedor_1 = client.get(f"/fornecedor-cliente/1/contas-a-pagar-e-receber")

    assert response_get_fornecedor_1.status_code == 200
    assert len(response_get_fornecedor_1.json()) == 2


    response_get_fornecedor_2 = client.get(f"/fornecedor-cliente/2/contas-a-pagar-e-receber")

    assert response_get_fornecedor_2.status_code == 200
    assert len(response_get_fornecedor_2.json()) == 1










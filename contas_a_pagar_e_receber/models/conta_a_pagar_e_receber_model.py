from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, DateTime, Boolean
from shared.database import Base
from sqlalchemy.orm import relationship




class ContaPagarReceber(Base):
    __tablename__='contas_a_pagar_e_receber'

    id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String(30))
    valor = Column(Numeric)
    tipo = Column(String(30))
    data_da_baixa  = Column(DateTime())
    valor_da_baixa = Column(Numeric())
    esta_baixada = Column(Boolean, default = False)

    fornecedor_cliente_id = Column(Integer, ForeignKey("fornecedor_cliente.id"))
    fornecedor = relationship("FornecedorCliente")
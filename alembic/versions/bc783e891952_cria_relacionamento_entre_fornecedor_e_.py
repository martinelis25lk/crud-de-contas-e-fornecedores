"""cria relacionamento entre fornecedor e conta

Revision ID: bc783e891952
Revises: 3a8224b4e3f2
Create Date: 2024-09-28 13:14:22.329300

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc783e891952'
down_revision = '3a8224b4e3f2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contas_a_pagar_e_receber', sa.Column('fornecedor_cliente_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'contas_a_pagar_e_receber', 'fornecedor_cliente', ['fornecedor_cliente_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'contas_a_pagar_e_receber', type_='foreignkey')
    op.drop_column('contas_a_pagar_e_receber', 'fornecedor_cliente_id')
    # ### end Alembic commands ###

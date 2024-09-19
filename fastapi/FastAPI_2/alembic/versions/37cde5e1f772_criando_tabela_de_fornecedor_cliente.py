"""Criando tabela de fornecedor cliente

Revision ID: 37cde5e1f772
Revises: d85c9cb0644c
Create Date: 2024-09-16 10:07:03.829636

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '37cde5e1f772'
down_revision: Union[str, None] = 'd85c9cb0644c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fornecedor_cliente',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fornecedor_cliente')
    # ### end Alembic commands ###
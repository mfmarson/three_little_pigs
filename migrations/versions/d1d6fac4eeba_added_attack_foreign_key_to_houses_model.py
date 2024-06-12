"""Added attack foreign key to houses model.

Revision ID: d1d6fac4eeba
Revises: 5b7e70cfd5ac
Create Date: 2024-06-12 11:03:20.003488

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd1d6fac4eeba'
down_revision: Union[str, None] = '5b7e70cfd5ac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('houses', sa.Column('attack_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'houses', 'attacks', ['attack_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'houses', type_='foreignkey')
    op.drop_column('houses', 'attack_id')
    # ### end Alembic commands ###

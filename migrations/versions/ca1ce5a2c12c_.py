"""empty message

Revision ID: ca1ce5a2c12c
Revises: b0cfbd289b38
Create Date: 2020-03-25 21:50:27.890157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca1ce5a2c12c'
down_revision = 'b0cfbd289b38'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'options', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'options', type_='unique')
    # ### end Alembic commands ###

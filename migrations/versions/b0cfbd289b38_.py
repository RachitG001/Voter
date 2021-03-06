"""empty message

Revision ID: b0cfbd289b38
Revises: c7d364380ddc
Create Date: 2020-03-25 20:15:43.745824

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0cfbd289b38'
down_revision = 'c7d364380ddc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('polls', 'status')
    op.add_column('topics', sa.Column('status', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('topics', 'status')
    op.add_column('polls', sa.Column('status', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###

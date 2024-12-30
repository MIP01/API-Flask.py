"""empty message

Revision ID: c479289dd4e9
Revises: bfbac6c91c51
Create Date: 2024-12-24 17:11:02.675529

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c479289dd4e9'
down_revision = 'bfbac6c91c51'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('_email', sa.String(length=150), nullable=False))
        batch_op.add_column(sa.Column('no_telp', sa.String(length=18), nullable=False))
        batch_op.create_unique_constraint(None, ['_email'])
        batch_op.create_unique_constraint(None, ['no_telp'])
        batch_op.drop_column('_alamat')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('_alamat', mysql.VARCHAR(length=150), nullable=False))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('no_telp')
        batch_op.drop_column('_email')

    # ### end Alembic commands ###

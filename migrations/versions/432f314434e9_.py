"""empty message

Revision ID: 432f314434e9
Revises: 46a941e213f9
Create Date: 2019-10-29 20:21:05.878124

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '432f314434e9'
down_revision = '46a941e213f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'lastname',
               existing_type=mysql.VARCHAR(length=120),
               nullable=True)
    op.drop_index('firstname', table_name='users')
    op.drop_index('lastname', table_name='users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('lastname', 'users', ['lastname'], unique=True)
    op.create_index('firstname', 'users', ['firstname'], unique=True)
    op.alter_column('users', 'lastname',
               existing_type=mysql.VARCHAR(length=120),
               nullable=False)
    # ### end Alembic commands ###
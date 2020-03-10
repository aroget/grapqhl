"""remove avtar_url to user model

Revision ID: 1b58e80e1e24
Revises: 3b2433effc63
Create Date: 2020-03-04 07:43:04.892750

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1b58e80e1e24'
down_revision = '3b2433effc63'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar_url')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar_url', mysql.VARCHAR(length=80), nullable=True))
    # ### end Alembic commands ###

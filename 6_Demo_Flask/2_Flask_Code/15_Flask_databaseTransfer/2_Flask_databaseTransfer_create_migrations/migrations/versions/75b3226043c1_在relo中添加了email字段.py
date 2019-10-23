"""'在Relo中添加了email字段'

Revision ID: 75b3226043c1
Revises: dde092937cb7
Create Date: 2019-07-31 11:59:15.217860

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75b3226043c1'
down_revision = 'dde092937cb7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('email', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('roles', 'email')
    # ### end Alembic commands ###

""" added user phone number

Revision ID: 232d45cc77c4
Revises: 398b2025d3cf
Create Date: 2024-09-30 09:59:34.364750

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '232d45cc77c4'
down_revision = '398b2025d3cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_phone', sa.String(length=15), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('user_phone')

    # ### end Alembic commands ###
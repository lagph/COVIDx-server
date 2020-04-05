"""empty message

Revision ID: 5af7ff828b91
Revises: 4cb4de8935b7
Create Date: 2020-04-05 14:50:49.230138

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5af7ff828b91'
down_revision = '4cb4de8935b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('role_id', sa.String(length=50), nullable=False))
    op.drop_index('id', table_name='roles')
    op.create_unique_constraint(None, 'roles', ['role_id'])
    op.drop_column('roles', 'id')
    op.add_column('users', sa.Column('user_id', sa.String(length=50), nullable=True))
    op.drop_index('id', table_name='users')
    op.create_unique_constraint(None, 'users', ['user_id'])
    op.drop_column('users', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False))
    op.drop_constraint(None, 'users', type_='unique')
    op.create_index('id', 'users', ['id'], unique=True)
    op.drop_column('users', 'user_id')
    op.add_column('roles', sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False))
    op.drop_constraint(None, 'roles', type_='unique')
    op.create_index('id', 'roles', ['id'], unique=True)
    op.drop_column('roles', 'role_id')
    # ### end Alembic commands ###
"""empty message

Revision ID: 72576a9e6e4e
Revises: 04934123a63a
Create Date: 2020-04-04 20:30:40.037788

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72576a9e6e4e'
down_revision = '04934123a63a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_roles_name', table_name='roles')
    op.create_index(op.f('ix_roles_name'), 'roles', ['name'], unique=False)
    op.drop_index('ix_users_name', table_name='users')
    op.create_index(op.f('ix_users_name'), 'users', ['name'], unique=False)
    op.create_unique_constraint(None, 'users', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_index(op.f('ix_users_name'), table_name='users')
    op.create_index('ix_users_name', 'users', ['name'], unique=True)
    op.drop_index(op.f('ix_roles_name'), table_name='roles')
    op.create_index('ix_roles_name', 'roles', ['name'], unique=True)
    # ### end Alembic commands ###

"""empty message

Revision ID: 0c08f73fe69c
Revises: b5e44244e137
Create Date: 2023-02-19 04:59:45.597050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c08f73fe69c'
down_revision = 'b5e44244e137'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('marks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('likes', sa.Integer(), nullable=False),
    sa.Column('imgs_refs', sa.PickleType(), nullable=False),
    sa.Column('longitude', sa.String(), nullable=False),
    sa.Column('latitude', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('likes', sa.Integer(), nullable=False),
    sa.Column('imgs_refs', sa.PickleType(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('travel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fio', sa.String(), nullable=False),
    sa.Column('guest_count', sa.String(), nullable=False),
    sa.Column('entry', sa.String(), nullable=False),
    sa.Column('depart', sa.String(), nullable=False),
    sa.Column('phone_number', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('status', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('travel')
    op.drop_table('review')
    op.drop_table('marks')
    # ### end Alembic commands ###

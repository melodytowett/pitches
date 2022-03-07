"""secret key migration

Revision ID: 5e8336f585b6
Revises: 116516b2f5eb
Create Date: 2022-03-07 11:17:12.142374

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e8336f585b6'
down_revision = '116516b2f5eb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('pitches', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'pitches', 'users', ['user_id'], ['id'])
    op.drop_column('pitches', 'upvote')
    op.drop_column('pitches', 'downvote')
    op.drop_constraint('users_role_id_fkey', 'users', type_='foreignkey')
    op.drop_column('users', 'role_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('role_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('users_role_id_fkey', 'users', 'pitches', ['role_id'], ['id'])
    op.add_column('pitches', sa.Column('downvote', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('pitches', sa.Column('upvote', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    op.drop_column('pitches', 'user_id')
    op.drop_table('comments')
    # ### end Alembic commands ###

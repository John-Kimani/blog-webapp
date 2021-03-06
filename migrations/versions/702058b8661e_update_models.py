"""Update models

Revision ID: 702058b8661e
Revises: 3fda6fa1975c
Create Date: 2022-03-14 08:26:00.978743

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '702058b8661e'
down_revision = '3fda6fa1975c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('Comments_blog_id_fkey', 'Comments', type_='foreignkey')
    op.drop_column('Comments', 'blog_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Comments', sa.Column('blog_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('Comments_blog_id_fkey', 'Comments', 'blogs', ['blog_id'], ['id'])
    # ### end Alembic commands ###

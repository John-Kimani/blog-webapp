"""update

Revision ID: 2522194fe5e0
Revises: 5cfa7e97c7cb
Create Date: 2022-03-16 00:05:51.667015

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2522194fe5e0'
down_revision = '5cfa7e97c7cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('blog_title', sa.String(length=25), nullable=True),
    sa.Column('blog_post', sa.String(length=300), nullable=True),
    sa.Column('admin_id', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['admin_id'], ['admin.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_blog_timestamp'), 'blog', ['timestamp'], unique=False)
    op.drop_index('ix_blogs_timestamp', table_name='blogs')
    op.drop_table('blogs')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blogs',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('blog_title', sa.VARCHAR(length=25), autoincrement=False, nullable=True),
    sa.Column('blog_post', sa.VARCHAR(length=140), autoincrement=False, nullable=True),
    sa.Column('admin_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['admin_id'], ['admin.id'], name='blogs_admin_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='blogs_pkey')
    )
    op.create_index('ix_blogs_timestamp', 'blogs', ['timestamp'], unique=False)
    op.drop_index(op.f('ix_blog_timestamp'), table_name='blog')
    op.drop_table('blog')
    # ### end Alembic commands ###

"""empty message
Revision ID: 67c8796321c3
Revises: 
Create Date: 2022-09-01 23:35:35.511789
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67c8796321c3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=46), nullable=True),
    sa.Column('short_name', sa.String(length=46), nullable=True),
    sa.Column('slug', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('short_name'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('chat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.String(length=140), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('knot',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('f_name', sa.String(length=32), nullable=True),
    sa.Column('s_name', sa.String(length=32), nullable=True),
    sa.Column('username', sa.String(length=32), nullable=True),
    sa.Column('email', sa.String(length=129), nullable=True),
    sa.Column('phone_number', sa.String(length=15), nullable=True),
    sa.Column('password', sa.String(length=256), nullable=True),
    sa.Column('slug', sa.String(length=140), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.Column('authenticated', sa.Boolean(), nullable=True),
    sa.Column('auth_key', sa.String(length=256), nullable=True),
    sa.Column('auth_key_create', sa.DateTime(), nullable=True),
    sa.Column('admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone_number'),
    sa.UniqueConstraint('slug'),
    sa.UniqueConstraint('username')
    )
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=46), nullable=True),
    sa.Column('slug', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('chat_users',
    sa.Column('chat_id', sa.Integer(), nullable=False),
    sa.Column('knot_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['chat_id'], ['chat.id'], ),
    sa.ForeignKeyConstraint(['knot_id'], ['knot.id'], ),
    sa.PrimaryKeyConstraint('chat_id', 'knot_id'),
    sa.UniqueConstraint('chat_id', 'knot_id', name='chat_user_id')
    )
    op.create_table('message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.String(length=140), nullable=True),
    sa.Column('text', sa.String(length=5000), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('edited', sa.DateTime(), nullable=True),
    sa.Column('is_read', sa.Boolean(), nullable=True),
    sa.Column('author_username', sa.String(length=32), nullable=True),
    sa.ForeignKeyConstraint(['author_username'], ['knot.username'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.String(length=140), nullable=True),
    sa.Column('slug', sa.String(length=140), nullable=True),
    sa.Column('title', sa.String(length=78), nullable=True),
    sa.Column('preview', sa.String(length=250), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('author', sa.String(length=32), nullable=True),
    sa.Column('visible', sa.Boolean(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('chat_msgs',
    sa.Column('chat_id', sa.Integer(), nullable=False),
    sa.Column('message_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['chat_id'], ['chat.id'], ),
    sa.ForeignKeyConstraint(['message_id'], ['message.id'], ),
    sa.PrimaryKeyConstraint('chat_id', 'message_id'),
    sa.UniqueConstraint('chat_id', 'message_id', name='chat_msg_id')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.String(length=140), nullable=True),
    sa.Column('text', sa.String(length=2000), nullable=True),
    sa.Column('slug', sa.String(length=140), nullable=True),
    sa.Column('author', sa.String(length=32), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('edited', sa.DateTime(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['post.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('post_tags',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], ),
    sa.PrimaryKeyConstraint('post_id', 'tag_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_tags')
    op.drop_table('comment')
    op.drop_table('chat_msgs')
    op.drop_table('post')
    op.drop_table('message')
    op.drop_table('chat_users')
    op.drop_table('tag')
    op.drop_table('knot')
    op.drop_table('chat')
    op.drop_table('category')
    # ### end Alembic commands ###

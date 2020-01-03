"""empty message

Revision ID: 4dad771f1a87
Revises: 530e5c647af6
Create Date: 2019-12-14 20:45:37.008238

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4dad771f1a87'
down_revision = '530e5c647af6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post_knot',
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('knot_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['knot_id'], ['knot.id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_knot')
    # ### end Alembic commands ###

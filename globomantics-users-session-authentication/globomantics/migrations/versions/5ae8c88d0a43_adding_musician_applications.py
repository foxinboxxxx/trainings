"""Adding musician applications

Revision ID: 5ae8c88d0a43
Revises: 2cc56941ea99
Create Date: 2024-02-17 15:48:09.524467

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ae8c88d0a43'
down_revision = '2cc56941ea99'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('applications',
    sa.Column('gig_id', sa.Integer(), nullable=True),
    sa.Column('musician_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['gig_id'], ['gigs.id'], ),
    sa.ForeignKeyConstraint(['musician_id'], ['users.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('applications')
    # ### end Alembic commands ###

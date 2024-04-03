"""Create examples table and columns

Revision ID: f421f169bac4
Revises: 
Create Date: 2024-04-03 09:42:27.795266

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f421f169bac4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('examples',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('columnname', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('examples')
    # ### end Alembic commands ###

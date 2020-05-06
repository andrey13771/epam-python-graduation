"""departments and employees tables

Revision ID: 3ae0d7825688
Revises: 
Create Date: 2020-04-29 23:41:13.990112

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ae0d7825688'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_department_title'), 'department', ['title'], unique=True)
    op.create_table('employee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('dob', sa.Date(), nullable=True),
    sa.Column('salary', sa.Integer(), nullable=True),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['department.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_employee_dob'), 'employee', ['dob'], unique=False)
    op.create_index(op.f('ix_employee_name'), 'employee', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_employee_name'), table_name='employee')
    op.drop_index(op.f('ix_employee_dob'), table_name='employee')
    op.drop_table('employee')
    op.drop_index(op.f('ix_department_title'), table_name='department')
    op.drop_table('department')
    # ### end Alembic commands ###
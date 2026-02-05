from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String 
from sqlalchemy import ForeignKey
metadata_obj = MetaData()
Task = Table(
    "user_task",
    metadata_obj,
    Column("task_id", Integer, primary_key=True),
    Column("task_title", String(100), nullable=False),
    Column("task_status", String(20), nullable=False),
)

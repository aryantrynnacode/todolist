from sqlalchemy import insert, select, update, delete
from database import engine
from models import Task

 
def add_task(task_title):
    
    stmt = insert(Task).values(
        task_title = task_title,
        task_status = "pending"
    ) 
    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()

def get_task():
    
    stmt = select(Task)
    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()


def delete_task(task_id):

    stmt = delete(Task).where(Task.c.task_id == task_id)
    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()


def update_task(task_id, new_title=None, new_status=None ):
    stmt = update(Task).where(Task.c.task_id == task_id)
    values = {}
    if new_title:
        values["task_title"] = new_title
    if new_status:
        values["task_status"] = new_status
    
    stmt = stmt.values(**values)

    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()
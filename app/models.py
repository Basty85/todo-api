from sqlalchemy import Table, Column, Integer, String, Boolean
from app.db import metadata

todos = Table(
    "todos",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
    Column("done", Boolean, default=False)
)
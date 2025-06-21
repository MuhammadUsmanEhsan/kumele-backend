from sqlalchemy import Table, Column, Integer, String
from app.database import metadata

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, unique=True, index=True),
    Column("email", String, unique=True, index=True),
    Column("hashed_password", String),
)

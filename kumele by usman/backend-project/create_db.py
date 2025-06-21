from app.db.base import Base
from app.db.session import engine
from app.models.user import User
from app.database import engine, Base
from app import models

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Done!")

Base.metadata.create_all(bind=engine)

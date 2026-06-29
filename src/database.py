from sqlalchemy import create_engine, text
from src.config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

try:
    engine = create_engine(DATABASE_URL)

    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("Database connection successful!")

except Exception as e:
    print(f"Error connecting to the database: {e}")



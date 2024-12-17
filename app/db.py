from sqlmodel import create_engine, Session

# Corrected database URL
database_url = "mysql+pymysql://root:root@127.0.0.1/test"

# Create the engine
engine = create_engine(database_url)

# Dependency for getting the database session
def get_db():
    with Session(engine) as session:
        yield session

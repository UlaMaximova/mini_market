from database import engine

from models import Base


def create_tables():
    try:
        Base.metadata.create_all(bind=engine)
        print('Successfully created tables')
        
    except Exception as error:
        print(f'Error creating tables: ${error}')

if __name__ == "__main__":
    create_tables()

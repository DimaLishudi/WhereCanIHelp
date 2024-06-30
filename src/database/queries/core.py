from sqlalchemy import text, insert, select, text, update
from database import engine, session_factory
from WhereCanIHelp.src.database.models_orm import metadata_obj, Organization

def create_tables():
    engine.echo = False
    metadata_obj.drop_all(engine)
    metadata_obj.create_all(engine)
    #engine.echo = True

def insert_data():
    with session_factory() as session:
        org1 = Organization(name="Non-Profit1", phone = "5554321")
        org2 = Organization(name="Non-Profit2", phone = "5551234")
        session.add_all([org1, org2])
        session.commit()



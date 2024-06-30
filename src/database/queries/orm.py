from sqlalchemy import Integer, and_, cast, func, insert, inspect, or_, select, text
from sqlalchemy.orm import aliased, contains_eager, joinedload, selectinload

from database import Base, session_factory, engine
from models_orm import Organization, Helptype, OrgNeeds, User, Actions

class SyncORM:
    @staticmethod
    def create_tables():
        engine.echo = False
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        engine.echo = True

    @staticmethod
    def insert_org(name, address="", phone="", website=""):
        with session_factory() as session:
            session.expire_on_commit = False
            org = Organization(name=name, address=address, phone=phone, website=website)
            session.add(org)
            session.flush()
            session.commit()
            session.expunge(org)
            return org

    @staticmethod
    def get_org_by_id(id):
        with session_factory() as session:
            org = session.get(Organization, id)
            session.expunge_all()
            return org

    @staticmethod
    def update_org(id, name, address, phone, website):
        with session_factory() as session:
            org = session.get(Organization, id)
            session.commit()
    
    @staticmethod
    def select_organizations():
        with session_factory() as session:
            query = select(Organization)
            result = session.execute(query)
            organizations = result.scalars().all()
            print(f"{organizations=}")

    @staticmethod
    def insert_needs(name):
        with session_factory() as session:
            session.expire_on_commit = False
            need = Helptype()
            need.name = name
            session.add(need)
            session.flush()
            session.commit()
            session.expunge(need)
            return need

    @staticmethod
    def insert_org_need(org:Organization, need:Helptype):
        with session_factory() as session:
            session.expire_on_commit = False
            new_need = OrgNeeds()
            new_need.organization = org
            new_need.help_type_id = need.id
            new_need.amount = 0
            new_need.description = ""

            session.add(new_need)
            session.commit()


def update_organization(organization_id: int = 2, new_username: str = "Misha"):
    with session_factory() as session:
        worker_michael = session.get(Organization, organization_id)
        worker_michael.name = new_username
        session.refresh(worker_michael)
        session.commit()

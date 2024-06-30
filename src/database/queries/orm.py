from datetime import date
from sqlalchemy import Integer, and_, cast, func, insert, inspect, or_, select, text
from sqlalchemy.orm import aliased, contains_eager, joinedload, selectinload

from database import Base, session_factory, engine
from models_orm import Organization, Helptype, OrgNeeds, User, UserСapability, Actions

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

    @staticmethod
    def insert_user(name, phone, email=""):
        with session_factory() as session:
            session.expire_on_commit = False
            new_user = User()
            new_user.name = name
            new_user.phone = phone
            new_user.email = email
            session.add(new_user)
            session.flush()
            session.commit()
            session.expunge(new_user)
            return new_user
        
    @staticmethod
    def add_user_capability(user:User, helptype:Helptype, amount=1, description=""):
        with session_factory() as session:
            session.expire_on_commit = False
            new_cap = UserСapability()
            new_cap.user_id = user.id
            new_cap.help_type_id = helptype.id
            new_cap.description = description
            new_cap.amount = amount
            session.add(new_cap)
            session.commit()



    @staticmethod
    def insert_action(user:User, org:Organization, need:Helptype, amount=1, action_date=date.today(), descsription=""):
        with session_factory() as session:
            session.expire_on_commit = False
            new_action = Actions()
            new_action.organization_id = org.id
            new_action.user_id = user.id
            new_action.help_type_id = need.id
            new_action.amount = amount
            new_action.action_date = action_date
            new_action.description = descsription
            session.add(new_action)
            session.flush()
            session.commit()
            session.expunge(new_action)
            return new_action
    
    @staticmethod
    def get_user_actions(user):
        with session_factory() as session:
            query = select(Actions).where(Actions.user_id == user.id)
            result = session.execute(query)
            actions = result.scalars().all()
            return actions
        
    @staticmethod
    def get_user_by_id(id):
        with session_factory() as session:
            session.expire_on_commit = False
            user = session.get(User, id)
            session.expunge_all()
            return user

    


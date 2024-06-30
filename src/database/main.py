from queries.orm import SyncORM

SyncORM.create_tables()

org1 = SyncORM.insert_org(name="Helping Hands", phone="555-1234")
org2 = SyncORM.insert_org(name="Community Care", phone="555-5678")
org3 = SyncORM.insert_org(name="Bright Future", phone="555-9101")
org4 = SyncORM.insert_org(name="Hope Foundation", phone="555-1122")
org5 = SyncORM.insert_org(name="Unity Volunteers", phone="555-3344")
org6 = SyncORM.insert_org(name="Peaceful World", phone="555-5566")
org7 = SyncORM.insert_org(name="Green Earth", phone="555-7788")
org8 = SyncORM.insert_org(name="Happy Hearts", phone="555-9900")
org9 = SyncORM.insert_org(name="Lending Hands", phone="555-2233")
org10 = SyncORM.insert_org(name="Sunny Days", phone="555-4455")

need1 = SyncORM.insert_needs(name="Money")
need2 = SyncORM.insert_needs(name="Food")
need3 = SyncORM.insert_needs(name="Clothes")
need4 = SyncORM.insert_needs(name="Volunteers")
need5 = SyncORM.insert_needs(name="Medical Supplies")
need6 = SyncORM.insert_needs(name="Educational Materials")
need7 = SyncORM.insert_needs(name="Transportation")
need8 = SyncORM.insert_needs(name="Office Supplies")
need9 = SyncORM.insert_needs(name="Cleaning Supplies")
need10 = SyncORM.insert_needs(name="Event Space")

# SyncORM.insert_org_need(org1, need1)
# SyncORM.insert_org_need(org1, need2)
# SyncORM.insert_org_need(org1, need3)
# SyncORM.insert_org_need(org1, need4)
# SyncORM.insert_org_need(org2, need5)
# SyncORM.insert_org_need(org2, need6)
# SyncORM.insert_org_need(org2, need7)
# SyncORM.insert_org_need(org2, need8)


org = SyncORM.get_org_by_id(5)
print(org)


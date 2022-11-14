from sqlalchemy import MetaData, Table, String, ForeignKey, Integer, Column, Text, DateTime, Boolean
metadata = MetaData()
USERS = Table('Users', metadata,
              Column('userId', Integer(), primary_key=True),
              Column('age', Integer(), nullable=False),
              )

PURCHASES = Table('Purchases', metadata,
                  Column('purchaseId', Integer(), primary_key=True),
                  Column('userId', ForeignKey("Users.userId")),
                  Column('itemId', ForeignKey("Items.itemId")),
                  Column('date', DateTime(), nullable=False)
                  )

ITEMS = Table('Items', metadata,
              Column('itemId', Integer(), primary_key=True),
              Column('price', Integer(), nullable=False))
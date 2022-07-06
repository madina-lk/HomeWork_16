from models import *
from config.config import *
from config.utils import *

db.drop_all()
db.create_all()

# загрузка из json
users_data = load_json(USERS_DATA_PATH)
orders_data = load_json(ORDERS_DATA_PATH)
offers_data = load_json(OFFERS_DATA_PATH)

# заполнение таблиц
for user_data in users_data:
    users = [UserModel(**user_data)]
    db.session.add_all(users)

for order_data in orders_data:
    orders = [OrderModel(**order_data)]
    db.session.add_all(orders)

for offer_data in offers_data:
    offers = [OfferModel(**offer_data)]
    db.session.add_all(offers)

# сохранение данных в базе
db.session.commit()
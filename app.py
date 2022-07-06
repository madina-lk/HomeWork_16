from flask import Flask, request, jsonify
from models import *
from config.utils import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.app_context().push()


@app.route("/users", methods=['GET', "POST"])
def get_all_users():
    """
    Представление для пользователей, которое обрабатывает
    GET-запросы получения всех пользователей,
    а также создание пользователя user посредством метода POST
    """
    result = []
    if request.method == 'GET':
        users = UserModel.query.all()
        for user in users:
            result.append(instance_to_dict_user(user))
        return jsonify(result)
    if request.method == "POST":
        user = json.loads(request.data)
        new_user = UserModel(
            id=user['id'],
            first_name=user['first_name'],
            last_name=user['last_name'],
            age=user['age'],
            email=user['email'],
            role=user['role'],
            phone=user['phone']
        )
        db.session.add(new_user)
        db.session.commit()
        db.session.close()
        return "Добавлена новая запись"


@app.route("/users/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def get_one_user(id):
    """
    получение одного пользователя по идентификатору,
    обновление пользователя user посредством метода PUT ,
    удаление пользователя user посредством метода DELETE
    """
    if request.method == 'GET':
        user = UserModel.query.get(id)
        if user is None:
            return 'не найдено поле с таким ид'
        else:
            return jsonify(instance_to_dict_user(user))

    elif request.method == 'PUT':
        user_data = json.loads(request.data)
        user = UserModel.query.get(id)
        # user = db.session.query(UserModel).get(gid)
        if user is None:
            return 'не найдено поле с таким ид'
        else:
            user.first_name = user_data['first_name']
            user.last_name = user_data['last_name']
            user.age = user_data['age']
            user.email = user_data['email']
            user.role = user_data['role']
            user.phone = user_data['phone']
            db.session.add(user)
            db.session.commit()
            return "Запись изменена"

    elif request.method == 'DELETE':
        user = UserModel.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return 'Запись удалена'


@app.route("/orders", methods=['GET', "POST"])
def get_all_orders():
    """
    Представление для orders, которое обрабатывает
    GET-запросы получения всех заказов,
    а также создание заказа order посредством метода POST
    """

    result = []
    if request.method == 'GET':
        orders = OrderModel.query.all()
        for order in orders:
            result.append(instance_to_dict_order(order))
        return jsonify(result)

    if request.method == "POST":
        order = json.loads(request.data)
        new_order = OrderModel(
            id=order['id'],
            name=order['name'],
            description=order['description'],
            start_date=order['start_date'],
            end_date=order['end_date'],
            address=order['address'],
            price=order['price'],
            customer_id=order['customer_id'],
            executor_id=order['executor_id']
        )
        db.session.add(new_order)
        db.session.commit()
        db.session.close()
        return "Добавлена новая запись"


@app.route("/orders/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def get_one_order(id):
    """
    получение одного заказа по идентификатору,
    обновление заказа посредством метода PUT ,
    удаление заказа посредством метода DELETE
    """
    if request.method == 'GET':
        order = OrderModel.query.get(id)
        if order is None:
            return 'не найдено поле с таким ид'
        else:
            return jsonify(instance_to_dict_order(order))

    elif request.method == 'PUT':
        order_data = json.loads(request.data)
        order = OrderModel.query.get(id)
        if order is None:
            return 'не найдено поле с таким ид'
        else:
            order.name = order_data['name']
            order.description = order_data['description']
            order.start_date = order_data['start_date']
            order.end_date = order_data['end_date']
            order.address = order_data['address']
            order.price = order_data['price']
            order.customer_id = order_data['customer_id']
            order.executor_id = order_data['executor_id']
            db.session.add(order)
            db.session.commit()
            return "Запись изменена"
    elif request.method == 'DELETE':
        order = OrderModel.query.get(id)
        db.session.delete(order)
        db.session.commit()
        return 'Запись удалена'


@app.route("/offers", methods=['GET', "POST"])
def get_all_offers():
    """
    Представление для предложений, которое обрабатывает
    GET-запросы получения всех предложений,
    а также создание предложения  Offer посредством метода POST
    """

    result = []
    if request.method == 'GET':
        offers = OfferModel.query.all()
        for offer in offers:
            result.append(instance_to_dict_offer(offer))
        return jsonify(result)
    if request.method == "POST":
        offer = json.loads(request.data)
        new_offer = OfferModel(
            id=offer['id'],
            order_id=offer['order_id'],
            executor_id=offer['executor_id']
        )
        db.session.add(new_offer)
        db.session.commit()
        db.session.close()
        return "Добавлена новая запись"


@app.route("/offers/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def get_one_offer(id):
    """
    получение одного предложения по идентификатору,
    обновление предложения посредством метода PUT ,
    удаление предложения посредством метода DELETE
    """
    if request.method == 'GET':
        offer = OfferModel.query.get(id)
        if offer is None:
            return 'не найдено поле с таким ид'
        else:
            return jsonify(instance_to_dict_offer(offer))

    elif request.method == 'PUT':
        offer_data = json.loads(request.data)
        offer = OfferModel.query.get(id)
        if offer is None:
            return 'не найдено поле с таким ид'
        else:
            offer.order_id = offer_data['order_id']
            offer.executor_id = offer_data['executor_id']
            db.session.add(offer)
            db.session.commit()
            return "Запись изменена"

    elif request.method == 'DELETE':
        offer = OfferModel.query.get(id)
        db.session.delete(offer)
        db.session.commit()
        return 'Запись удалена'


if __name__ == '__main__':
    app.run()

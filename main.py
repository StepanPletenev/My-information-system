from datetime import datetime
import uuid


class Order:
    def __init__(self, description, client):
        self.order_id = str(uuid.uuid4())[:8]
        self.description = description
        self.status = "Создан"
        self.client = client
        self.courier = None
        self.created_date = datetime.now()
        self.delivered_date = None

    def update_status(self, new_status):
        self.status = new_status
        if new_status == "Доставлен":
            self.delivered_date = datetime.now()
            self.courier.set_available(True)

    def __str__(self):
        return f"Заказ #{self.order_id} ({self.status})\nОписание: {self.description}\nКлиент: {self.client.name}"


class Courier:
    def __init__(self, name, phone):
        self.courier_id = str(uuid.uuid4())[:8]
        self.name = name
        self.phone = phone
        self.available = True
        self.current_order = None

    def set_available(self, status):
        self.available = status
        if not status:
            self.current_order = None

    def __str__(self):
        status = "Свободен" if self.available else "Занят"
        return f"Курьер #{self.courier_id} - {self.name} ({status})"


class Client:
    def __init__(self, name, address, phone):
        self.client_id = str(uuid.uuid4())[:8]
        self.name = name
        self.address = address
        self.phone = phone
        self.order_history = []

    def add_order(self, order):
        self.order_history.append(order)
    
    def __str__(self):
        return f"Клииент #{self.client_id} - {self.name}\nАдрес: {self.address}"
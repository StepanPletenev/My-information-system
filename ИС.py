from datetime import datetime
import uuid
class Order:
    def __init__(self,description, client):
        self.order_id = str(uuid.uuid4())[:8]
        self.description = description
        self.status = "Создан"
        self.client = client
        self.courier = None
        self.created_date = datetime.now()
        self.delivered_date = None

    def update_status(self,new_status):
        self.status = new_status
        if new_status == "Доставлен":
            self.delivered_date = datetime.now()
            self.courier.set_available(True)

    def __str__(self):
        return f"Заказ #{self.order_id} ({self.status})\nОписание: {self.description}\nКлиент: {self.client.name}"
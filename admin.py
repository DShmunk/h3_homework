import uuid
from ORM.user import User

class Administrator(User):
    def __init__(self, username, userpass, email):
        super().__init__(username, userpass, email)
        self.supply = list()
        self.orders = list()

    def update_supply(self, suppliers_list):
        self.supply.clear()
        for supplier in suppliers_list:
            self.supply.extend(supplier.supply)

    def update_orders(self, customers_list):
        self.orders.clear()
        for customer in customers_list:
            self.orders.extend(customer.orders)

    def check_order(self, order):
        print(f"Checking order {order.id}")
        if not order.status == 'New':
            return order
        for supply in self.supply:
            if supply.item == order.item and supply.amount >= order.amount:
                order.status = 'Confirmed'
                return order
        order.status = 'On hold'
        return order

    # не понял, как провести механизм одобрения админом
    # здесь попытка с критерием публикации = одобрение товара, то есть оценка 4 или 5
    def check_review(self, review):
        print(f"Checking review {review.id}")
        if not review.status == 'Moderation':
            return review
        for review in self.review:
            if review.rating >= 4:
                review.status = 'Published'
                return review
        review.status = 'Published'
        return review
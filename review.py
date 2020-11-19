"""
Добавьте сущность Review.
Review имеет текст, автора (Customer), оценку от 1 до 5, статус (по умолчанию, "Moderation").
Customer может создать Review.
Admin может одобрить Review (статус меняется на "Published").
"""
import uuid
# пусть еще и время создания отзыва будет
import datetime as dt
from ORM.customer import Customer
# по идее, отзыв к какому-то товару, поэтому +Item
from ORM.item import Item

class Review:
    def __init__(self, customer, review_text, rating, item, status="Moderation"):
        self.id = uuid.uuid4()
        self.customer = customer
        self.review_text = review_text
        # self.rating = rating in (1, 2, 3, 4, 5)  - первый вариант, показался негибким
        self.rating = int(rating)
        self.status = status
        self.item = item
        self.date = dt.datetime.now()

    def __str__(self):
        # проверка оценки, если не 1-5, то присваивается максимум, без отказа создания отзыва
        if self.rating not in (1, 2, 3, 4, 5):
            self.rating = 5
        return f'{self.id} {self.customer} {self.review_text} {self.rating} {self.item} {self.status} {self.date}'

if __name__ == '__main__':
    from ORM.item import Item
    from ORM.customer import Customer
    customer0 = Customer("iamguido",
                         "4sure",
                         "Guido",
                         "Van Rossum",
                         "000-112-35-8",
                         "guido@python.org",
                         "09-09-1968")
    review_text0 = "Good product, 5!"
    rating0 = 13
    item0 = Item("Banana",
                 "Better than ever before",
                 799.0,
                 ("Golden", "Fresh Green"))
    review0 = Review(customer=customer0,
                     review_text=review_text0,
                     rating=rating0,
                     item=item0)
    print(review0)

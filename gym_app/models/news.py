from datetime import datetime

class News:
    def __init__(self, news_item: str, create_date: datetime = None, id: int = None):
        self.news_item = news_item
        self.create_date = create_date
        self.id = id
    
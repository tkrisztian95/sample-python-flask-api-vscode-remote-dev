class TopMovie:
    # Initializer / Instance Attributes
    def __init__(self, rank, title, rating):
        self.rank = rank
        self.title = title
        self.rating = rating

    def serialize(self):  
        return {           
            'rank': self.rank, 
            'title': self.title,
            'rating': self.rating
        }
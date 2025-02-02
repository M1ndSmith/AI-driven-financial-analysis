from app.extensions import db


class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(10), unique=True, nullable=False)

    def __repr__(self):
        return f"<Stock {self.ticker}>"

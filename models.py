from app import db

class Result(db.Model):
    __tablename__ = "LinRegResults"

    Id = db.Column(db.Integer, primary_key = True)
    Name = db.Column(db.String())
    YearsExperience = db.Column(db.Float)
    Prediction = db.Column(db.Float)

    def __init__(self, Name, YearsExperience, Prediction):
        self.Name = Name
        self.YearsExperience = YearsExperience
        self.Prediction = Prediction

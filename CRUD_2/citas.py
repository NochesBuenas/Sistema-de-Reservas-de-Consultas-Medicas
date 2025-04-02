class Citas:
    def __init__(self, name, document, phone, direction, date, doctor):
        self.name = name
        self.document = document
        self.phone = phone
        self.direction = direction
        self.date = date
        self.doctor = doctor

    def toTuple(self):
        return (self.name, self.document, self.phone, self.direction, self.date, self.doctor)

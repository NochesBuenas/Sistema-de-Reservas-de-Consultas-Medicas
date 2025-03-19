class Citas:
    def __init__(self, name, document, phone, direction, date, doctor):
        self.name = name
        self.document = document
        self.phone = phone
        self.direction = direction
        self.date = date
        self.doctor = doctor
    def toDBColletion(self):
        return {
            'name': self.name,
            'document': self.document,
            'phone': self.phone,
            'direction': self.direction,
            'date': self.date,
            'doctor': self.doctor
        }
from bson import ObjectId

# Clase utilitaria para manejar los datos de los eventos
class Event:
    def __init__(self, title, description, date, location, _id=None):
        self._id = ObjectId(_id) if _id else None  # Manejar el ObjectId de MongoDB
        self.title = title
        self.description = description
        self.date = date
        self.location = location

    def to_dict(self):
        """
        Convierte el objeto Event en un diccionario para almacenarlo en MongoDB.
        """
        data = {
            "title": self.title,
            "description": self.description,
            "date": self.date,
            "location": self.location,
        }
        if self._id:
            data["_id"] = self._id
        return data

    @staticmethod
    def from_dict(data):
        """
        Crea un objeto Event desde un diccionario (por ejemplo, datos obtenidos de MongoDB).
        """
        return Event(
            title=data.get("title"),
            description=data.get("description"),
            date=data.get("date"),
            location=data.get("location"),
            _id=data.get("_id"),
        )
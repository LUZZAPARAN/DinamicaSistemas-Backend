from flask import Blueprint, jsonify, request
from database.connection import get_db
from models.event import Event

# Crear un Blueprint para las rutas de eventos
events_bp = Blueprint("events", __name__)

@events_bp.route("/events", methods=["GET"])
def get_events():
    db = get_db()
    events = list(db.Events.find({}))  
    event_objects = [Event.from_dict(event).to_dict() for event in events]
    return jsonify(event_objects)

@events_bp.route("/events", methods=["POST"])
def create_event():
    db = get_db()
    data = request.get_json()
    event = Event.from_dict(data)
    result = db.Events.insert_one(event.to_dict())  
    return jsonify({"inserted_id": str(result.inserted_id)}), 201
from flask import Blueprint, jsonify
from services.data_service import load_events

events_bp = Blueprint("events", __name__)

@events_bp.route("/", methods=["GET"])
def get_events():
    """
    Return oil market events.
    """
    try:
        df = load_events()
        return jsonify(df.to_dict(orient="records"))
    except FileNotFoundError:
        return jsonify({"error": "Events data file not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

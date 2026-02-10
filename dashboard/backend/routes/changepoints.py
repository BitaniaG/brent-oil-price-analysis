from flask import Blueprint, jsonify
from services.data_service import load_changepoints

changepoints_bp = Blueprint("changepoints", __name__)

@changepoints_bp.route("/", methods=["GET"])
def get_changepoints():
    try:
        data = load_changepoints()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

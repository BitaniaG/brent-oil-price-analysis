from flask import Blueprint, jsonify
from services.data_service import load_prices

prices_bp = Blueprint("prices", __name__)

@prices_bp.route("/", methods=["GET"])
def get_prices():
    """
    Return Brent oil price data.
    """
    try:
        df = load_prices()
        return jsonify(df.to_dict(orient="records"))
    except FileNotFoundError:
        return jsonify({"error": "Price data file not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

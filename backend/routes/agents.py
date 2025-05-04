from flask import Blueprint, jsonify
from services.sqlserver_service import SQLServerService

agents_bp = Blueprint("agents", __name__)

@agents_bp.route("/agents", methods=["GET"])
def get_agents():
    try:
        data = SQLServerService.get_table_data("agents")
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
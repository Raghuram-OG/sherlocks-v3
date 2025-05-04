from flask import Blueprint, jsonify
from services.sqlserver_service import SQLServerService
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

archives_bp = Blueprint("archives", __name__)

@archives_bp.route("/archives", methods=["GET"])
def get_archives():
    try:
        logger.debug("Fetching archives data")
        data = SQLServerService.get_table_data("archives")
        logger.info(f"Returning {len(data)} rows for archives")
        return jsonify(data)
    except Exception as e:
        logger.error(f"Error fetching archives: {str(e)}")
        return jsonify({"error": str(e)}), 500
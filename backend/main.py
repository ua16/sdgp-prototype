
# g is a global object that can be accessed safely from all threads ( at least I think )
from flask import Flask, jsonify, request, g

import sqlite3

# Set up sqlite3
db_path = "db_01.db"

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(
            db_path,
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def create_app():
    app = Flask(__name__)

    @app.after_request
    def add_cors_headers(response):
        response.headers["Access-Control-Allow-Origin"] = "*"  # allow all origins
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization, x-api-key"
        return response

    @app.route("/", methods=["GET"])
    def index():
        return jsonify({"message": "API is running"})

    @app.route("/echo", methods=["POST"])
    def echo():
        data = request.get_json(silent=True) or {}
        return jsonify({"received": data})

    @app.route("/rfqs", methods=["POST"])
    def rfqs():
        db = get_db()
        cursor = db.cursor()
        data = request.get_json(silent=True)

        if not data or "targetOrgId" not in data:
            return jsonify({"error": "targetOrgId is required"}), 400

        targetOrgId = data["targetOrgId"]

        cursor.execute("""
                       SELECT r.rfqid, r.origin, r.destination,
                       datetime(r.creationDate) as creationDate, datetime(r.expiryDate) as expiryDate, 
                       o.companyName
                       FROM rfq as r
                       LEFT JOIN
                       organization as o
                       ON r.issuingOrgId = o.organizationID
                       WHERE targetOrgId = ?
                       """, (targetOrgId,))

        rows = cursor.fetchall()
        rows = [dict(row) for row in rows]

        return jsonify(rows), 200

    @app.teardown_appcontext
    def close_db(exception):
        db = g.pop("db", None)
        if db is not None:
            db.close()

    return app


if __name__ == "__main__":
    application = create_app()
    application.run(host="0.0.0.0", port=5000)

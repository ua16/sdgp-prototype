from flask import Flask, jsonify, request
from dataclasses import asdict, dataclass
from datetime import datetime

import utils.faker as faker

@dataclass
class RequestForQuote:
    ident : str
    Shipper : str
    RequiredServices : str
    OriginDestination : str
    DateCreated : datetime
    Deadline  : datetime
    Status : str

rfqlist = []
# Generate fake rfq data
for i in range(70):
    rfqlist.append(RequestForQuote(
        ident=f"rfq{i}",
        Shipper=faker.company.name(),
        RequiredServices="Freight Forwarding",
        OriginDestination=faker.airline.iatacode() + ">" + faker.airline.iatacode(),
        DateCreated=faker.date.recent(),
        Deadline=faker.date.near_future(),
        Status="Pending"
        ))



def create_app():
    app = Flask(__name__)

    @app.after_request
    def add_cors_headers(response):
        response.headers["Access-Control-Allow-Origin"] = "*"  # allow all origins
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        return response

    @app.route("/", methods=["GET"])
    def index():
        return jsonify({"message": "API is running"})

    @app.route("/echo", methods=["POST"])
    def echo():
        data = request.get_json(silent=True) or {}
        return jsonify({"received": data})

    @app.route("/rfqs", methods=["GET"])
    def rfqs():
        return jsonify(rfqlist)

    return app


if __name__ == "__main__":
    application = create_app()
    application.run(host="0.0.0.0", port=5000)

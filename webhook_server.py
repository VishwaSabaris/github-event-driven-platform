from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

from utils.processor import process_event
from services.api_service import validate_payload

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("API_KEY", "SECRET123")


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "running",
        "service": "GitHub Event Backend API"
    }), 200


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy"
    }), 200


@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json(silent=True)

        if not data:
            return jsonify({
                "success": False,
                "error": "Invalid or empty JSON body"
            }), 400

        print("\nReceived data from n8n:")
        print(data)

        is_valid, message = validate_payload(data)

        if not is_valid:
            return jsonify({
                "success": False,
                "error": message
            }), 400

        processed_event = process_event(data)

        if processed_event["status"] == "Late Activity":
            print("Late activity detected")
        elif processed_event["status"] == "Normal Activity":
            print("Normal activity")
        else:
            print("Unknown or invalid activity")

        return jsonify({
            "success": True,
            "message": "Webhook processed successfully",
            "processed": processed_event
        }), 200

    except Exception as e:
        print("Server error:", str(e))

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.route("/secure-webhook", methods=["POST"])
def secure_webhook():
    try:
        received_api_key = request.headers.get("x-api-key")

        if received_api_key != API_KEY:
            return jsonify({
                "success": False,
                "error": "Unauthorized request"
            }), 401

        data = request.get_json(silent=True)

        if not data:
            return jsonify({
                "success": False,
                "error": "Invalid or empty JSON body"
            }), 400

        processed_event = process_event(data)

        return jsonify({
            "success": True,
            "message": "Secure webhook processed successfully",
            "processed": processed_event
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

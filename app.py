from flask import Flask, request, jsonify
from lob_service import send_letter

app = Flask(__name__)

@app.route("/send-letter", methods=["POST"])
def send_letter_route():
    try:
        data = request.json
        print("📩 Received data:", data)

        result = send_letter(
            first_name=data["first_name"],
            last_name=data["last_name"],
            address_line1=data["address_line1"],
            city=data["address_city"],
            state=data["address_state"],
            zip_code=data["address_zip"],
            message_body="Hello {{name}}, this is your test letter from Stride CRM."
        )

        return jsonify({
            "status": "success",
            "lob_response": result
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
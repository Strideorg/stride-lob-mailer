from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Stride Lob API is running ✅"

@app.route("/send-letter", methods=["POST"])
def send_letter_endpoint():
    data = request.json

    print("📩 Received data:", data)

    return jsonify({
        "status": "success",
        "message": "Data received successfully"
    })

if __name__ == "__main__":
    app.run(port=5000, debug=True)
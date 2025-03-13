from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask API is running!"

@app.route("/get_stock_price", methods=["GET"])
def get_stock_price():
    symbol = request.args.get("symbol")
    if not symbol:
        return jsonify({"error": "No stock symbol provided"}), 400

    stock_data = {"AAPL": 150.75, "GOOGL": 2800.50, "TSLA": 950.25}
    price = stock_data.get(symbol.upper())

    if price:
        return jsonify({"symbol": symbol.upper(), "price": price})
    else:
        return jsonify({"error": "Stock symbol not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

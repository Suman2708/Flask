# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from pymongo import MongoClient
# import math

# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})



# # Connect to MongoDB
# client = MongoClient("mongodb+srv://shumankr99:sSuAAWNasR6aIhkr@cluster0.zngrhkq.mongodb.net/")  # Or your Atlas URI
# db = client['shopDB']
# collection = db['products']

# @app.route('/products', methods=['GET'])
# def get_products():
#     try:
#         raw_data = list(collection.find({}, {'_id': 0}))
#         cleaned_data = []

#         for item in raw_data:
#             name = item.get('demo_data', '')
#             price_str = item.get('Unnamed: 1', '')

#             try:
#                 price = float(price_str)
#             except ValueError:
#                 continue  # skip if price is not valid

#             cleaned_data.append({
#                 'name': name,
#                 'price': price
#             })

#         return jsonify(cleaned_data), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# @app.route('/filter', methods=['POST'])
# def filter_products():
#     try:
#         data = request.get_json()
#         min_price = float(data.get('min_price', 0))
#         max_price = float(data.get('max_price', float('inf')))

#         raw_data = list(collection.find({}, {'_id': 0}))
#         filtered = []

#         for item in raw_data:
#             try:
#                 price = float(item.get('Unnamed: 1', ''))
#                 if min_price <= price <= max_price:
#                     filtered.append({
#                         'name': item.get('demo_data', ''),
#                         'price': price
#                     })
#             except ValueError:
#                 continue

#         return jsonify(filtered), 200

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)




from flask import Flask
from flask_cors import CORS
from routes.products import products_bp
from routes.filter import filter_bp

app = Flask(__name__)
CORS(app)

# Register Blueprints
app.register_blueprint(products_bp)
app.register_blueprint(filter_bp)

if __name__ == '__main__':
    app.run(debug=True)


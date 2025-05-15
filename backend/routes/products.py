from flask import Blueprint, jsonify
from db.mongo import get_collection

products_bp = Blueprint('products', __name__)

collection = get_collection()

@products_bp.route('/products', methods=['GET'])
def get_products():
    try:
        raw_data = list(collection.find({}, {'_id': 0}))
        cleaned_data = []

        for item in raw_data:
            name = item.get('demo_data', '') 
            price_str = item.get('Unnamed: 1', '')  
            try:
                price = float(price_str) 
            except ValueError:
                continue 

            cleaned_data.append({
                'name': name,
                'price': price
            })

        return jsonify(cleaned_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

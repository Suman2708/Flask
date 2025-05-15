from flask import Blueprint, request, jsonify
from db.mongo import get_collection

filter_bp = Blueprint('filter', __name__)

collection = get_collection()

@filter_bp.route('/filter', methods=['POST'])
def filter_products():
    try:
        data = request.get_json()
        min_price = float(data.get('min_price', 0))
        max_price = float(data.get('max_price', float('inf')))

        raw_data = list(collection.find({}, {'_id': 0}))
        filtered = []

        for item in raw_data:
            try:
                price = float(item.get('Unnamed: 1', ''))
                if min_price <= price <= max_price:
                    filtered.append({
                        'name': item.get('demo_data', ''),
                        'price': price
                    })
            except ValueError:
                continue

        return jsonify(filtered), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

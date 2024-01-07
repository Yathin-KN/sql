from flask import Flask, jsonify
import mysql.connector
import time

app = Flask(__name__)

# Connect to the MySQL database
mysql_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "ecommerce"
}
conn = mysql.connector.connect(**mysql_config)
cursor = conn.cursor()

# Sample injection for time-based blind SQL injection
sample_injection = " AND (SELECT COUNT(*) FROM information_schema.tables WHERE table_name = 'product') > 0 AND SLEEP(2);"



@app.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    # Execute a query to retrieve the product by ID from the MySQL database
    sql_query = "SELECT * FROM products WHERE id = " + product_id
    cursor.execute(sql_query)
    print(cursor.statement)
    # Fetch the result
    product = cursor.fetchone()

    # Check if the product exists
    if not product:
        return jsonify({"error": "Product not found"}), 404

    # Convert the result to a dictionary for the API response
    product_dict = {
        "id": product[0],
        "name": product[1],
        "price": product[2],
        "description": product[3],
        "stock": product[4],
    }

    return jsonify(product_dict)

if __name__ == '__main__':
    app.run(debug=True)

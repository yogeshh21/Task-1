# Import necessary libraries
import requests
from flask import Flask, render_template

app = Flask(__name__)

# Fetch JSON data from the provided API URL
url = "https://s3.amazonaws.com/open-to-cors/assignment.json"
response = requests.get(url)
data = response.json()

# Extract product data
products = data.get("products", {})
sorted_products = sorted(products.values(), key=lambda x: int(x["popularity"]), reverse=True)

# Display data in the console
for product in sorted_products:
    print(f"Title: {product['title']}, Price: {product['price']}, Popularity: {product['popularity']}")

# Render the web page
@app.route('/')
def display_products():
    return render_template('index.html', products=sorted_products)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify,request

app = Flask(__name__)

# Sample data
books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}
]

# GET endpoint to retrieve all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({"data":books,"source":request.headers['User-Agent']})

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
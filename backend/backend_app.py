from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]


@app.route('/api/posts', methods=['GET'])
def get_posts():
    return jsonify(POSTS)


@app.route('/api/posts', methods=['POST'])
def add_posts():
    # Expecting JSON object in the body of the request
    data = request.get_json()
    try:
        if not data or data["title"] is None or data["content"] is None or  not data["title"] or not data["content"]:
            return jsonify({"error": "Invalid or missing JSON data"}), 400
    except KeyError:
        return jsonify({"error": "Invalid or missing JSON data"}), 400

    # Add data to the dictionary
    data_id = len(POSTS) + 1
    data["id"] = data_id
    POSTS.append(data)
    return jsonify(data), 201


@app.route('/api/posts/<int:id>')
def delete(id):
    try:
        if POSTS[id] is None:
            # Post not found
            return "Post not found", 404
    except IndexError:
        return "Post not found", 404
    else:
        del POSTS[id]
        return jsonify({"message": f'Post with id {id} has been deleted successfully.'}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)

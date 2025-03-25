from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

POSTS = [
    {"id": 1, "title": "First post", "content": "This is the first post."},
    {"id": 2, "title": "Second post", "content": "This is the second post."},
]
data_blue_print = {"title", "content"}

@app.route('/api/posts', methods=['GET', 'POST'])
def handle_posts():
    if request.method == 'POST':
        data = request.json
        if not data["title"] or not data["content"]:
            return jsonify({"message": "missing-items"}), 404

        title = data['title']
        content = data['content']
        if POSTS:
            max_post = max(POSTS, key=lambda x: x['id'])
            new_id = max_post['id'] + 1
        else:
            new_id = 1
        new_post = {"id": new_id, "title": title, "content": content}
        POSTS.append(new_post)

        return jsonify(new_post), 201

    if request.method == 'GET':
        sort = request.args.get('sort')
        direction = request.args.get('direction')

        if not sort or not direction:
            return jsonify(POSTS), 200

        if sort not in data_blue_print or direction not in ['asc', 'desc']:
            return jsonify({"message": "Invalid sort parameters"}), 400

        if direction == 'desc':
            reverse = True
        else:
            reverse = False
        sorted_posts = sorted(POSTS, key=lambda x: x[sort], reverse=reverse)
        return jsonify(sorted_posts), 200


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


@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete(post_id):
    i = 0
    for post in POSTS:
        if post["id"] == post_id:
            del POSTS[i]
            return jsonify({"message": f'Post with id {post_id} has been deleted successfully.'}), 200
        i += 1
    return "Post not found", 404


@app.route('/api/posts/search', methods=['GET'])
def search_posts():
    search_title = request.args.get('title')
    search_content = request.args.get('content')
    results = [
        post for post in POSTS
        if (search_title.lower() in post['title'].lower() if search_title else True) and
           (search_content.lower() in post['content'].lower() if search_content else True)
    ]

    if results:
        return jsonify(results), 200
    else:
        return jsonify({"message": f"No posts found that match your queries"}), 404



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)

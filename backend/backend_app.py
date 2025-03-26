from django.core.exceptions import BadRequest
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
    sort = request.args.get('sort')
    direction = request.args.get('direction')

    if not sort or not direction:
        return jsonify(POSTS), 200

    if sort not in ["title", "content"] or direction not in ['asc', 'desc']:
        return jsonify({"message": "Invalid sort parameters"}), 400

    if direction == 'desc':
        reverse = True
    else:
        reverse = False
    sorted_posts = sorted(POSTS, key=lambda x: x[sort], reverse=reverse)
    return jsonify(sorted_posts), 200


@app.route('/api/posts', methods=['POST'])
def add_posts():
    data = None
    # Expecting JSON object in the body of the request
    try:
        data = request.get_json()
    except Exception:
        return jsonify({"Error": "Invalid or missing JSON data"}), 400
    if data is None or data == {}:
        return jsonify({"Error": "Nothing to Add"}), 400
    try:
        if data["title"] == '':
            return jsonify({"error": "'Title' is missing"}), 400
        if data["content"] == '':
            return jsonify({"Error": "'Content' is missing"}), 400
    except (KeyError, TypeError) as e:
        return jsonify('{Error:'+str(e)+' is missing}'), 400
    if POSTS:
        max_post = max(POSTS, key=lambda x: x['id'])
        data_id = max_post['id'] + 1
    else:
        data_id = 1
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
    return jsonify({"message": f"Post with id {post_id} not found"}), 404


@app.route('/api/posts/<int:post_id>', methods=['PUT'])
def update(post_id):
    i = 0
    for post in POSTS:
        if post["id"] == post_id:
            data = request.json
            try:
                POSTS[i]["title"] = data["title"]
            except KeyError:
                pass
            try:
                POSTS[i]["content"] = data["content"]
            except KeyError:
                pass
            return jsonify({"message": f'Post with id {post_id} has been '
                                       f'updated successfully.'}), 200
        i += 1
    return jsonify({"message": f"Post with id {post_id} not found"}), 404


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

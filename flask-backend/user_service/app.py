from flask import Flask, jsonify
from flask_cors import CORS
import redis
import json

app = Flask(__name__)
CORS(app)

cache = redis.Redis(host='redis', port=6379, db=1, decode_responses=True)

@app.route('/profile/<username>', methods=['GET'])

def get_profile(username):
    cache_key = f"profile:{username}"
    
    cached_profile = cache.get(cache_key)
    if cached_profile:
        return jsonify({"user": json.loads(cached_profile), "cached": True}), 200

    user_profile = {
        "username": username,
        "bio": "Esta é uma bio de exemplo.",
        "email": f"{username}@exemplo.com"
    }
    
    cache.set(cache_key, json.dumps(user_profile), ex=3600)
    return jsonify({"user": user_profile, "cached": False}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

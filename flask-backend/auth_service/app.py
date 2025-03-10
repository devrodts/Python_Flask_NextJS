from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
from datetime import timedelta
from common.redis_logger import setup_redis_logging

app = Flask(__name__)
CORS(app)

app.config["MONGO_URI"] = "mongodb://mongo:27017/python_next"
app.config["JWT_SECRET_KEY"] = "senha_secreta"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

mongo = PyMongo(app)
jwt = JWTManager(app)


logger = setup_redis_logging(__name__)

@app.route('/register', methods=['POST'])

def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    if mongo.db.users.find_one({"username": username}):
        logger.warning(f"Tentativa de registro com usuário existente: {username}")
        return jsonify({"msg": "Usuário já existe"}), 409

    hashed_password = generate_password_hash(password)
    mongo.db.users.insert_one({"username": username, "password": hashed_password})
    logger.info(f"Usuário registrado: {username}")
    return jsonify({"msg": "Usuário registrado com sucesso"}), 201


@app.route('/login', methods=['POST'])

def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = mongo.db.users.find_one({"username": username})
    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(identity=username)
        logger.info(f"Login realizado com sucesso: {username}")
        return jsonify(access_token=access_token), 200
    else:
        logger.error(f"Falha no login para: {username}")
        return jsonify({"msg": "Credenciais inválidas"}), 401

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    logger.info(f"Acesso à rota protegida por: {current_user}")
    return jsonify(logged_in_as=current_user), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

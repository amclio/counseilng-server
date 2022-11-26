import os

from flask import Flask, jsonify, make_response, request
from flask_cors import CORS
from supabase import Client, create_client

url = os.environ.get('SUPABASE_URL')
key = os.environ.get('SUPABASE_KEY')
supabase = create_client(url, key)

app = Flask(__name__)
CORS(app)


def createArticles(user_id, title, content):
    approval = {
        "user_id": user_id,
        "title": title,
        "content": content
    }
    data = supabase.table("posts").insert(approval).execute()
    return data.data


def getArticles():
    data = supabase.table("posts").select(
        "*, profiles(raw_user_meta_data)").order('id', desc=False).execute()
    return data.data


def getArticlesById(id):
    data = supabase.table("posts").select(
        "*, profiles(raw_user_meta_data)").eq('id', id).execute()
    return data.data


@app.route('/articles', methods=['POST'])
def postArticles():
    data = request.get_json()
    user_id = data['user_id']
    title = data['title']
    content = data['content']
    res = createArticles(user_id, title, content)
    return jsonify(res), 201


@app.route('/articles', methods=['GET'])
def restGetArticles():
    res = getArticles()
    return jsonify(res), 200


@app.route('/articles/<id>', methods=['GET'])
def restGetArticlesById(id):
    res = getArticlesById(id)

    return jsonify(res), 200


@app.route('/articles/<id>', methods=['DELETE'])
def deleteArticlesById(id):
    supabase: Client = create_client(url, key)
    res = supabase.table("posts").delete().eq("id", id).execute()
    data = res
    # 사용자에게 잘 생성되었다고 응답
    return make_response(jsonify(data.data), 202)


@app.route('/users', methods=['POST'])
def createUser():
    data = request.get_json()
    email = data['email']
    password = data['password']

    user = supabase.auth.sign_up(email=email, password=password)
    print(user)

    return jsonify(user.dict()), 201


if __name__ == '__main__':
    app.run(port=4000)

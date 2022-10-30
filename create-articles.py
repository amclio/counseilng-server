import os

from flask import Flask, Response, jsonify, request
from supabase import Client, create_client

url = 'https://zvxlqpfkfudfdqedqoyu.supabase.co'
key = 'key'
supabase = create_client(url, key)

app = Flask(__name__)


def insert_approval(user_id, title, content):
    approval = {
        "user_id": user_id,
        "title": title,
        "content": content
    }
    data = supabase.table("posts").insert(approval).execute()
    return data.data


@app.route('/articles', methods=['POST'])
def add_approval():
    data = request.get_json()
    user_id = data['user_id']
    title = data['title']
    content = data['content']
    res = insert_approval(user_id, title, content)
    return jsonify(res), 201


insert_approval('b67db583-0a47-4d32-a5c4-35eb9e28704c', '제목', '내용')

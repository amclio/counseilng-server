import os

from flask import Flask, Response, jsonify, make_response, request
from supabase import Client, create_client

# Supabase 코드
url: str = "https://zvxlqpfkfudfdqedqoyu.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inp2eGxxcGZrZnVkZmRxZWRxb3l1Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY2MTk1NjY5OCwiZXhwIjoxOTc3NTMyNjk4fQ.Z6THxR-f68TDk0uAdPrZmp93iQ00-PV5yRjkk1DOe_M"

app = Flask(__name__)

supabase = create_client(url, key)

# 모든 데이터를 가져옴


def find_approvals():
    data = supabase.table("approvals").select("*").execute()
    return data['data']

# 데이터를 DB에 저장함


def insert_approval(title, project_name, value):
    approval = {
        "title": title,
        "project_name": project_name,
        "value": value
    }

    data = supabase.table("approvals").insert(approval).execute()

    return data['data']

# Flask 코드


@app.route('/articles/<id>', methods=['DELETE'])
def add_approval(id):
    supabase: Client = create_client(url, key)
    res = supabase.table("posts").delete().eq("id", id).execute()
    data = res
    # 사용자에게 잘 생성되었다고 응답
    return make_response(jsonify(data.data), 202)


if __name__ == '__main__':
    app.run()

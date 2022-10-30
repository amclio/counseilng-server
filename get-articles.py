import os

from flask import Flask, Response, jsonify, request
from supabase import Client, create_client

app = Flask(__name__)


# 모든 데이터를 가져옴
def find_approvals():
    data = supabase.table("posts").select("*").execute()
    return data.data

# 데이터를 DB에 저장함


print(find_approvals())
# Flask 코드


@app.route('/articles', methods=['GET'])
def add_approval():
    res = find_approvals()

    # 사용자에게 잘 생성되었다고 응답
    return jsonify(res), 201

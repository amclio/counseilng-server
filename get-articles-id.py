import os

from flask import Flask, Response, jsonify, request
from supabase import Client, create_client

url = "https://zvxlqpfkfudfdqedqoyu.supabase.co"
key = "키"

supabase = create_client(url, key)

app = Flask(__name__)


def find_approvals(id):
    data = supabase.table("approvals").select("*").eq('id', id).execute()
    return data['data']


def insert_approval(title, project_name, value):
    approval = {
        "title": title,
        "project_name": project_name,
        "value": value
    }

    data = supabase.table("approvals").insert(approval).execute()

    return data['data']


@app.route('/articles/<id>', methods=['POST'])
def add_approval(id):

    data = request.get_json()

    title = data['title']
    project_name = data['project_name']
    value = data['value']

    res = insert_approval(title, project_name, int(value))

    return jsonify(res), 201

from flask import request, jsonify, Blueprint, render_template, abort
from contextlib import closing

from markupsafe import Markup

from server.utils import get_db
from difflib import HtmlDiff

index = Blueprint("index", __name__, template_folder="static")


@index.route("/upsert_question", methods=["POST"])
def upsert_question():
    body = request.get_json()
    if not body or not body.get("question"):
        return jsonify({"error": "`question` text required"}), 400

    question_id = body.get("question_id")
    question_text = body.get("question")
    db = get_db()
    with closing(db.cursor()) as cursor:
        if question_id:
            cursor.execute("SELECT id FROM questions WHERE id=?", (question_id, ))
            db_response = cursor.fetchone()
            if not db_response or not db_response.get("id"):
                return jsonify({"error": "Unknown `question_id`: {}".format(question_id)}), 404
            else:
                cursor.execute(
                    "INSERT INTO questions(id, question) VALUES (?, ?)",
                    (question_id, question_text)
                )
            message = "Question successfully updated"
        else:
            cursor.execute("SELECT IFNULL(MAX(id), 0) + 1 AS id FROM questions")
            question_id = cursor.fetchone()["id"]
            cursor.execute(
                "INSERT INTO questions(id, question) VALUES (?, ?) ",
                (question_id, question_text)
            )
            message = "Question successfully created"

    db.commit()

    return jsonify({"message": message, "question_id": question_id})


@index.route("/question_history/<question_id>", methods=["GET"])
def question_history(question_id):
    db = get_db()
    with closing(db.cursor()) as cursor:
        cursor.execute(
            "SELECT updated_at, question FROM questions WHERE id = ? ORDER BY updated_at ASC",
            (question_id, )
        )
        items = cursor.fetchall()
    differ = HtmlDiff()
    tables = []
    if not items:
        return abort(404)
    if len(items) == 1:
        tables.append((Markup(differ.make_table(
            [items[0]["question"]], "", fromdesc=items[0]["updated_at"])
        )))
    else:
        for i in range(len(items) - 1):
            from_item = items[i]
            to_item = items[i + 1]
            tables.append(Markup(differ.make_table(
                [from_item["question"]], [to_item["question"]],
                fromdesc=from_item["updated_at"], todesc=to_item["updated_at"])
            ))
    return render_template(
        "question_history.html",
        question_id=question_id, tables=tables, styles=differ._styles
    )

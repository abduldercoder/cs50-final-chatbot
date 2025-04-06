import os
from flask import jsonify
from datetime import datetime
from flask import Flask, render_template, request, redirect
import sqlite3
from transformers import pipeline

# Starte das Chat-Modell (DIALOGPT)
chat_pipe = pipeline("text-generation", model="microsoft/DialoGPT-small")

app = Flask(__name__)
app.secret_key = "geheim"

# Datenbank vorbereiten
def init_db():
    with sqlite3.connect("chatbot.db") as con:
        db = con.cursor()
        db.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                prompt TEXT NOT NULL,
                response TEXT NOT NULL,
                timestamp TEXT NOT NULL
            )
        """)
        con.commit()

init_db()



@app.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        prompt = request.form.get("prompt")
        response = chat_pipe(prompt, max_new_tokens=100)[0]["generated_text"]

        # Speichern in der Datenbank
        with sqlite3.connect("chatbot.db") as con:
            db = con.cursor()
            db.execute("INSERT INTO messages (prompt, response, timestamp) VALUES (?, ?, ?)",
                       (prompt, response, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            con.commit()

        return jsonify({"response": response})

    return render_template("chat.html")


    # Lade bisherigen Chatverlauf
    with sqlite3.connect("chatbot.db") as con:
        db = con.cursor()
        db.execute("SELECT prompt, response, timestamp FROM messages ORDER BY id DESC")
        messages = db.fetchall()

    return render_template("chat.html", messages=messages)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask,jsonify
import os
import sqlite3
app=Flask(__name__)
@app.route("/jobs")
def get_jobs():
    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "jobs.db"))
    conn = sqlite3.connect(db_path)
    c=conn.cursor()
    c.execute("SELECT * FROM jobs")
    jobs=[{"title":row[0],"link":row[1]} for row in c.fetchall()]
    return jsonify(jobs)
if __name__=="__main__":
    app.run(debug=True)


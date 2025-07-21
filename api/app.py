from flask import Flask,jsonify
import sqlite3
app=Flask(__name__)
@app.route("/jobs")
def get_jobs():
    conn=sqlite3.connect("jobs.db")
    c=conn.sursor()
    c.execute("SELECT * FROM jobs")
    jobs=[{"title":row[0],"link":row[1]} for row in c.fetchall()]
    return jsonify(jobs)
if __name__=="__main__":
    app.run(debug=True)
    
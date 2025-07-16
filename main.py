from flask import Flask, jsonify
from rss_evaluate import main as run_rss

app = Flask(__name__)

@app.route("/run", methods=["GET"])
def run_job():
    try:
        run_rss()
        return jsonify({"status": "success", "message": "RSS evaluation complete."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

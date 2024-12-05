# insureai/app.py
from flask import Flask, request, jsonify
from qa_pipeline import query_insureai

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    # Get user query from request
    user_query = request.json.get("query", "")
    if not user_query:
        return jsonify({"error": "Query is required"}), 400

    # Get response from RAG pipeline
    response = query_insureai(user_query)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, jsonify
import sys
import os

# ✅ Add project root to path FIRST
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from rag_pipline import answer_question

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    if 'pdf' not in request.files or 'query' not in request.form:
        return jsonify({"error": "Missing PDF file or question"}), 400

    pdf_file = request.files['pdf']
    question = request.form['query']

    answer = answer_question(pdf_file, question)

    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify
import gemma3n  # Gemma 3n Python API

app = Flask(__name__)

# モデルをロード（初回のみ）
model = gemma3n.load_model("gemma3n-base")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text_input = data.get("text", "")
    
    # Gemma 3nでテキストを処理
    result = model.predict(text_input)
    
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)

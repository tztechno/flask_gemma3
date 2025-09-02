# flask_gemma3


---

完璧です。では **テキスト入力型** の簡易 Web アプリを作る場合、先ほどの Flask 例をベースに少し整理して、最小構成で動かせる形をまとめます。

---

## 1. ディレクトリ構成

```
gemma_web_app/
│
├─ app.py           # Flask サーバー
├─ templates/
│   └─ index.html   # 入力画面
├─ requirements.txt # 依存ライブラリ
```

---

## 2. `requirements.txt`

```txt
flask
gemma3n  # 仮: Gemma 3n の Python ライブラリ名
```

---

## 3. Flaskサーバー (`app.py`)

```python
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
```

---

## 4. HTML画面 (`templates/index.html`)

```html
<!DOCTYPE html>
<html>
<head>
    <title>Gemma 3n Text App</title>
</head>
<body>
    <h1>Gemma 3n Demo</h1>
    <input type="text" id="user_input" placeholder="Type something"/>
    <button onclick="sendRequest()">Submit</button>
    <p id="output"></p>

    <script>
    async function sendRequest() {
        const text = document.getElementById("user_input").value;
        const res = await fetch("/predict", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({text: text})
        });
        const data = await res.json();
        document.getElementById("output").innerText = data.result;
    }
    </script>
</body>
</html>
```

---

## 5. 実行方法

```bash
# 仮想環境作成
python -m venv venv
source venv/bin/activate  # mac/linux
# venv\Scripts\activate   # Windows

# 必要ライブラリインストール
pip install -r requirements.txt

# サーバー起動
python app.py
```

ブラウザで `http://127.0.0.1:5000/` にアクセスするとテキストを入力して結果を取得できます。

---

💡 **ポイント**

* モデルのロードはサーバー起動時に一度だけ行う
* `/predict` は JSON でリクエスト・レスポンスするシンプルな API
* フロント側は Fetch API で非同期通信

---

希望であれば、**テキスト履歴を画面に残すチャット風UI** にも拡張できます。
作ってほしいですか？

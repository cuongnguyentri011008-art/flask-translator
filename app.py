from flask import Flask, request, render_template_string
from translatepy import Translator

app = Flask(__name__)
translator = Translator()

template = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Dịch Anh → Việt</title>
<style>
body{
    font-family: Arial;
    background:#e3f2fd;
    text-align:center;
    padding-top:50px;
}
.box{
    background:white;
    width:600px;
    margin:auto;
    padding:25px;
    border-radius:10px;
    box-shadow:0 0 15px rgba(0,0,0,.2);
}
textarea{
    width:95%;
    height:120px;
    padding:10px;
    font-size:16px;
}
button{
    padding:10px 20px;
    margin-top:15px;
    font-size:16px;
    background:#1976d2;
    color:white;
    border:none;
    border-radius:5px;
    cursor:pointer;
}
.output{
    margin-top:20px;
    font-size:18px;
    color:#2e7d32;
}
</style>
</head>

<body>
<div class="box">
<h2>🌍 English → Vietnamese Translator</h2>

<form method="POST">
<textarea name="text" placeholder="Nhập câu tiếng Anh vào đây...">{{ text }}</textarea><br>
<button type="submit">Dịch ngay</button>
</form>

{% if result %}
<div class="output">
<h3>Kết quả dịch:</h3>
<p>{{ result }}</p>
</div>
{% endif %}

</div>
</body>
</html>
"""

@app.route("/", methods=["GET","POST"])
def index():
    text = ""
    result = ""

    if request.method == "POST":
        text = request.form["text"]
        if text.strip():
            result = translator.translate(text, "Vietnamese").result

    return render_template_string(template, text=text, result=result)

app.run(debug=True)

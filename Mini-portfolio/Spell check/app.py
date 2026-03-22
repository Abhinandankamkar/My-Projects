from flask import Flask, render_template, request
from spellchecker import SpellChecker # type: ignore

app = Flask(__name__)
spell = SpellChecker()

@app.route("/", methods=["GET", "POST"])
def index():
    corrected_text = ""
    original_text = ""

    if request.method == "POST":
        original_text = request.form["text"]
        words = original_text.split()
        corrected_words = []

        for word in words:
            corrected_word = spell.correction(word)
            corrected_words.append(corrected_word)
        
        corrected_text = " ".join(corrected_words)

    return render_template("index.html", corrected_text=corrected_text, original_text=original_text)

if __name__ == "__main__":
    app.run(debug=True)

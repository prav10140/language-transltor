from flask import Flask, render_template, request, jsonify
from googletrans import Translator, LANGUAGES

app = Flask(__name__)
translator = Translator()

@app.route('/')
def home():
    # Pass the available languages to the frontend
    return render_template('index.html', languages=LANGUAGES)

@app.route('/translate', methods=['POST'])
def translate():
    text = request.form.get('text')
    target_language = request.form.get('target_language')

    if not text or not target_language:
        return jsonify({'error': 'Both text and target language are required!'}), 400

    try:
        # Translate the entire text at once
        translated = translator.translate(text, dest=target_language)
        translated_text = translated.text

        # Debugging output
        print(f"Original: {text}")
        print(f"Translated: {translated_text}")

        return jsonify({'translated_text': translated_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)

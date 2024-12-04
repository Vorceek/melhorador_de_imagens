from io import BytesIO
from flask import Flask, render_template, request, send_file
from PIL import Image, ImageEnhance

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "Nenhum arquivo enviado", 400

    file = request.files['file']

    if file.filename == '':
        return "Nenhum arquivo selecionado", 400

    if file:
        file_content = BytesIO(file.read())
        file_content.seek(0)

        image = Image.open(file_content)

        enhancer = ImageEnhance.Contrast(image)
        enhanced_image = enhancer.enhance(1.3)

        img_output = BytesIO()
        enhanced_image.save(img_output, format="PNG")
        img_output.seek(0)

        return send_file(img_output, as_attachment=True, download_name="imagem_processada.png", mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)

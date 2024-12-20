from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

# Endpoint para receber as informações e salvar em JSON
@app.route('/save', methods=['POST'])
def save():
    data = request.json

    # Validar os dados recebidos
    if not all(key in data for key in ('nome', 'latitude', 'longitude', 'descricao')):
        return jsonify({"error": "Invalid data. All fields are required: 'nome', 'latitude', 'longitude', 'descricao'"}), 400

    try:
        # Tentar carregar dados existentes
        try:
            with open('data.json', 'r') as file:
                content = json.load(file)
                # Certifique-se de que o conteúdo é uma lista
                if isinstance(content, list):
                    data_list = content
                else:
                    data_list = [content]  # Converte objeto em lista
        except FileNotFoundError:
            # Arquivo não existe, cria uma lista vazia
            data_list = []

        # Adicionar o novo registro
        data_list.append(data)

        # Salvar de volta no arquivo
        with open('data.json', 'w') as file:
            json.dump(data_list, file, ensure_ascii=False, indent=4)

    except Exception as e:
        return jsonify({"error": f"Failed to save data: {str(e)}"}), 500

    return jsonify({"message": "Data saved successfully"}), 200

# Rota para o Front-End
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
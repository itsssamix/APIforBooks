from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
    'id': 1,
    'título do livro': "Vidas secas",
    'Autor': 'Graciliano Ramos'
    },
    {
        'id': 2,
        'Título do livro': 'A paixão segundo GH',
        'Autor': 'Clarice Lispector'

    },
    {
        'id': 3,
        'Título do livro': 'A metamorfose',
        'Autor': 'Franz Kafka'

    },
    {
        'id': 4,
        'Título do livro': 'O avesso da pele',
        'Autor': 'Jefferson Tenório'

    }
]
## essa rota é capaz de retornar todos os livros do dicionário.
@app.route('/livros')
def obter_livros():
    return jsonify(livros)

## essa rota obtém os dados de uma obra pelo ID.
@app.route('/livros/<int:id>',methods=['GET'])
def obter_obra_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

## essa rota é capaz de alterar as informações de um  livro através do parametro id do livro.
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_obra_por_id(id):
    obra_alterada = request.get_json()
    for indice,obra in enumerate(livros):
        if obra.get('id') == id:
            livros[indice].update(obra_alterada)
            return jsonify(livros[indice])

## essa rota é capaz de incluir um novo livro.
@app.route('/livros',methods=['POST'])
def incluir_obra():
    nova_obra = request.get_json()
    livros.append(nova_obra)

    return jsonify(livros)

## essa rota é capaz de excluir um livro do dicionário (passando id como parametro)
@app.route('livros/<int:id>',methods=['DELETE'])
def excluir_obra(id):
    for indice, obra in enumerate(livros):
        if obra.get('id') == id:
            del livros[indice]

if __name__ ==  '__main__':
    app.run(debug=True)

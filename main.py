from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb+srv://xxxxx:xxxx@cluster0.trjlbpz.mongodb.net/?retryWrites=true&w=majority')
db = client['faculdade']
collection = db['alunos']


def criar_aluno(nome, curso, periodo, disciplinas):
    aluno = {
        "nome": nome,
        "curso": curso,
        "periodo": periodo,
        "disciplinas": disciplinas
    }
    return collection.insert_one(aluno).inserted_id


def listar_alunos():
    return list(collection.find())


def buscar_aluno_por_id(aluno_id):
    return collection.find_one({"_id": ObjectId(aluno_id)})


def atualizar_aluno(aluno_id, atualizacoes):
    return collection.update_one({"_id": ObjectId(aluno_id)}, {"$set": atualizacoes})


def deletar_aluno(aluno_id):
    return collection.delete_one({"_id": ObjectId(aluno_id)})


if __name__ == "__main__":
    aluno_id = criar_aluno("Henrique Pacini", "Ciência da Computação", 5,
                           ["Modelagem Computacional", "Inteligência Artificial"])
    print("Aluno criado com ID:", aluno_id)

    print("Listando todos os alunos:")
    alunos = listar_alunos()
    for aluno in alunos:
        print(aluno)

    atualizar_aluno(aluno_id, {"curso": "Engenharia de Software"})
    print("Aluno atualizado.")

    aluno = buscar_aluno_por_id(aluno_id)
    print("Dados do aluno:", aluno)

    deletar_aluno(aluno_id)
    print("Aluno deletado.")

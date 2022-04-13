from pymongo import MongoClient

from pprint import pprint
# pip install pymongo

class MongoConnect():

    def __init__(self):
        self.cliente = MongoClient('localhost', 27017)
        self.banco = self.cliente.teste  # nome do banco
        self.colecao = self.banco.aluno  # nome da coleção

    def save(self, json):
        try:
            self.colecao.insert_one(json)
        except Exception as e:
            print("problema ao salvar registro")
            print(json)
            print(e)

    def update(self, json, fields):
        try:
            self.colecao.update(json, fields)
        except Exception as e:
            print("problema ao UPDATE registro")
            print(json)
            print(e)


    def delete(self, json):
        try:
            self.colecao.remove(json)
        except Exception as e:
            print("problema ao DELETAR registro")
            print(json)
            print(e)

    def read(self, json=None): #,escondido=None
        try:
            for vai_la in self.colecao.find(json): #,escondido
                pprint(vai_la)
        except Exception as e:
            print("problema ao MOSTRAR registro")
            print(json)
            print(e)

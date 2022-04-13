from conexao import MongoConnect

class Aluno():

    def __init__(self):
        self.conexao = MongoConnect()

    def save(self, name, sobrenome, profissao):
        conexao = MongoConnect()
        aluno = {'name': name, 'sobrenome': sobrenome, 'profissao': profissao}
        conexao.save(aluno)

    def cadastrar(self):
        nome = input("Digite o nome do aluno: ")
        sobrenome = input(f'Digite o sobrenome ')
        profissao = input(f'Digite a sua profissao: ')

        aluno = {"Nome": nome, "Sobrenome": sobrenome, "Profissao": profissao}

        self.conexao.save(aluno)

    def excluir(self):
        find = input("Digite o nome para excluir: ")
        self.conexao.delete({"Nome": find})

    def mostrar(self):
        #Passa os campos que não quer motrar...
        self.conexao.read({"Nome": "Cima"})

    def atualizar(self):
        atualiza = input("Digite o nome atual do aluno: ")

        nome = input("Digite o novo nome do aluno: ")
        sobrenome = input(f'Digite o sobrenome ')
        profissao = input(f'Digite a sua profissao: ')

        aluno = {"Nome": nome, "Sobrenome": sobrenome, "Profissao": profissao}

        #self.conexao.update({"Nome": atualiza}, {produto})
        self.conexao.update({"Nome": atualiza}, {"$set": aluno})



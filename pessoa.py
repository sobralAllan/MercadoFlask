import this
this.name = ""
this.telephone = ""
this.address = ""
this.dateOfBorn = "01/01/1999"

def cadastrar(nome, telefone, endereco, dataDeNascimento):
    this.name = nome
    this.telephone = telefone
    this.address = endereco
    this.dateOfBorn = dataDeNascimento

def consultar():
    resultado = "Seu nome é: {} Telefone: {} Endereço: {} Data de Nascimento: {}".format(this.name, this.telephone, this.address, this.dateOfBorn)
    return resultado


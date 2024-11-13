class Produto:
    def __init__(self, id, nome, desc, tam):  #Definindo a caracteristica dos bolos
        self.id = id
        self.nome = nome
        self.desc = desc
        self.tamanho = tam

    def __repr__(self):                       #Ver o id dos bolos
        return f"{self.id}"

bolos = [
Produto(1, "Bolo", "Um delicioso bolo de laranja", "Grande"),
Produto(2, "Bolo", "Um delicioso bolo de chocolate", "medio"),
Produto(3, "Bolo", "Um delicioso bolo de limao", "grande"),
Produto(4, "Bolo", "Um delicioso bolo de milho", "pequeno"),
Produto(5, "Bolo", "Um delicioso bolo de leite", "medio"),
Produto(6, "Bolo", "Um delicioso bolo de nata", "pequeno"),
Produto(7, "Bolo", "Um delicioso bolo de farinha de trigo", "Grande"),
Produto(8, "Bolo", "Um delicioso bolo de cenoura", "Grande"),
Produto(9, "Bolo", "Um delicioso bolo de aimpin", "Grande"),
Produto(10, "Bolo", "Um delicioso bolo de brigadeiro com leite Ninho e nozes", "Grande")
]                                            #Bolos

print(bolos)                                 #printar id dos bolos


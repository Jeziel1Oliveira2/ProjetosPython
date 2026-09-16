import json
import phonenumbers

#Criação da classe Contato 
class Contato:
    #Constructor da classe Contato
    def __init__(self, nome, telefone, email):
        self.verificarNome(nome)
        self.verificarTelefone(telefone)
        self.verificarEmail(email)

    #Método para fazer a autenticação do nome do contato e definir o nome do contato com as primeiras letras maiúsculas
    def verificarNome(self, nome):
        if any(caracter.isdigit() for caracter in nome):
            raise ValueError(f"O nome {nome} é inválido, pois contém números.") 
        else:
            self.nome = nome.title()
            return self.nome

    #Método para fazer a autenticação do telefone do contato e definir o telefone do contato
    def verificarTelefone(self, telefone):
        try:
            numero = phonenumbers.parse(telefone, "BR")
            if not phonenumbers.is_valid_number(numero):
                raise ValueError(f"O telefone {telefone} é inválido.")
            
            self.telefone = telefone

        except phonenumbers.NumberParseException:
            raise ValueError(f"O formato do telefone,{telefone}, é inválido.")

    #Método para fazer a autenticação do email e definir o email do contato
    def verificarEmail(self, email):
        if "@" not in email or "." not in email.split("@")[-1]:
            raise ValueError(f"O email {email} é inválido.")
        
        self.email = email
            
    #Métotodo para printar os dados do contato
    def __str__(self):
        return f"nome: {self.nome} \ntelefone: {self.telefone} \nemail: {self.email}"

    #Método para converter os dados do contato em um dícionario, para poder ser salvo em um arquivo JSON
    def para_dicionario(self):
        return {
            "nome": self.nome,
            "telefone": self.telefone,
            "email": self.email
        }
    #Método alternativo para fazer a conversão para dicionário
    """
    def para_dicionario(self):
        retunr self.__dict__
    """

#Criação da classe gerenciador de contatos
class GerenciadorContatos:

    #Constructor da classe GerenciadorContatos
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.contatos = []
        self.carregarContatos()

    #Método que adiciona um contato na lista de contatos e salva no arquivo JSON
    def adicionarContato(self, contato):
        self.contatos.append(contato)
        self.salvarContatos()

    #Método que salva os contatos no arquivo JSON
    def salvarContatos(self):
        with open (self.arquivo, 'w', encoding='utf-8') as f:
            json.dump([contato.para_dicionario() for contato in self.contatos], f, indent=4)

    #Método que lista os contatos salvos no arquivo JSON
    def listarContatos(self):
        if not self.contatos:
            print("Nenhum contato encontrado.")
            return
        for contato in self.contatos:
            print(contato)
            print("-" * 30)

    #Método que carrega os contatos do arquivo JSON
    def carregarContatos(self):
        try: 
            with open(self.arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                for dado in dados:
                    contato = Contato(dado["nome"], dado["telefone"], dado["email"])
                    self.contatos.append(contato)
        except FileNotFoundError:
            pass 

#Programa principal
gerenciador = GerenciadorContatos("contatos.json")

#Menu de opções para o usuário
while True:
    print("1- Adicionar contato")
    print("2- Listar contatos")
    print("3- Sair")
    opcao = input("Escolha uma opcao:")

    #Verifica a opção escolhida pelo usuário e executa a ação correspondente
    if opcao == "1":
        nome = input("Digite o nome do contato:")
        telefone = input("Digite o telefone do contato:")
        email = input("Digite o email do contato:")
        try:
            contato = Contato(nome, telefone, email)
            gerenciador.adicionarContato(contato)
        except ValueError as e:
            print(e)
    elif opcao == "2":
        gerenciador.listarContatos()
    elif opcao == "3":
        break 
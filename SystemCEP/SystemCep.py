import requests
import csv

#Criação da classe Address
class Address:
    #Constructor da classe Address
    def __init__(self, zipCode, street, neighborhood, city, state):
        self.zipCode = zipCode
        self.street = street
        self.neighborhood = neighborhood
        self.city = city
        self.state = state

    #Método para printar os dados do endereço
    def __str__(self):
        return f"CEP: {self.zipCode} \nLogradouro: {self.street} \nBairro: {self.neighborhood} \nCidade: {self.city} \n UF: {self.state}"
    
#Criação da classe CepSearcher
class CepSearcher:
    #Constructor da classe CepSearcher
    def __init__(self,csvFile):
        self.csvFile = csvFile

    #Método para fazer a busca do CEP na API e retornar os dados do endereço
    def searchCep(self, zipCode):
        url = f"https://viacep.com.br/ws/{zipCode}/json/"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            address = Address(
                data["cep"],
                data["logradouro"],
                data["bairro"],
                data["localidade"],
                data["uf"]
            )
            self.saveHistory(address)
            return address

        else:
            print("CEP informado não foi encontrado")
            return None

    #Método que salva o histórico das buscas em um arquivo CSV
    def saveHistory(self, address):
        with open(self.csvFile, mode = "a", newline = "", encoding = "utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([address.zipCode, address.street, address.neighborhood, address.city, address.state])

    #Método que lista o histórico de buscas salvo no arquivo CSV
    def showHistory(self):
        try:
            with open(self.csvFile, mode = "r", encoding = "utf-8") as file:
                reader = csv.reader(file)
                history = list(reader)
                if not history:
                    print(f"Nenhuma busca foi realizada.")
                for row in history:
                    print(f"CEP: {row[0]}\nLogradouro: {row[1]}\nBairro: {row[2]}\nCidade: {row[3]}\nUF: {row[4]}")
                    print("-"* 30)
        except FileNotFoundError:
            print("Nenhuma busca foi realizada.")

#Programa principal
searcher = CepSearcher("history.csv")

#Menu de opções para o usuário
while True:
    option = int(input("1- Buscar CEP \n2- Vizualizar o historico \n3- Sair\n"))
    
    #Verifica a opção escolhida pelo usuário e executa a ação correspondente
    match option:
        case 1:
            zipCode = input("Digite o CEP:")
            address = searcher.searchCep(zipCode)
            if address:
                print(address)
        case 2:
            searcher.showHistory()
        case 3:
            break
        case _:
            print("Opção inválida")
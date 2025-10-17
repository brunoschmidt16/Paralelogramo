def questão_1():
    class Pessoa:
        def __init__(self, nome, idade, cpf, endereço):
            self.nome = nome
            self.idade = idade
            self.cpf = cpf
            self.endereço = endereço
            print(f"Pessoa {self.nome} criado com sucesso!")

        def dados(self):
            print(f"Nome: {self.nome}")
            print(f"Idade: {self.idade}")
            print(f"CPF: {self.cpf}")
            print(f"Endereço: {self.endereço}")

    print("---Cadastro de Pessoas---")
    pessoa_nome = input("Nome: ")
    pessoa_idade = int(input("Idade: "))
    pessoa_cpf = input("CPF: ")
    pessoa_endereço = input("Endereço: ")
    pessoa = Pessoa(pessoa_nome, pessoa_idade, pessoa_cpf, pessoa_endereço)
    pessoa.dados()

def questão_2():
    class Funcionário:
        def __init__(self, nome, salario):  
            self.nome = nome
            self.salario = salario
            print(f"Funcionário logado com sucesso!") 

        def dados(self):
            print(f"Nome: {self.nome}")
            print(f"Salário atual: R$ {self.salario:.2f}")
            print(f"Salário com reajuste: R$ {self.salario + 100:.2f}")

    print("---Reajuste de Salários---")
    funcionário_nome = input("Nome: ")
    funcionário_salário = float(input("Salário: "))
    funcionário = Funcionário(funcionário_nome, funcionário_salário)
    funcionário.dados()
            
def questão_3():
    class Funcionário:
        def __init__(self, nome, salario, entrada, rg):  
            self.nome = nome
            self.salario = salario
            self.entrada = entrada
            self.rg = rg
            print(f"\nFuncionário registrado com sucesso!") 
        
        def aumentarSalário(self):
            aumento = 1000
            self.salario += aumento
            print(f"Salário de {self.nome} aumentado para R$ {self.salario:.2f}")
        
        def consultarSalário(self):
            print(f"Salário atual: R$ {self.salario:.2f}")

        def calcularGanhoAnual(self):
            ganho_anual = self.salario * 12
            print(f"Ganho anual: R$ {ganho_anual:.2f}")
        
        def dados(self):
            print(f"Nome: {self.nome}")
            print(f"Salário: R$ {self.salario:.2f}")
            print(f"Data de entrada: {self.entrada}")
            print(f"RG: {self.rg}")

    print("---Registro de Funcionário---")
    funcionário_nome = input("Nome: ")
    funcionário_salário = float(input("Salário: "))
    funcionário_entrada = input("Data de entrada: ")
    funcionário_rg = input("RG: ")
    funcionário = Funcionário(funcionário_nome, funcionário_salário, funcionário_entrada, funcionário_rg)
    funcionário.dados()

    print("\n---Consultas---")
    funcionário.consultarSalário()
    funcionário.aumentarSalário()
    funcionário.calcularGanhoAnual()

def questão_4():
    class Apolice:
        def __init__(self, apolice, nomeSegurado, idade, valorPrêmio):  
            self.apolice = apolice
            self.nomeSegurado = nomeSegurado
            self.idade = idade
            self.valorPrêmio = valorPrêmio
            print(f"\nApólice criada com sucesso!") 
        
        def imprimir(self):
            print(f"Nome do segurado: {self.nomeSegurado}")
            print(f"Idade: {self.idade}")
            print(f"Número da apólice: {self.apolice}")
            print(f"Valor do prêmio: R$ {self.valorPrêmio:.2f}")

        def calcularPremioApolice(self):
            if 18 < self.idade <= 25:
                valor = self.valorPrêmio + (self.valorPrêmio * 20)/100.
            elif 26 <= self.idade <= 36:
                valor = self.valorPrêmio + (self.valorPrêmio * 15)/100.
            else:
                valor = self.valorPrêmio + (self.valorPrêmio * 10)/100.
            
            print(f"Valor do prêmio atualizado: R$ {valor:.2f}")
        

    print("---Cadastro de Apólice---")
    apolice_id = int(input("Número da apólice: "))
    apolice_nome = input("Nome do segurado: ")
    apolice_idade = int(input("Idade: "))
    apolice_valor = float(input("Valor do prêmio: "))
    apolice = Apolice(apolice_id, apolice_nome, apolice_idade, apolice_valor)
    apolice.imprimir()

    print("\n---Consultas---")
    apolice.calcularPremioApolice()
    
def questão_5():
    class Eleitoral:
        def __init__(self, nome, idade, título):  
            self.nome = nome
            self.idade = idade
            self.título = título
            print(f"\nEleitor registrado com sucesso!") 
        
        def mostrarDados(self):
            print(f"Nome: {self.nome}")
            print(f"Idade: {self.idade}")
            print(f"Título de eleitor: {self.título}")

        def verificar(self):
            if self.idade < 16:
                print("Eleitor não pode votar")
            elif 16 <= self.idade < 18 or self.idade > 70:
                print("Voto facultativo")
            else:
                print("Eleitor deve votar")
    
    print("---Registro de Eleitor---")
    eleitor_nome = input("Nome: ")      
    eleitor_idade = int(input("Idade: "))
    eleitor_título = input("Título de eleitor: ")
    eleitor = Eleitoral(eleitor_nome, eleitor_idade, eleitor_título)
    eleitor.mostrarDados()

    print("\n---Consulta de Votação---")
    eleitor.verificar()

def main():
    while True:
        print("\n---Menu de Exercícios---")
        print("1. Questão 1 - Cadastro de Pessoas")
        print("2. Questão 2 - Reajuste de Salários")
        print("3. Questão 3 - Registro de Funcionário")
        print("4. Questão 4 - Cadastro de Apólice")
        print("5. Questão 5 - Registro de Eleitor")
        print("6. Sair")
        
        escolha = input("Escolha uma opção (1-6): ")
        
        if escolha == '1':
            questão_1()
        elif escolha == '2':
            questão_2()
        elif escolha == '3':
            questão_3()
        elif escolha == '4':
            questão_4()
        elif escolha == '5':
            questão_5()
        elif escolha == '6':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")   
main()        

            

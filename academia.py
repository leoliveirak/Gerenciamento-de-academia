import random

class Aluno:
    def __init__(self, matricula, nome, cpf, altura, peso):
        self.matricula = matricula
        self.nome = nome
        self.cpf = cpf
        self.altura = altura
        self.peso = peso
        self.exercicios = []
        self.status = False
    
    def calcular_imc(self):
        self.imc = (self.peso)/((self.altura)**2)

    def exibir_aluno(self):
        print("\n\nMatrícula:", self.matricula)
        print("Nome:", self.nome)
        print("Altura:", self.altura)
        print("Peso:", self.peso)
        print("CPF:", self.cpf)
        print("IMC: {:.2f}".format(self.imc))
        print("Status: Ativo" if self.status else "Status: Inativo")
        print("\n======================")
        print("      EXERCÍCIOS:     ")
        print("\n======================")
        
        if self.exercicios:
            for exercicio in self.exercicios:
                print(f"Exercício: {exercicio['nome']}")
                print(f"Carga (kg): {exercicio['carga']}")
                print(f"Séries: {exercicio['series']}")
                print(f"Repetições: {exercicio['repeticoes']}")
                print("----------------------")

        else:
            print("O aluno não possúi cadastro de exercício")

class Academia:
    def __init__(self):
        self.alunos = []
    
    def cadastro(self):
        matricula = self.matricula()
        print(f"Matrícula: {matricula}")
        nome = input("Nome do aluno: ")
        cpf = input("CPF do aluno: ")
        altura = float(input("Altura do aluno (m): "))
        peso = float(input("Peso do aluno (kg): "))
        aluno = Aluno(matricula, nome, cpf, altura, peso)
        aluno.calcular_imc()
        aluno.status = False
        self.alunos.append(aluno)
        print("Cadastro finalizado")
        print("Você pode adicionar uma lista de treino pelo índice 3 do menu")

    def matricula(self):
        matricula = random.randint(1, 2000)
        while self.verificar_matricula(matricula):
            matricula = random.randint(1, 2000)
        return matricula

    def verificar_matricula(self, matricula):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                return True
        return False
    
    def exluir_cadastro(self, matricula):
        matricula = int(matricula)
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                print("\nConfirme as informações do aluno que deseja excluir:")
                aluno.exibir_aluno()
                print()
                print("Confirme sua decisão")
                print("Cuidado, pois esta ação é irreversível")
                print("[1] Excluir")
                print("[2] Cancelar")
                confirmacao = int(input())
                if confirmacao == 1:
                    self.alunos.remove(aluno)
                    print("Cadastro excluído com sucesso!")
                else:
                    print("Operação cancelada!")
                return
        print("Aluno não encontrado")

    def atualizar_cadastro(self, matricula):
        aluno = self.buscar_aluno_por_matricula(matricula)
        if aluno:
            print("Altere os seguintes dados: ")
            print("Caso deseje alterar NOME ou CPF, exclua o aluno e faça um novo cadastro")
            altura = float(input("\nNova altura do aluno (m): "))
            peso = float(input("Novo peso do aluno (kg): "))
            aluno.status = self.status_aluno(aluno)
            aluno.calcular_imc()
            print("Dados atualizados!")

    def buscar_aluno_por_matricula(self, matricula):
        matricula = int(matricula)
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                return aluno
        return None

    def encontrar_aluno_e_exibir(self):
        consulta = input("Digite a MATRÍCULA, NOME ou CPF do aluno: ")
        encontrado = False
        for aluno in self.alunos:
            if(str(aluno.matricula) == consulta or aluno.nome.lower() == consulta.lower() or aluno.cpf == consulta):
                aluno.exibir_aluno()
                encontrado = True
            if not encontrado:
                print("Aluno não encontrado!")
            
    def gerenciamento_treino(self, matricula):
        aluno = self.buscar_aluno_por_matricula(matricula)
        if aluno:
            aluno.status = True
            print("========== Gerenciamento de Treino ==========")
            print("[1] Adicionar exercício(s)")
            print("[2] Editar exercício existente")
            print("[3] Excluir exercício")
            print("[4] Excluir todos os exercícios")
            print("=============================================")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                qtd_exercicios = int(input("Quantos exercícios deseja adicionar? "))
                for i in range(qtd_exercicios):
                    nome_exercicio = input("Nome do exercício: ")
                    carga_exercicio = float(input("Peso do exercício (kg): "))
                    series_exercicio = int(input("Numero de séries: "))
                    repeticoes_exercicio = int(input("Número de repetições: "))
                    exercicio = {'nome': nome_exercicio, 'carga': carga_exercicio, 'series': series_exercicio, 'repeticoes': repeticoes_exercicio}
                    aluno.exercicios.append(exercicio)
                print("Exercícios adicionados com sucesso!")
            
            elif(opcao == "2"):
                if aluno.exercicios:
                    print("Exercícios disponíveis: ")
                    for j, exercicio, in enumerate(aluno.exercicios):
                        print(f"[{j}] {exercicio['nome']}")
                    indice = int(input("Digite o índice que deseja editar: "))
                    if 0 <= indice < len(aluno.exercicios):
                        exercicio = aluno.exercicios[indice]
                        carga_exercicio = float(input("Nova carga (kg): "))
                        series_exercicio = float(input("Nova quantidade de séries: "))
                        repeticoes_exercicio = int(input("Nova quantidade de repetições: "))
                        exercicio['carga'] = carga_exercicio
                        exercicio['series'] = series_exercicio
                        exercicio['repeticoes'] = repeticoes_exercicio
                        print("Exercício alterado com sucesso!")
                    else:
                        print("Opção inválida")
                else:
                    print("O aluno não possúi cadastro de exercício")
            
            elif(opcao == "3"):
                if aluno.exercicios:
                    print("Exercícios disponíveis: ")
                    for k, exercicio in enumerate(aluno.exercicios):
                        print(f"[{k}] {exercicio['nome']}")
                    indice = int(input("Digite o índice do exercício a ser excluído: "))
                    if 0 <= indice < len(aluno.exercicios):
                        exercicio = aluno.exercicios[indice]
                        aluno.exercicios.remove(exercicio)
                        aluno.status = self.status_aluno(aluno)
                        print("Exercício excluído!")
                    else:
                        print("Opção inválida!")
                else:
                    print("Nenhum exercício cadastrado!")
            
            elif opcao == "4":
                if aluno.exercicios:
                    aluno.exercicios = []
                    print("Todos os exercícios foram excluídos!")
                else:
                    print("Nenhum exercício cadastrado!")
                aluno.status = self.status_aluno(aluno)
            else:
                print("Opção inválida!")
        else:
            print("Aluno não encontrado!")
    
    def relatorio(self):
        print("\nRELATÓRIO DE ALUNOS:")
        busca = input("Digite o filtro desejado\n[T]odos\n[A]tivos\n[I]nativos\n").upper()
        alunos_relatorio = []
        if busca == "T":
            alunos_relatorio = self.alunos
        elif busca == "A":
            alunos_relatorio = [aluno for aluno in self.alunos if aluno.status]
        elif busca == "I":
            alunos_relatorio = [aluno for aluno in self.alunos if not aluno.status]
        else:
            print("Opção inválida!")
            return
        alunos_relatorio = sorted(alunos_relatorio, key=lambda aluno: aluno.nome)
        
        if alunos_relatorio:
            for aluno in alunos_relatorio:
                aluno.exibir_aluno()
                print("--------------------")
        else:
            print("Nenhum aluno encontrado!")
    
    def status_aluno(self, aluno):
        if aluno.exercicios:
            return len(aluno.exercicios) > 0

academia = Academia()

while True:
    print(" ==============================")
    print("|        FitLab UFFS          |")
    print(" ==============================")
    print("| 1 - Cadastrar aluno         |")
    print("| 2 - Excluir aluno           |")
    print("| 3 - Gerenciar treino        |")
    print("| 4 - Consultar aluno         |")
    print("| 5 - Atualizar cadastro      |")
    print("| 6 - Relatório de alunos     |")
    print("| 7 - Sair                    |")
    print(" ------------------------------")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        academia.cadastro()
    elif opcao == "2":
        matricula = input("Matrícula do aluno: ")
        academia.exluir_cadastro(matricula)
    elif opcao == "3":
        matricula = input("Matrícula do aluno: ")
        academia.gerenciamento_treino(matricula)
    elif opcao == "4":
        academia.encontrar_aluno_e_exibir()
    elif opcao == "5":
        matricula = input("Matrícula do aluno: ")
        academia.atualizar_cadastro(matricula)
    elif opcao == "6":
        academia.relatorio()
    elif opcao == "7":
        print("Saindo...")
        break
    else:
        print("Opção inválida, tente novamente!")

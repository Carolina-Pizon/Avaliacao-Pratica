
class Servico:
    def __init__(self, nome, preco, desconto):
        self.nome = nome
        self.preco = preco
        self.desconto = desconto

    def aplicar_desconto(self):
        valor_desconto = self.preco * self.desconto / 100
        return self.preco - valor_desconto


class Cliente:
    def __init__(self, nome):
        self.nome = nome


class Atendimento:
    def __init__(self, cliente, servico):
        self.cliente = cliente
        self.servico = servico

    def exibir_resumo(self):
        valor_desconto = (
            self.servico.preco * self.servico.desconto / 100
        )

        valor_final = self.servico.aplicar_desconto()

        print("\n========== SPA DELUXE ==========")
        print(f"Nome: {self.cliente.nome}")
        print(f"Servico escolhido: {self.servico.nome}")
        print(f"Preco original: R$ {self.servico.preco:.2f}")
        print(f"Desconto aplicado: {self.servico.desconto}%")
        print(f"Valor do desconto: R$ {valor_desconto:.2f}")
        print(f"Total a pagar: R$ {valor_final:.2f}")
        print("================================")


class SpaDeluxe:
    def __init__(self):
        self.servicos = [
            Servico("SPA dos pes", 150.00, 10),
            Servico("SPA das maos", 160.00, 10),
            Servico("Manicure", 50.00, 0),
            Servico("Pedicure", 50.00, 0),
            Servico("Massagem", 100.00, 15)
        ]

    def exibir_menu(self):
        print("\n========== SPA DELUXE ==========")
        print("Seja bem-vindo(a)! Escolha o servico desejado:\n")

        for numero, servico in enumerate(self.servicos, start=1):
            print(
                f"{numero} - {servico.nome} "
                f"| R$ {servico.preco:.2f}"
            )

        print("\n0 - Sair")
        print("================================")

    def selecionar_servico(self):
        while True:
            self.exibir_menu()

            try:
                opcao = int(input("\nQual servico voce deseja realizar? "))

            except ValueError:
                print("\nOpcao invalida! Digite um numero.")
                continue

            if opcao == 0:
                return None

            if 1 <= opcao <= len(self.servicos):
                return self.servicos[opcao - 1]

            print("\nOpcao invalida! Escolha um servico do menu.")

    def executar(self):
        print("\nBEM-VINDO(A) AO SPA DELUXE!")

        while True:
            # Cliente escolhe o servico pelo menu
            servico = self.selecionar_servico()

            if servico is None:
                print("\nObrigado por escolher o SPA DELUXE!")
                print("Esperamos receber voce novamente!")
                break

            # Sistema calcula o desconto automaticamente
            valor_final = servico.aplicar_desconto()

            print("\n========== SEU SERVICO ==========")
            print(f"Servico escolhido: {servico.nome}")
            print(f"Preco original: R$ {servico.preco:.2f}")
            print(f"Desconto aplicado: {servico.desconto}%")
            print(f"Total com desconto: R$ {valor_final:.2f}")
            print("=================================")

            # Solicita os dados diretamente ao cliente
            nome = input("\nPor favor, digite seu nome: ")

            cliente = Cliente(nome)

            # Cria o atendimento
            atendimento = Atendimento(cliente, servico)

            # Exibe o resumo do atendimento
            atendimento.exibir_resumo()

            continuar = input(
                "\nDeseja escolher outro servico? (s/n): "
            ).strip().lower()

            if continuar != "s":
                print("\nObrigado por escolher o SPA DELUXE!")
                print("Esperamos receber voce novamente!")
                break


# Criando o sistema
sistema = SpaDeluxe()

# Iniciando o aplicativo
sistema.executar()

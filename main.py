from dados_paciente import criar_tabela_de_pacientes
from dados_paciente import cadastrar_paciente
from dados_paciente import criar_tabela_consultas
from dados_paciente import buscar_paciente
from dados_paciente import buscar_consulta
from dados_paciente import cadastrar_consulta

def menu() -> str:
    escolha: int = input("""

    Digite 0 para sair! \n
    Digite 1 para cadastrar um paciente.\n 
    Digite 2 para cadastrar uma consulta. \n
    Digite 3 para listar pacientes \n
    Digite 4 para listar consultar.\n
    Digite 5 para buscar um paciente. \n
    Digite 6 para buscar uma consulta \n 
    Digite 7 para editar um paciente. \n 
    Digite 8 para editar uma consulta. \n
    Digite 9 para excluir um paciente. \n
    Digite 10 para excluir uma consulta.

    """)

    return escolha

criar_tabela_de_pacientes()
criar_tabela_consultas()


while True:

        match menu():
            case "0":
                break
            case "1":
                cadastrar_paciente()

            case "2":
                cadastrar_consulta()

            case "3":
                pass

            case "4":
                pass

            case "5":
                
                buscar_paciente(cpf_busca = input("Digite o CPF do paciente!\n"))

            case "6":
                buscar_consulta()
        
            case "7":
                pass

            case "8":
                pass

            case "9":
                pass

            case "10":
                pass
        
import pickle
import os

from pip._vendor.distlib.compat import raw_input

arquivo = open('candidatos.db', 'wb')
for i in range(10):
    pickle.dump(i, arquivo)
arquivo.close()

print('Arquivo criado com sucesso!')

db = {}


def mostraMenu():
    os.system('clear')
    print('Existe ' + str(len(db)) + ' candidatos cadastrados\n\n')
    print('Escolha uma opção:')
    print('1 - Incluir Candidato')
    print('2 - Consultar Candidato')
    print('3 - ALterar Candidato')
    print('4 - Excluir Candidato')
    print('5 - Listar Candidatos')
    print('6 - Sair')
    return int(raw_input(''))


def registroExistente(codigo):
    duplicated = False
    if codigo in db.keys():
        duplicated = True

    return duplicated


def include():
    candidato = {}

    codigo = raw_input('Digite o código do candidato:\n')

    if registroExistente(codigo):
        print('Código de candidato já existente, informe outro código!')
        include()
    else:
        populaCandidato(candidato, codigo)
        db[codigo] = candidato

        main()


def mostraCandidato(codigo):
    print('Código do Candidato: ' + db[codigo]['codigo'])
    print('Nome do Candidato: ' + db[codigo]['nome'])
    print('Cargo do Candidato: ' + db[codigo]['cargo'])
    print('Região do Candidato: ' + db[codigo]['regiao'])
    print('Votos do Candidato: ' + str(db[codigo]['votos']))


def show():
    codigo = raw_input('Digite o código do Candidato\n')
    if registroExistente(codigo):
        mostraCandidato(codigo)
        trash = raw_input('pressione para voltar ao menu\n')
        main()
    else:
        print('Registro não encontrado')
        trash = raw_input('pressione para voltar ao menu\n')
        main()


def alterar():
    candidatoAlteracao = {}

    codigo = raw_input('Digite o código do Candidato\n')

    if registroExistente(codigo):
        populaCandidato(candidatoAlteracao, codigo)

        db[codigo] = candidatoAlteracao

        main()
    else:
        print('Registro não encontrado')
        trash = raw_input('pressione para voltar ao menu\n')
        main()


def populaCandidato(candidato, codigo):
    candidato['codigo'] = codigo
    candidato['nome'] = raw_input('Digite o Nome do Candidato:\n')
    candidato['cargo'] = raw_input('Digite o Cargo do Candidato:\n')
    candidato['regiao'] = raw_input('Digite a Região do Candidato:\n')
    candidato['votos'] = float(raw_input('Digite o número de Votos do Candidato\n'))


def delete():
    codigo = raw_input('Digite o código do Candidato:\n')

    if registroExistente(codigo):
        del (db[codigo])
        print('Registro apagado com sucesso!')
        trash = raw_input('pressione para voltar ao menu\n')
        main()
    else:
        print('Registro não encontrado')
        trash = raw_input('pressione para voltar ao menu\n')
        main()


def listar():
    if len(db) > 0:
        for codigo in db.keys():
            mostraCandidato(codigo)
            print('-' * 10)
        trash = raw_input('pressione para voltar ao menu\n')
        main()
    else:
        print('Não há registros para serem exibidos')
        trash = raw_input('pressione para voltar ao menu\n')
        main()


def main():
    option = mostraMenu()
    if option == 1:
        include()
    elif option == 2:
        show()
    elif option == 3:
        alterar()
    elif option == 4:
        delete()
    elif option == 5:
        listar()
    elif option == 6:
        print('Saindo do programa de Candidatos')
        exit()
    else:
        print('Comando inválido, tente outra opção')
        main()


main()

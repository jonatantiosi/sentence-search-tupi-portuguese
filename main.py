import os
import json

# acervo de frases:
# cada frase e tradução tem um dicionário próprio em uma lista
# portanto a formatação fica do seguinte jeito
# [ [{"Frase": "frase"},{"Tradução": "tradução"}]  ]
#
# acervo de palavras:
# cada palavra com sua tradução é composta em um dicionário
# e.g. { "Palavra (na íntegra)": "significado da palavra"}

CAMINHO_ARQUIVO_FRASES = 'acervo_frases.json'
CAMINHO_ARQUIVO_PALAVRAS = 'acervo_palavras.json'


def carregar_acervo(CAMINHO_ARQUIVO):
    if not os.path.exists(CAMINHO_ARQUIVO):
        # se nenhum arquivo existir criar um novo usando último hardcoded log
        # do acervo
        return []

    try:
        with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except (json.JSONDecodeError, FileNotFoundError):
        # arquivo vazio ou corrompido reinicia com último hardcoded log do
        # acervo
        return []


def salvar_acervos(acervo_palavras, acervo_frases):
    with open(CAMINHO_ARQUIVO_PALAVRAS, 'w', encoding='utf-8') as arquivo:
        # ensure ascii false para manter os caracteres como estão
        json.dump(acervo_palavras, arquivo, ensure_ascii=False, indent=2)
    with open(CAMINHO_ARQUIVO_FRASES, 'w', encoding='utf-8') as arquivo:
        # ensure ascii false para manter os caracteres como estão
        json.dump(acervo_frases, arquivo, ensure_ascii=False, indent=2)


def limpar_menu():
    '''limpa o terminal para windows e linux/mac'''
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    opcao = input(
        "[1] Pesquisar palavra\n"
        "[2] Adicionar nova frase\n"
        "[3] Adicionar nova palavra\n"
        "[4] Sair\n"
    )
    return opcao


def pesquisar_palavra(palavra_pesquisada) -> tuple[str, str]:
    '''Pesquisa a palavra no acervo de frases e retorna
    uma tupla com a frase se houver e traducao
    '''
    for acervo in acervo_frases:
        # strip para garantir pesquisa mesmo com espaços extras ou aspas
        if palavra_pesquisada in acervo[0]["Frase"].strip():
            return (acervo[0]["Frase"], acervo[1]["Traducao"])
    raise Exception


def buscar_definicao(palavra_pesquisada):
    '''Retorna a definição da palavra'''
    for dicionario in acervo_palavras:
        if palavra_pesquisada in dicionario:
            return dicionario[palavra_pesquisada]

    raise Exception


def adicionar_frase(frase, traducao):
    '''adiciona a frase e traducao digitadas pelo usuario'''
    acervo_frases.append([{"Frase": frase}, {"Traducao": traducao}])


def adicionar_palavra(palavra, definicao):
    '''adiciona palavra com a respectiva definição em formato de dicionário
    à lista acervo_palavras'''
    acervo_palavras.append({palavra: definicao})


def mensagem_agradecimento(quantidade_palavras, quantidade_frases):
    '''imprime a quantidade de frases e palavras registradas pelo usuário
    caso ele faço algum registro'''
    print("Obrigado pela contribuição!\n")
    if quantidade_frases:
        print(f'{quantidade_frases} nova(s) frase(s) adicionadas.')
    if quantidade_palavras:
        print(f'{quantidade_palavras} nova(s) palavra(s) adicionadas.')


acervo_frases = carregar_acervo(CAMINHO_ARQUIVO_FRASES)
acervo_palavras = carregar_acervo(CAMINHO_ARQUIVO_PALAVRAS)

# contadores para mensagem final
palavras_adicionadas = 0
frases_adicionadas = 0

print('Busca de sentenças em Tupi-Português\n')

while True:

    opcao = menu()

    match opcao:

        case "1":
            # pesquisar palavra

            limpar_menu()
            palavra_pesquisada = input("Qual palavra deseja pesquisar?:\n")

            try:
                frase, traducao = pesquisar_palavra(palavra_pesquisada)
            except Exception:
                print('Nenhuma frase encontrada com essa palavra.')
                print()
                continue
            try:
                definicao = buscar_definicao(palavra_pesquisada)
            except Exception:
                definicao = 'Palavra sem definição.'
                print()

            print()
            print(
                f"Frase: {frase}\n"
                f"Tradução: {traducao}\n"
                f"Definição de {palavra_pesquisada}: {definicao}"
            )

            print()

        case "2":
            # adicionar frase

            limpar_menu()
            frase_adicionar = input('Digite a frase em linguagem Tupi: \n')
            traducao_adicionar = input('Digite o significado em português: \n')

            try:
                adicionar_frase(frase_adicionar, traducao_adicionar)
                frases_adicionadas += 1
                limpar_menu()
                print('Nova frase adicionada. ')
            except Exception as e:
                print(f"Erro ao adicionar a frase ({e})")

            print()

        case "3":
            # adicionar palavra

            limpar_menu()
            palavra_adicionar = input(
                'Digite a palavra que deseja adicionar: \n'
            )

            definicao_palavra = input(
                f'Digite a tradução de {palavra_adicionar} em português: \n'
            )

            try:
                adicionar_palavra(palavra_adicionar, definicao_palavra)
                palavras_adicionadas += 1
                limpar_menu()
                print(f'Palavra "{palavra_adicionar}" adicionada.')
            except Exception as e:
                print(f"Erro ao adicionar a palavra ({e})")

            print()

        case "4":
            # sair

            limpar_menu()
            if palavras_adicionadas or frases_adicionadas:
                mensagem_agradecimento(palavras_adicionadas,
                                       frases_adicionadas)
            break

        case _:  # equivalente ao else
            limpar_menu()
            print('Opção inválida, selecione um número de 1 a 4.')
            print()

salvar_acervos(acervo_palavras, acervo_frases)

import pandas as pd  # Importa a biblioteca pandas para manipulação de dados
import datetime as dt  # Importa a biblioteca datetime para manipulação de datas e horas
import os  # Importa a biblioteca os para operações de sistema de arquivos


# Classe para gerenciar logs
class ArquivoDeLog:
    def __init__(self, caminho_log="log.log"):

        # Inicializa a classe com o caminho do arquivo de log
        self.caminho_log = caminho_log

    # Função para escrever uma mensagem no log
    def log(self, msg):
        # Obtém a data e hora atual como uma string formatada
        agora_str = dt.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        # Abre o arquivo de log em modo de adição (append)
        with open(self.caminho_log, "a") as arquivo:
            # Escreve a mensagem de log junto com a data e hora
            arquivo.write(f"\n{msg}  => {agora_str}\n==========================")


# Função para carregar os dados de um arquivo CSV
def carregar_dados(caminho_arquivo, log):
    try:
        # Tenta carregar os dados do arquivo CSV
        df = pd.read_csv(caminho_arquivo, sep=';')
        return df
    except Exception as e:
        # Se ocorrer um erro, registra a mensagem de erro no log e relança a exceção
        log.log(f'Erro ao carregar dados: {e}')
        raise


# Função para filtrar valores acima de um determinado limite
def filtrar_valores_acima_limite(df, limite, log):
    try:
        # Tenta filtrar os valores da coluna 'Valor da Transação' que são maiores que o limite
        return df.loc[df['Valor da Transação'] > limite]
    except Exception as e:
        # Se ocorrer um erro, registra a mensagem de erro no log e relança a exceção
        log.log(f'Erro ao filtrar dados: {e}')
        raise


# Função para salvar os dados filtrados em um novo arquivo CSV
def salvar_dados(df, caminho_arquivo, log):
    try:
        # Tenta salvar o DataFrame no arquivo CSV
        df.to_csv(caminho_arquivo, index=True)
    except Exception as e:
        # Se ocorrer um erro, registra a mensagem de erro no log e relança a exceção
        log.log(f'Erro ao salvar dados: {e}')
        raise


# Função principal que coordena as operações
def main():
    # Inicializa o gerenciador de log
    log = ArquivoDeLog()
    # Define o caminho do arquivo de entrada e saída
    arquivo_entrada = 'planilha/transacoes.csv'
    arquivo_saida = 'planilha/transacoes_altas.csv'

    # Cria o diretório se não existir
    os.makedirs(os.path.dirname(arquivo_saida), exist_ok=True)

    try:
        # Carrega os dados do arquivo CSV de entrada
        df = carregar_dados(arquivo_entrada, log)
        # Filtra os valores acima de 1000 na coluna 'Valor da Transação'
        valores_acima_1000 = filtrar_valores_acima_limite(df, 1000, log)
        # Salva os dados filtrados no arquivo CSV de saída
        salvar_dados(valores_acima_1000, arquivo_saida, log)

        # Verifica a leitura do arquivo salvo
        df_valores_altos = pd.read_csv(arquivo_saida, sep=',')
        print(df_valores_altos.head())
    except Exception as e:
        # Se ocorrer um erro fatal, imprime a mensagem de erro e a registra no log
        print(f'Erro fatal: {e}')
        log.log(f'Erro fatal: {e}')


# Executa a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()

# Manipulação de Dados com Pandas e Registro de Logs

Este projeto em Python demonstra um sistema para manipulação de dados em formato CSV utilizando a biblioteca Pandas, além de registrar atividades em um arquivo de log. Abaixo estão detalhadas as funcionalidades principais e as instruções para utilização.

## Funcionalidades

1. **Carregamento de Dados**: 
   - Carrega dados de um arquivo CSV especificado (`planilha/transacoes.csv`) usando Pandas.

2. **Filtragem de Valores**:
   - Filtra os dados carregados, selecionando aqueles onde o valor da transação (`Valor da Transação`) é superior a 1000.

3. **Salvamento de Dados Filtrados**:
   - Salva os dados filtrados em um novo arquivo CSV (`planilha/transacoes_altas.csv`).

4. **Registro de Logs**:
   - Registra mensagens de log em um arquivo específico (`log.log`), incluindo timestamps para cada registro.

## Pré-requisitos

- Python 3.x instalado
- Pacotes necessários: Pandas

## Instalação de Dependências

1. **Instale o Pandas**:
   - Utilize o seguinte comando pip para instalar o Pandas, se ainda não estiver instalado:
     ```bash
     pip install pandas
     ```

## Execução

1. **Clone o Repositório**:
   - Clone este repositório para o seu ambiente local:
     ```bash
     git clone https://github.com/seu-usuario/nome-do-repositorio.git
     ```

2. **Executar o Script**:
   - Navegue até o diretório onde o script `main.py` está localizado.
   - Execute o script usando Python:
     ```bash
     python script_transacoes.py
     ```

3. **Entrada de Dados**:
   - O script carrega automaticamente os dados do arquivo CSV `planilha/transacoes.csv`.
   - Os dados filtrados com valores acima de 1000 serão salvos em `planilha/transacoes_altas.csv`.

## Configuração Adicional

- Certifique-se de que os arquivos de entrada e saída estejam no formato correto e no local esperado pelo script.
- Verifique o arquivo `log.log` para registrar quaisquer erros ou eventos durante a execução do script.


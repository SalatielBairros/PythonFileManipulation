# MANIPULAÇÃO ARQUIVOS PYTHON
Script criado para selecionar arquivos em um diretório (incluindo os subdiretorios) e copiar os arquivos encontrados para outro diretório.
Copia os arquivos PDFs existentes dentro dos diretórios padrões do software de emissão de NF-e UNINFE registrando tudo em logs.
Quando existir um arquivo de chave para uma nota mas não existir o PDF da mesma, é registrado no log, assim como possíveis erros e exceções na execução.

## Observações execução
- Na variável `path`, substituir o valor `YOUR_DIRECTORY` pelo diretório a ser buscado.
- Como a estrutura de pastas padrão do UNINFE depente do CNPJ da empresa, o mesmo é solicitado no início da execução.
- A execução gera um arquivo de log dentro do diretório informado na variável `baseDirectory` chamado *log.txt*.
- Foi gerado um arquivo executável utilizando o *pyinstaller* e está no diretório *dist/main.exe*.

## Objetivo
O objetivo deste repositório é um exemplo de acesso e manipulação de arquivos utilizado em uma aplicação real.
Inclui operações como listagem de arquivos de um diretório e cópia de arquivos.

###### Autor: Salatiel Bairros

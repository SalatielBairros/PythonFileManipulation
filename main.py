import glob
import os
from datetime import datetime
from ntpath import basename
from shutil import copyfile

log = "*** COPIA ARQUIVOS PDF ***\n\nINICIO: " + str(datetime.now()) + "\n"
XML_FILE_ID = "-procNFe.xml"

try:
    cnpj = input("Digite o CNPJ: ")
    path = "YOUR_DIRECTORY" + cnpj + "\\Prod\\Enviado\\Autorizados\\*\\"
    print("Buscando arquivos...")
    files = glob.glob(path + "*" + XML_FILE_ID)
    baseDirectory = "C:\\TempPDF\\" + cnpj + "\\"

    if len(files) > 0:
        print("Criando diretorio...")
        if not os.path.exists(baseDirectory):
            os.makedirs(baseDirectory)

        print("Criando diretorio...")
        for file in files:
            try:
                pdfFile = file.replace(XML_FILE_ID, ".pdf")
                if os.path.isfile(pdfFile):
                    fileName = basename(pdfFile)
                    newPath = baseDirectory + fileName
                    copyfile(pdfFile, newPath)
                    log += "\nSUCCESS - Arquivo copiado: " + fileName
                else:
                    log += "\nERROR - Arquivo " + basename(file) + " não possui PDF"
            except Exception as ex:
                log += "\n\n FILE " + file + " ERROR: " + str(ex)

    log += "\n\nFIM: " + str(datetime.now())

    with open(baseDirectory + 'log.txt', 'w') as f:
        f.write(log)
except Exception as ex:
    log += "\n\n PROCESS ERROR: " + str(ex)

print("Processamento encerrado. Verifique o arquivo de log.")

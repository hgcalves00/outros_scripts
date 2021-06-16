from ftplib import FTP
from tabula import read_pdf
from zipfile import ZipFile

ftp = FTP('ftp.mtps.gov.br')
ftp.login()
ftp.cwd('pdet/rais/2010/estaduais/tabelas')
#todos os arquivos aqui:
files = ftp.nlst()
print(files)

with open('AC.ZIP', 'wb') as fobj:
    AC = ftp.retrbinary('RETR %s' % 'AC.ZIP', fobj.write)
  
#especificando o nome do arquivo procurado
file_name = "AC.ZIP"
  
#abrindo o arquivo com a biblioteca zipfile
with ZipFile(file_name, 'r') as zip:
    #printando todos os conteúdos
    zip.printdir()
  
    #extraindo todos os arquivos
    print('extraindo arquivos...')
    zip.extractall()
    print('feito!')
    
arquivo = 'Tabelas_RAIS_2010_AC.pdf'

df = read_pdf(arquivo, pages="1", multiple_tables=True)


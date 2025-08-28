# edição de pdfs com senha

import pypdf
from pathlib import Path

# caminho_pdf = Path('materiais de aula') / 'documentos' / 'dom_casmurro.pdf'
caminho_pdf = Path('dom_casmurro_senha.pdf')
# escritor_pdf = pypdf.PdfWriter(clone_from=caminho_pdf)

leitor_pdf = pypdf.PdfReader(caminho_pdf)
leitor_pdf.decrypt('senhasecreta')

# escritor_pdf.encrypt('senhasecreta')
# escritor_pdf.write('dom_casmurro_senha.pdf')


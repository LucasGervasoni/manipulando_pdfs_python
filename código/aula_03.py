# abrindo pdf

import pypdf
from pathlib import Path

caminho_pdf = Path('materiais de aula') / 'documentos' / 'dom_casmurro.pdf'

leitor_pdf = pypdf.PdfReader(caminho_pdf)

print(len(leitor_pdf.pages))
print(leitor_pdf.metadata)
print(leitor_pdf.metadata.author)
print(leitor_pdf.metadata.creation_date)
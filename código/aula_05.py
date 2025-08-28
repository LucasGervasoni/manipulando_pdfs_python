# combinando pdfs

import pypdf
from pathlib import Path

escritor_pdf = pypdf.PdfWriter()

caminhos = [
  Path('materiais de aula') / 'documentos' / 'vpt_minecraft.pdf',
  Path('materiais de aula') / 'documentos' / 'dom_casmurro.pdf'
]

leitores_pdf = [pypdf.PdfReader(caminho) for caminho in caminhos]

for pagina in leitores_pdf.pages:
    escritor_pdf.add_page(pagina)

escritor_pdf.write('documento_combinado.pdf')
# extraindo paginas de um pdf

import pypdf
from pathlib import Path

caminho_pdf = Path('materiais de aula') / 'documentos' / 'vpt_minecraft.pdf'
leitor_pdf = pypdf.PdfReader(caminho_pdf)
pagina_04 = leitor_pdf.pages[3]

escritor_pdf = pypdf.PdfWriter()
# escritor_pdf.add_page(pagina_04)
# escritor_pdf.write('vpt_minecraft_pagina_04.pdf')

for pagina in leitor_pdf.pages[:3]:
    escritor_pdf.add_page(pagina)
    
escritor_pdf.write('vpt_minecraft_intro.pdf')
#mudando dimensoes de um pdf

import pypdf
from pathlib import Path

caminho_pdf = Path('materiais de aula') / 'documentos' / 'vpt_minecraft.pdf'
escritor_pdf = pypdf.PdfWriter(clone_from=caminho_pdf)

for pagina in escritor_pdf.pages:
    # pagina.scale_by(0.1)
    pagina.scale_to(pypdf.PaperSize.A8.width, pypdf.PaperSize.A8.height)

escritor_pdf.write('vpt_minecraft_redimensionado02.pdf')
# adicionando carimbo e marca d'água 

import pypdf
from pathlib import Path

caminho_pdf = Path('materiais de aula') / 'documentos' / 'dom_casmurro.pdf'
escritor_pdf = pypdf.PdfWriter(clone_from=caminho_pdf)

# caminho_carimbo = Path('materiais de aula') / 'assets' / 'carimbo.pdf'
# carimbo = pypdf.PdfReader(caminho_carimbo).pages[0]

caminho_marca = Path('materiais de aula') / 'assets' / 'marca.pdf'
marca = pypdf.PdfReader(caminho_marca).pages[0]

# for pagina in escritor_pdf.pages:
#     fator_escala = 4
#     x = pagina.mediabox.left
#     y = pagina.mediabox.top - (carimbo.mediabox.height / fator_escala)
#     transformation = pypdf.Transformation().scale(1 / fator_escala).translate(x, y)
#     pagina.merge_transformed_page(carimbo, transformation, over=True)

for pagina in escritor_pdf.pages:
    escala_x = pagina.mediabox.width / marca.mediabox.width
    escala_y = pagina.mediabox.height / marca.mediabox.height
    transformation = pypdf.Transformation().scale(sx=escala_x, sy=escala_y)
    pagina.merge_transformed_page(marca, transformation, over=False)
    
    
escritor_pdf.write('dom_casmurro_marca.pdf')

#rotacionar pagina

import pypdf
from pathlib import Path

caminho_pdf = Path('materiais de aula') / 'documentos' / 'vpt_minecraft.pdf'
escritor_pdf = pypdf.PdfWriter(clone_from=caminho_pdf)

for pagina in escritor_pdf.pages:
    pagina.rotate(180)


#rotacionar conteudo

# transformacao = pypdf.Transformation().rotate(45)
transformacao = pypdf.Transformation().rotate(30).translate(tx=300)

for pagina in escritor_pdf.pages:
    pagina.add_transformation(transformacao)


escritor_pdf.write('vpt_minecraft_rotacionado03.pdf')
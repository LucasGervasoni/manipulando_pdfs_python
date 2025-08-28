#cortando pedaços de um PDF

import pypdf
from pathlib import Path

caminho_pdf = Path('materiais de aula') / 'documentos' / 'vpt_minecraft.pdf'
leitor_pdf = pypdf.PdfReader(caminho_pdf)

primeira_pagina = leitor_pdf.pages[0]
print(f'Mediabox original: {primeira_pagina.mediabox}')

escritor_pdf = pypdf.PdfWriter()
escritor_pdf.add_page(primeira_pagina)


primeira_pagina.mediabox.left = -200
primeira_pagina.mediabox.right = 800
primeira_pagina.mediabox.top = 792
primeira_pagina.mediabox.bottom = -50

print(f'Mediabox alterada: {primeira_pagina.mediabox}')

escritor_pdf.add_page(primeira_pagina)

escritor_pdf.write('vpt_minecraft_cortado.pdf')
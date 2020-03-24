from lib.deteccao import Deteccao
from lib.deteccao import HAARCASCATE

dt = Deteccao()

dt.selecionarImagem('img.jpg')
#dt.detectar(HAARCASCATE.ROSTO)
dt.detectaRosto(True)
dt.salvar('fotos-salvar/imagem2.jpg')
dt.exibir()
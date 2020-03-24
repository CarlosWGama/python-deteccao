from lib.deteccao import Deteccao

dt = Deteccao()

dt.selecionarImagem('img.jpg')
dt.detectaRosto(True)

#Caso deseje salvar
dt.salvar('fotos-salvar/imagem2.jpg')

#Caso deseje exibir na tela
dt.exibir()
# Detecção de Rostos



Um simples código de detecção de rostos:
```python
from lib.deteccao import Deteccao

dt = Deteccao()

dt.selecionarImagem('img.jpg')
#True caso queira pegar os olhos também
dt.detectaRosto(True) 

#Caso deseje salvar
dt.salvar('fotos-salvar/imagem2.jpg')

#Caso deseje exibir na tela
dt.exibir()
```

----
Usando haarscascade próprio

```python
from lib.deteccao import Deteccao
from lib.deteccao import HAARCASCATE

dt = Deteccao()

dt.selecionarImagem('img.jpg')
#Já há o de ROSTO E OLHOS DISPONIVEIS
#dt.detecta(HAARCASCATE.ROSTO)
dt.detecta('C:\opencv\haarscascade_proprio.xml')

dt.exibir()
```

----
Recuperando da Webcam

```python
from lib.deteccao import Deteccao
from lib.deteccao import HAARCASCATE

dt = Deteccao()
#False - Tira Foto | True - Exibe a webcam em tempo real
dt.detectaDeWebcam(HAARCASCATE.ROSTO, False)

dt.salvar('fotos-salvar/webcam.jpg')
```

---
Autor: Carlos W. Gama

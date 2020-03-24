import cv2
#pip install opencv-python 
from enum import Enum
import os

class HAARCASCATE(Enum):
    ROSTO = '\haarcascade\haarcascade_frontalface_default.xml';
    # ROSTO = '\haarcascade\haarcascade_frontalface_default.xml';
    OLHOS = '\haarcascade\haarcascade_eye.xml';


class Deteccao:

    def __init__(self):
        self.__imagem = None
        self.__imagemAlterada = None
   
    def selecionarImagem(self, caminho):
        ''' Busca uma imagem do pc '''
        self.__imagem = cv2.imread(caminho)
        
    def __escalaCinza(self):
        ''' Torna a imagem em escala cinza '''
        self.__imagemAlterada = cv2.cvtColor(self.__imagem, cv2.COLOR_RGB2GRAY)
      

    def detectaRosto(self, olhos=False, escala=1.1):
        self.detectar(HAARCASCATE.ROSTO, escala=escala)
        if (olhos):
            self.detectar(HAARCASCATE.OLHOS, (0, 255, 0), escala=escala)

    def detectar(self, haarcascade, cor=(0, 0, 255), espessura = 2, escala=1.1, minNeighbors=6, minSize=(5, 5)):
        ''' Detecta algo na imagem '''
        self.__escalaCinza()
        if(isinstance(haarcascade, HAARCASCATE)): 
            haarcascade = os.path.dirname(os.path.abspath(__file__)) + haarcascade.value
        
        classificador = cv2.CascadeClassifier(haarcascade)
        facesDetectadas = classificador.detectMultiScale(self.__imagemAlterada, scaleFactor=escala, minNeighbors=minNeighbors, minSize=minSize)

        for (x, y, w, h) in facesDetectadas:
            cv2.rectangle(self.__imagem, (x, y), (x+w,y+h), cor, espessura)

    def detectaDeWebcam(self, haarcascade, gravacao=False, cor=(0, 0, 255), espessura = 2, escala=1.1, minNeighbors=6, minSize=(5, 5)): 
        
        video = cv2.VideoCapture(0)


        while True:

            sucesso, self.__imagem = video.read()
            self.detectar(haarcascade, cor, espessura, escala, minNeighbors, minSize)
            cv2.imshow("Webcam", self.__imagem)


            if (not gravacao or cv2.waitKey(1) == ord('q')): #Clicou para sair
                break
        video.release()
        cv2.destroyAllWindows()
        self.exibir()

    def exibir(self):
        ''' Imagem com rastreio '''
        cv2.imshow("Original", self.__imagem)
        cv2.waitKey()

    def salvar(self,caminho):
        cv2.imwrite(caminho, self.__imagem)
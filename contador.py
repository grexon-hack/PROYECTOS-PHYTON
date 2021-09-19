import cv2
import numpy as np


valorGauss=3
valorKernel=3
original= cv2.imread('monedas.jpeg')
gris= cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)
gauss=cv2.GaussianBlur(gris,(valorGauss,valorGauss), 0)
canny=cv2.Canny(gauss, 50,60)
kernel=np.ones((valorKernel,valorKernel),np.uint8)
cierre=cv2.morphologyEx(canny,cv2.MORPH_CLOSE, kernel)


contornos,jerarquia=cv2.findContours(cierre.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print("monedas encontradas: {}".format(len(contornos)))
cv2.drawContours(original, contornos, -1, (0,0,255),2)
#mostrar
# cv2.imshow('original', original)
# cv2.imshow('grises', gris)
cv2.imshow('gauss', gauss)
cv2.imshow('canny',canny)
cv2.imshow('resultado', original)
cv2.waitKey(0)
cv2.destroyAllWindows()

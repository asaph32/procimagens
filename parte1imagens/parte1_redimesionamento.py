import cv2
import matplotlib.pyplot as plt

#Imagem Redimensionada
imagem_colorida = cv2.imread('C:/Users/ricar/Desktop/trabalhoimagens/parte1imagens/lenna.png')

# Defina as dimensões desejadas para o redimensionamento
largura_desejada = 800
altura_desejada = 600

# Redimensione a imagem
imagem_redimensionada = cv2.resize(imagem_colorida, (largura_desejada, altura_desejada))
cv2.imshow('Imagem redimensionada',imagem_redimensionada)
cv2.waitKey(0)

#HSV
imagem_hsv = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2HSV)
cv2.imshow('Imagem HSV : ',imagem_hsv)
cv2.waitKey(0)

#Histograma Colorido
canal_azul, canal_verde, canal_vermelho = cv2.split(imagem_colorida)
plt.hist(canal_azul.ravel(), bins=256, color='blue', alpha=0.5)
plt.hist(canal_verde.ravel(), bins=256, color='green', alpha=0.5)
plt.hist(canal_vermelho.ravel(), bins=256, color='red', alpha=0.5)
plt.xlabel('Intensidade de cor')
plt.ylabel('Número de pixels')
plt.legend(['Canal Azul', 'Canal Verde', 'Canal Vermelho'])
plt.title('Histograma Colorido')
plt.show()

#Histograma em Escala de Cinza
imagem_cinza = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2GRAY)
plt.hist(imagem_cinza.ravel(), bins=256, color='gray', alpha=0.5)
plt.xlabel('Intensidade de cinza')
plt.ylabel('Número de pixels')
plt.title('Histograma em Escala de Cinza')
plt.show()

#Equalização
canal_azul, canal_verde, canal_vermelho = cv2.split(imagem_colorida)

# Equalize cada canal de cor
canal_azul_equalizado = cv2.equalizeHist(canal_azul)
canal_verde_equalizado = cv2.equalizeHist(canal_verde)
canal_vermelho_equalizado = cv2.equalizeHist(canal_vermelho)

# Combine os canais equalizados de volta em uma imagem colorida
imagem_equalizada = cv2.merge((canal_azul_equalizado, canal_verde_equalizado, canal_vermelho_equalizado))

# Exiba a imagem original e a imagem equalizada
cv2.imshow('Imagem Original', imagem_colorida)
cv2.imshow('Imagem Equalizada', imagem_equalizada)

# Aguarde até que uma tecla seja pressionada e depois feche as janelas
cv2.waitKey(0)
cv2.destroyAllWindows()


























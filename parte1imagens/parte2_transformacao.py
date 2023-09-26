import cv2
import matplotlib.pyplot as plt
import numpy as np

imagem = cv2.imread('C:/Users/ricar/Desktop/trabalhoimagens/parte1imagens/imagem.png',cv2.IMREAD_COLOR)

# 1. Preencher todos os buracos dos objetos pretos

# Crie uma máscara binária para os objetos pretos
mascara_pretos = cv2.inRange(imagem, np.array([0, 0, 0]), np.array([30, 30, 30]))

# Aplique uma operação de fechamento para preencher os buracos
kernel = np.ones((5, 5), np.uint8)
mascara_pretos_filled = cv2.morphologyEx(mascara_pretos, cv2.MORPH_CLOSE, kernel)

# 2. Eliminar todos e somente os objetos pretos

# Inverta a máscara preta para selecionar objetos não pretos
mascara_nao_pretos = cv2.bitwise_not(mascara_pretos)

# Aplique uma operação de abertura para eliminar os objetos pretos
mascara_sem_pretos = cv2.morphologyEx(mascara_nao_pretos, cv2.MORPH_OPEN, kernel)

# 3. Preencher os buracos dos objetos de cor azul, amarelo e verde

# Converta a imagem para o espaço de cores HSV
imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

# Defina faixas de cores para azul, amarelo e verde
lower_blue = np.array([90, 50, 50])
upper_blue = np.array([130, 255, 255])
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])
lower_green = np.array([40, 40, 40])
upper_green = np.array([80, 255, 255])

# Crie máscaras binárias para objetos azuis, amarelos e verdes
mascara_azul = cv2.inRange(imagem_hsv, lower_blue, upper_blue)
mascara_amarela = cv2.inRange(imagem_hsv, lower_yellow, upper_yellow)
mascara_verde = cv2.inRange(imagem_hsv, lower_green, upper_green)

# Aplique uma operação de fechamento para preencher os buracos nas máscaras
mascara_azul_filled = cv2.morphologyEx(mascara_azul, cv2.MORPH_CLOSE, kernel)
mascara_amarela_filled = cv2.morphologyEx(mascara_amarela, cv2.MORPH_CLOSE, kernel)
mascara_verde_filled = cv2.morphologyEx(mascara_verde, cv2.MORPH_CLOSE, kernel)

# 4. Realçar as bordas da imagem

# Converta a imagem para escala de cinza
imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Aplique o detector de bordas Canny
bordas = cv2.Canny(imagem_gray, 100, 200)

# Exiba as imagens resultantes
cv2.imshow('Preenchimento de Buracos (Objetos Pretos)', mascara_pretos_filled)
cv2.imshow('Eliminação de Objetos Pretos', mascara_sem_pretos)
cv2.imshow('Preenchimento de Buracos (Azul)', mascara_azul_filled)
cv2.imshow('Preenchimento de Buracos (Amarelo)', mascara_amarela_filled)
cv2.imshow('Preenchimento de Buracos (Verde)', mascara_verde_filled)
cv2.imshow('Realce de Bordas', bordas)

# Aguarde até que uma tecla seja pressionada e depois feche as janelas
cv2.waitKey(0)
cv2.destroyAllWindows()
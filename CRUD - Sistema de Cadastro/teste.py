import os 
caminho_image = "imagens-background\\Pizzaria.jpg"

if os.path.exists(caminho_image):
    print("sim")
else:
    print("não")
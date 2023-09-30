import os 
caminho_image = ".\Pizzaria-4.jpg"

if os.path.exists(caminho_image):
    print("sim")
else:
    print("não")
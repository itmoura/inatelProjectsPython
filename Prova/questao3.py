import numpy as np

colors = [
    {"color": "black", "type": "primary", "code": {"rgba": [255,255,255,1],"hex": "#000"}},
    {"color": "green", "type": "secondary", "code": {"rgba": [0,255,0,0.1],"hex": "#0F0"}},
    {"color": "yellow", "type": "primary","code": {"rgba": [255,255,0,0.7],"hex": "#FF0"}},
    {"color": "blue", "type": "primary","code": {"rgba": [0,0,255,1],"hex": "#00F"}}
]

# a. Mostre apenas o nome das cores que são primárias;
colorsPrimary = np.array(colors)
for color in colorsPrimary:
    if(np.array(np.where(color['type'] == 'primary')).size > 0):
        print(color['color'])

# b. Mostre apenas os códigos hexadecimais das cores que possuem tom de azul máximo (255);
colorsPrimary = np.array(colors)
for color in colorsPrimary:
    if(np.array(np.where(color['code']['rgba'][2] == 255)).size > 0):
        print(color['code']['hex'])

# c. Mostre apenas os índices das cores na lista que possuem a menor opacidade (0.1);
for i in range(0, len(colors)):
    if(np.array(np.where(colors[i]['code']['rgba'][3] == 0.1)).size > 0):
        print(i)

# d. Mostre a cor e tipo das cores que possuem códigos hexadecimais com dois zeros;
for i in range(0, len(colors)):
    if(colors[i]['code']['hex'].find("00") > 0):
        print(colors[i]['color'])

# e. Mostre o RGBA das cores que possuem códigos hexadecimais com um “F” no meio;
for i in range(0, len(colors)):
    if(colors[i]['code']['hex'].find("F") > 0):
        print(colors[i]['color'])


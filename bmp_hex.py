import cv2 as cv
from PIL import Image

def convert_jpg_to_bmp(url):
    img = Image.open(url)
    img.save(url.split(".")[0]+".bmp", format="BMP")

#url_jpg = "car.jpg"
#img_bmp = convert_jpg_to_bmp(url_jpg)
url_bmp = "car.bmp"

def convert_bmp_to_hex(url, output_path):
    with Image.open(url) as img:
        # Converta para o modo RGB (caso não esteja)
        img = img.convert("RGB")
        
        # Obtenha os dados de pixels
        pixels = list(img.getdata())
        width, height = img.size

        # Crie o conteúdo hexadecimal
        hex_data = []
        for y in range(height):
            row = []
            for x in range(width):
                r, g, b = pixels[y * width + x]
                # Combine os canais RGB em um único valor hexadecimal
                pixel_hex = f"{r:02X}{g:02X}{b:02X}"
                row.append(pixel_hex)
            hex_data.append(" ".join(row))
        
        # Escreva o conteúdo hexadecimal em um arquivo
        with open(output_path, "w") as hex_file:
            hex_file.write("\n".join(hex_data))
    
    print(f"Arquivo .hex gerado em: {output_path}")


output_path = "car.hex"
convert_bmp_to_hex(url_bmp, output_path)
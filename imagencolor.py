from PIL import Image
ancho, alto = 0,0
def identidad(img): # obtiene la imagen en tono griss
    salida = Image.new("L",(ancho,alto)) # nueva imagen en tono gris

    for i in range(img.size[0]):
        for j in range (img.size[1]):
             p=img.getpixel((i,j))
             q=p # funcion de identidad
             salida.putpixel((i,j),q)
    return salida

def inverso(img):
    salida = Image.new("L",(ancho,alto)) # nueva imagen en tono gris

    for i in range(img.size[0]):
        for j in range (img.size[1]):
             p=img.getpixel((i,j))
             q=255-p # funcion inverso
             salida.putpixel((i,j),q)
    return salida

def umbral1(img,u):
    salida = Image.new("L",(ancho,alto)) # nueva imagen en tono gris
    for i in range(img.size[0]):
        for j in range (img.size[1]):
             p=img.getpixel((i,j))
             if p<=u:
                 q = 0
             else:
                     q=255
             salida.putpixel((i,j),q) 
    return salida

imgGray=Image.open("nuevo.jpg").convert("L")#imagen en jpg convierte en tono gris
imgGray.show()
ancho,alto = imgGray.size # dimension de la imagen
resultado = umbral1(imgGray,128)# llama a la funcion identidad , la salida es el resultado
resultado.save("snoopy_umbral1.tiff")# guardando
resultado.show()# visualiza la imagen


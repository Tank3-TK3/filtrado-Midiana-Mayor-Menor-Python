# >>>>>>>>>>>>>>>>>>>>>>>>>>>Hecho por Roberto (Tank3) Cruz Lozano<<<<<<<<<<<<<<<<<<<<<<<<<<<
#############################################################################################
#                                          MODULOS
import cv2
import numpy as np
import matplotlib.pyplot as plt
#############################################################################################
#                                         FUNCIONES
def ruidoSal( img ):
    imgSal = img.copy()
    for i in range( 0 , int( ( img.shape[0] * img.shape[1] ) / 10 ) ):
        imgSal[np.random.randint( img.shape[0] )][np.random.randint( img.shape[1] )] = 255
    return imgSal

def ruidoPimienta( img ):
    imgPimienta = img.copy()
    for i in range( 0 , int( ( img.shape[0] * img.shape[1] ) / 10 ) ):
        imgPimienta[np.random.randint( img.shape[0] )][np.random.randint( img.shape[1] )] = 0
    return imgPimienta

def vecinos( img , i , j ):
    m = []
    try:
        m.append( img[i-1][j-1] )
    except:
        pass
    try:
        m.append( img[i][j-1] )
    except:
        pass
    try:
        m.append( img[i+1][j-1] )
    except:
        pass
    try:
        m.append( img[i-1][j] )
    except:
        pass
    try:
        m.append( img[i][j] )
    except:
        pass
    try:
        m.append( img[i+1][j] )
    except:
        pass
    try:
        m.append( img[i-1][j+1] )
    except:
        pass
    try:
        m.append( img[i][j+1] )
    except:
        pass
    try:
        m.append( img[i+1][j+1] )
    except:
        pass
    m.sort()
    return m

def filtroMediana( imgOrg , imgRuido ):
    imgMediana = np.zeros( imgOrg.shape , dtype=np.uint8 )
    mask = []
    for i in range( 0 , imgOrg.shape[0] ):
        for j in range( 0 , imgOrg.shape[1] ):
            mask = vecinos( imgRuido , i , j )
            imgMediana[i][j] = mask[int( len( mask ) / 2 )]
            mask = []
    return imgMediana

def filtroMayor( imgOrg , imgRuido ):
    imgMayor = np.zeros( imgOrg.shape , dtype=np.uint8 )
    mask = []
    for i in range( 0 , imgOrg.shape[0] ):
        for j in range( 0 , imgOrg.shape[1] ):
            mask = vecinos( imgRuido , i , j )
            imgMayor[i][j] = mask[-1]
            mask = []
    return imgMayor

def filtroMenor( imgOrg , imgRuido ):
    imgMenor = np.zeros( imgOrg.shape , dtype=np.uint8 )
    mask = []
    for i in range( 0 , imgOrg.shape[0] ):
        for j in range( 0 , imgOrg.shape[1] ):
            mask = vecinos( imgRuido , i , j )
            imgMenor[i][j] = mask[0]
            mask = []
    return imgMenor
#############################################################################################
#                                           MAIN
if __name__ == '__main__':
    img = cv2.imread( './img/man.bmp' , 2 )
    plt.imshow( img , 'gray' )
    plt.title( 'Imagen Original' )
    plt.axis( 'off' )
    plt.show()

    img2 = ruidoSal( img )
    plt.subplot( 2 , 3 , 1 )
    plt.imshow( img2 , 'gray' )
    plt.title( 'Imagen con Sal' )
    plt.axis( 'off' )
    cv2.imwrite( './imgExam/imgSal.bmp' , img2 )

    img3 = ruidoPimienta( img )
    plt.subplot( 2 , 3 , 4 )
    plt.imshow( img3 , 'gray' )
    plt.title( 'Imagen con Pimienta' )
    plt.axis( 'off' )
    cv2.imwrite( './imgExam/imgPimienta.bmp' , img3 )

    img4 = filtroMediana( img , img2 )
    plt.subplot( 2 , 3 , 2 )
    plt.imshow( img4 , 'gray' )
    plt.title( 'Imagen Filtro Mediana sin Sal' )
    plt.axis( 'off' )
    cv2.imwrite( './imgExam/imgFiltroMedianaSal.bmp' , img4 )

    img5 = filtroMediana( img , img3 )
    plt.subplot( 2 , 3 , 5 )
    plt.imshow( img5 , 'gray' )
    plt.title( 'Imagen Filtro Mediana sin Pimienta' )
    plt.axis( 'off' )
    cv2.imwrite( './imgExam/imgFiltroMedianaPimienta.bmp' , img5 )

    img6 = filtroMenor( img , img2 )
    plt.subplot( 2 , 3 , 3 )
    plt.imshow( img6 , 'gray' )
    plt.title( 'Imagen Filtro Menor sin Sal' )
    plt.axis( 'off' )
    cv2.imwrite( './imgExam/imgFiltroMenorSal.bmp' , img6 )

    img7 = filtroMayor( img , img3 )
    plt.subplot( 2 , 3 , 6 )
    plt.imshow( img7 , 'gray' )
    plt.title( 'Imagen Filtro Mayor sin Pimienta' )
    plt.axis( 'off' )
    cv2.imwrite( './imgExam/imgFiltroMayorPimienta.bmp' , img7 )

    plt.show()
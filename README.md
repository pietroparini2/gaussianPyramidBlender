
# ___Pietro Parini 794146___
# ___Visual Information Processing and Management___
# ___Assignment 1: Blend piramidale___

******


    """  
        Created on Tue Nov 12 10:38:36 2019  
        @author: pietro  
        @version: python3  
        @library: opencv  
        @library : numpy  
        1- caricare 2 immagini e la maschera  
        2- calcolare le piramide gaussiane per le due immagine e per la maschera  
          @function: gaussian_pyramid  
        3- partendo dalla piramide gaussiana calcolare la piramide laplaciana  
          @function: laplacian_pyramid  
        4- mescolare ogni livello della piramide secondo l'immagine della maschera con
        corrispondente livello della piramide gaussiana  
          @function: blendLaplacesAndMask  
        5- ricostruire l'immagine originale partendo dalla laplaciana mescolata
          espandendo il livello e aggiungendolo al livello inferiore  
          @function: recosrtuct  
    """

__immagine originale input a__
![Alt original_a](./img/summer.jpg? "input_original_a")
__immagine originale input b__
![Alt original_b](./img/summer.jpg "input_original_b")
__immagine ottenuta con piramide a un livello(minimo n° di livelli della piramide)__
![Alt level_1](./img/imageFinal0.jpg "Immagine ottenuta con piramide a 1 livello")
__immagine ottenuta con piramide a 10 livelli(massimo n° di livelli della piramide)__
![Alt level_9](./img/imageFinal10.jpg "Immagine ottenuta con piramide a 10 livelli")
******
__immagine ottenuta con piramide a 7 livelli(miglior risultato visivo)__
![Alt level_7](./img/imageFinal7.jpg "Immagine ottenuta con piramide a 10 livelli")

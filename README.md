
# ___Pietro Parini 794146___
# ___Visual Information Processing and Management___
# ___Assignment 1: Blend piramidale___

******
Repository [gitHub](https://github.com/pietroparini2/gaussianPyramidBlender).

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

*immagine originale input a*
![Alt original_a](./img/summer.jpg? "input_original_a")  


*immagine originale input b*
![Alt original_b](./img/winter.jpg "input_original_b")  


*immagine ottenuta con piramide a un livello(minimo n° di livelli della piramide)*  
*stacco netto tra immagine di input a ed immagine di input b*
![Alt level_1](./img/imageFinal0.jpg "Immagine ottenuta con piramide a 1 livello")  


*immagine ottenuta con piramide a 10 livelli(massimo n° di livelli della piramide)*  
*eccessiva propagazione dei colori delle due immagini*
![Alt level_9](./img/imageFinal10.jpg "Immagine ottenuta con piramide a 10 livelli")  


******
*immagine ottenuta con piramide a 7 livelli*  
*effetto visivo ottimale*
![Alt level_7](./img/imageFinal7.jpg "Immagine ottenuta con piramide a 10 livelli")  

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 10:38:36 2019
@author: pietro
@version python3
@library: opencv
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
    @function: recostruction
"""

import cv2 as cv
import numpy as np


#------- funzione per piramide gaussiana
def gaussian_pyramid( img, levels):
    lower = img.copy();
    pyramid = [lower];
    for i in range(levels):
        lower = cv.pyrDown(lower);
        pyramid.append(np.float32(lower));
    return pyramid

#-------- funzione per piramide laplaciana
def laplacian_pyramid(gaussian_pyramid):
    top = gaussian_pyramid[-1];
    levels = len(gaussian_pyramid) -1 ;
    pyramid = [top];
    for i in range(levels,0,-1):
        size = (gaussian_pyramid[i - 1].shape[1], gaussian_pyramid[i - 1].shape[0])
        gaussian_expanded = cv.pyrUp(gaussian_pyramid[i], dstsize=size)
        laplacian = np.subtract(gaussian_pyramid[i-1], gaussian_expanded)
        pyramid.append(laplacian)
    return pyramid

#-------- funzione per miscelare le due laplaciane con la maschera
def blendLaplacesAndMask(laplacian_a, laplacian_b , mask):
    blender = []
    for la,lb,mask in zip(laplacian_a,laplacian_b,mask):
        ls= lb * mask + la * (1.0- mask)
        blender.append(ls)
    return blender

#------- funzione per ricostruire l'immagine originale
def reconstruct(laplacian_pyramid):
    top = laplacian_pyramid[0]
    lst = [top]
    levels = len(laplacian_pyramid) - 1
    for i in range(levels):
        size = (laplacian_pyramid[i + 1].shape[1], laplacian_pyramid[i + 1].shape[0])
        expanded = cv.pyrUp(top, dstsize=size)
        top = cv.add(laplacian_pyramid[i+1], expanded)
        lst.append(top)
    return lst

## ------ step 1 --------
#carico le due immagini
#dimensione di resize delle immagini

im1 = cv.imread('./img/summer.jpg');
im2 = cv.imread('./img/winter.jpg');
dim1 = im1.shape;
x1 = dim1[1];
y1 = dim1[0];
dim2 = im2.shape;
x2 = dim2[1];
y2 = dim2[0];
x = min(x1, x2);
y = min(y1, y2);
if (x == x1):
    y = y1;
else:
    y = y2;
im1 = cv.resize(im1, (x,y));
im2 = cv.resize(im2, (x,y));

#debug
#cv.imshow('Image', im1);
#cv.waitKey(0); #per non farla chiudere
def main (level):
    #creo la maschera
    mask = np.zeros((y,x,3), dtype= 'float32');
    mask[0:round(y*2/3) , 0:x , : ] = (1,1,1); #area che mi interessa

    ## ---------step 2--------


    gaussian_pyramid_a = gaussian_pyramid(im1, level);
    gaussian_pyramid_b = gaussian_pyramid(im2, level);
    gaussian_pyramid_mask = gaussian_pyramid(mask, level)
    gaussian_pyramid_mask.reverse();

    ## ------- step 3 -------
    laplacian_pyramid_a = laplacian_pyramid(gaussian_pyramid_a);
    laplacian_pyramid_b = laplacian_pyramid(gaussian_pyramid_b);

    ## -------- step 4 -------

    blender = blendLaplacesAndMask(laplacian_pyramid_a, laplacian_pyramid_b, gaussian_pyramid_mask)

    ##-------- step 5 -------

    recostruction = reconstruct(blender);

    #------ salvo il risultato ------
    name = './img/imageFinal'+str(level)+'.jpg'
    cv.imwrite(name,recostruction[level])

maxLevel =10;
for level in range(0,maxLevel):
    main(level)

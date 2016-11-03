from skimage import io
from skimage.color import rgb2gray
from skimage.filters.rank import entropy, gradient
from skimage.morphology import disk
import numpy as np
import matplotlib.pyplot as plt
import sys


def get(y, x, t):
    m = len(t) #rows
    n = len(t[0]) #cols
    if x < 0 or x >= n: return sys.maxsize
    if y < 0 or y >= m: return sys.maxsize
    return t[y][x]

## Return the index of the element with less energy
def min_index(a,b,c):
    array=[a,b,c]
    return sorted(array)[0][1]

## Transform the image to gray
## Calculate the entropy or gradient
## Get the path with less energy
## Return the energy as an integer, and the 
## path with less energy as a list of (x,y)
def energy(img):
    # filas = m, columnas = n
    m, n = img.shape
    ans=[]
    e = 0
    j=img[0].argmin()
    ans.append(img[0][j])
    e+=img[0][j]
    for i in range(m-1):
        j=min_index((img[i+1][j],j),(img[i+1][j+1],j+1),(img[i+1][j-1],j-1))
        ans.append(img[i+1][j])
        e+=img[i+1][j]
 _______________________________________________________________________________________
    camino = [range(n) for i in range(m)]
    costo = [range(n) for i in range(m)]
    for i in range(n):#falta por recorrer el camino inverso para armar el camino, por ahora encuentra el camino con menos energia
    	for j i n range(m):
    		if i == 0:
    			camino[i][j] = 3
    			costo[i][j] = img[i][j]
    		elif j == 0:
    			if costo[i-1][j]<costo[i-1][j+1]:
    				camino[i][j] = 0
    				costo[i][j] = costo[i-1][j]+img[i][j]
    			else:
    				camino[i][j] = 1
    				costo[i][j] = costo[i-1][j+1]+img[i][j]
    		elif j == (len(img[i])-1):
    			if costo[i-1][j]<costo[i-1][j-1]:
    				camino[i][j] = 0
    				costo[i][j] = costo[i-1][j]+img[i][j]
    			else:
    				camino[i][j] = -1
    				costo[i][j] = costo[i-1][j-1]+img[i][j]
    		else:
    			if costo[i-1][j-1]<costo[i-1][j]:
    				camino[i][j] = -1
    				costo[i][j] = costo[i-1][j-1]+img[i][j]
    			elif costo[i-1][j+1]:
    				camino[i][j] = 1
    				costo[i][j] = costo[i-1][j+1]+img[i][j]
    			else:
    				camino[i][j] = 0
    				costo[i][j] = costo[i-1][j]+img[i][j]
   min = costo[len(costo)-1][0]
   mi = 0
   for i in range(len(img[0]):
    	if costo[len(costo)-1][i]< min:
    		min = costo[len(costo)-1][i]
    		mi = i
    return e, ans


def togray(image):
    image_bw = rgb2gray(image)
    # using the entropy
    #image_e = entropy(image_bw,disk(1))
    #return energy(image_e)
    
    # using gradient
    image_g = gradient(image_bw,disk(1))
    return image_g

## Remove one pixel per row... the one
## in the path min energy
def remove(image, pixels):
    ## Debe remover el camino con menor energia
    ans = image
    
    return ans
    
if __name__=='__main__':
    import sys
    
    image = io.imread('image.png')
    img_gray = togray(image)
    plt.figure()
    plt.imshow(image)
    plt.figure()
    plt.imshow(img_gray)
    plt.show()
    
    percent = 0.75
    
    m,n,_ = image.shape
    new_n = int(n * percent)
    
    img = image
    ims = []
    for i in range(n-new_n):
        print("Iteracion numero {}/{}".format(i+1, n-new_n))
        img_gray = togray(img)
        e, p = energy(img_gray)
        img_new = remove(img, p)
        
        img = img_new
    
    plt.figure()
    plt.imshow(image) # imagen original
    plt.figure()
    plt.imshow(img) # imagen escalada
    plt.show()

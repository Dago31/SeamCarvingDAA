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
def min_index(a,b,c=(sys.maxsize,0)):
    array=[a,b,c]
    return sorted(array)[0][1]

## Transform the image to gray
## Calculate the entropy or gradient
## Get the path with less energy
## Return the energy as an integer, and the
## path with less energy as a list of (x,y)
def energy2(img):
    # filas = m, columnas = n
    m, n = img.shape
    paths=[list() for _ in range(n)]
    path_energy=[0 for _ in range(n)]
    for k in range(n):
        j=k
        paths[k].append(j)
        path_energy[k]+=img[0][k]
        for i in range(m-1):
            if j == n-1:
                j=min_index((img[i+1][j],j),(img[i+1][j-1],j-1))
            elif j == 0:
                j=min_index((img[i+1][j],j),(img[i+1][j+1],j+1))
            else:
                j=min_index((img[i+1][j],j),(img[i+1][j+1],j+1),(img[i+1][j-1],j-1))

            paths[k].append(j)
            path_energy[k]+=img[i+1][j]

    index = path_energy.index(min(path_energy))
    return path_energy[index], paths[index]

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
    m,n,_ = image.shape
    aux=image.tolist()
    for i in range(m):
        del aux[i][pixels[i]]

    ans = np.asarray(aux,dtype='uint8')

    return ans

if __name__=='__main__':
    import sys

    image = io.imread('image.png')
    img_gray = togray(image)
    # plt.figure()
    # plt.imshow(image)
    # plt.figure()
    # plt.imshow(img_gray)
    # plt.show()

    percent = 0.75

    m,n,_ = image.shape
    print(m,n)
    new_n = int(n * percent)
    img = image
    print(img)
    for i in range(n-new_n):
        print("Iteracion numero {}/{}".format(i+1, n-new_n))
        img_gray = togray(img)
        e,p = energy2(img_gray)
        img_new = remove(img, p)
        img = img_new

    plt.figure()
    plt.imshow(image) # imagen original
    plt.figure()
    plt.imshow(img) # imagen escalada
    plt.show()

from skimage import io
from skimage.color import rgb2gray
from skimage.filters.rank import entropy, gradient
from skimage.morphology import disk
import numpy as np
import matplotlib.pyplot as plt
import sys

def sumar(arr):
	sum = 0
	for i in range(len(arr)):
		sum += arr[i]
	
	return sum
	
def energy(img):
    # filas = m, columnas = n
    m, n = img.shape
    costo = [[0] * n for i in range(m)]

    for j in range(n):
        for i in range(m):
            if i == 0:
                costo[i][j] = sumar(img[i][j])
            elif j == 0:
                if costo[i-1][j]<costo[i-1][j+1]:
                    costo[i][j] = costo[i-1][j]+sumar(img[i][j])
                else:
                    costo[i][j] = costo[i-1][j+1]+sumar(img[i][j])
            elif j == (len(img[i])-1):
                if costo[i-1][j]<costo[i-1][j-1]:
                    costo[i][j] = costo[i-1][j]+sumar(img[i][j])
                else:
                    costo[i][j] = costo[i-1][j-1]+sumar(img[i][j])
            else:
                if costo[i-1][j-1]<costo[i-1][j]:
                    costo[i][j] = costo[i-1][j-1]+sumar(img[i][j])
                elif costo[i-1][j+1]<costo[i-1][j]:
                    costo[i][j] = costo[i-1][j+1]+sumar(img[i][j])
                else:
                    costo[i][j] = costo[i-1][j]+sumar(img[i][j])

    min_acum = min(costo[len(costo)-1])
    ind = costo[len(costo)-1].index(min_acum)
    camino = []
    camino.append(ind)
    rest = min_acum - sumar(img[m-1][ind])

    for i in reversed(range(m-1)):
        if ind == 0:
            if costo[i][ind] != rest:
                ind = ind+1
        elif ind == n-1:
            if costo[i][ind-1] == rest:
                ind = ind-1
        else:
            if costo[i][ind-1] == rest:
                ind = ind-1
            elif costo[i][ind+1] == rest:
                ind = ind+1

        rest = rest - sumar(img[i][ind])
        camino.append(ind)
    return camino
def remove1(image, pixels):

    m,n,_ = image.shape
    aux=image.tolist()
    for i in range(n):
        value = img[m-1-i][pixels[i]]
        img[m-1-i].remove(value)
    # print(img)

def togray(image):
    image_bw = rgb2gray(image)
    # using the entropy
    #image_e = entropy(image_bw,disk(1))
    #return energy(image_e)

    # using gradient
    image_g = gradient(image_bw,disk(1))
    return image_g

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
    new_n = int(n * percent)
    img = image
    img_gray = togray(img)
    array=np.array([[3,2,5,7],[4,1,3,10],[7,8,9,1]])
    p=energy(img_gray)
    print(p)
    # print(img)
    # for i in range(n-new_n):
    #     print("Iteracion numero {}/{}".format(i+1, n-new_n))
    #     img_gray = togray(img)
    #     p = energy(img_gray)
    #     img_new = remove1(img, p)
    #     img = img_new
    #
    # plt.figure()
    # plt.imshow(image) # imagen original
    # plt.figure()
    # plt.imshow(img) # imagen escalada
    # plt.show()

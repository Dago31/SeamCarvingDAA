def e(img, m, n, i, j):
    if j < 0 or j > n: return sys.maxsize
    if i == m+1:
        return 0

    return img[i][j] + min(e(img,m,n,i+1,j),
                            e(img,m,n,i+1,j+1), e(img,m,n,i+1,j-1))

def energy(img): #usar img.shape para sacar n y m
    m,n=img.shape
    a=[]
    for i in range(n):
        a.append(e(img,m,n,0,i))

    return min(a)

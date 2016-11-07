def energy(img):
    # filas = m, columnas = n
    m, n = img.shape
    costo = [[0] * n for i in range(m)]
    for i in range(n):
    	for j in range(m):
    		if i == 0:
    			costo[i][j] = img[i][j]
    		elif j == 0:
    			if costo[i-1][j]<costo[i-1][j+1]:
    				costo[i][j] = costo[i-1][j]+img[i][j]
    			else:
    				costo[i][j] = costo[i-1][j+1]+img[i][j]
    		elif j == m-1:
    			if costo[i-1][j]<costo[i-1][j-1]:
    				costo[i][j] = costo[i-1][j]+img[i][j]
    			else:
    				costo[i][j] = costo[i-1][j-1]+img[i][j]
    		else:
    			if costo[i-1][j-1]<costo[i-1][j]:
    				costo[i][j] = costo[i-1][j-1]+img[i][j]
    			elif costo[i-1][j+1]<costo[i-1][j]:
    				costo[i][j] = costo[i-1][j+1]+img[i][j]
    			else:
    				costo[i][j] = costo[i-1][j]+img[i][j]
    mini = min(costo[n-1])
    ind = costo[n-1].index(mini)
    camino = []
    rest = mini - img[n-1][ind]
    for i in range(1,n+1):
    	if ind == 0:
    		if costo[n-i][ind] == rest:
    			ind = ind
    		else:
    			ind = ind+1
    	elif ind == m-1:
    		if costo[n-i][ind-1] == rest:
    			ind = ind-1
    		else:
    			ind = ind
    	else:
    		if costo[n-i][ind-1] == rest:
    			ind = ind-1
    		elif costo[n-i][ind+1] == rest:
    			ind = ind+1
    		else:
    			ind = ind
    	rest = rest - img[n-i][ind]
    	camino.append(ind)
    return camino
def remove1(image, pixels):
    
    m,n,_ = image.shape
    aux=image.tolist()
    for i in range(n):
		value = img[n-1-i][pixels[i]]
		img[n-1-i].remove(value)
	print(img)

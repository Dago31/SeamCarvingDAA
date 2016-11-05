def energy(img):
    # filas = m, columnas = n
    m, n = img.shape
    costo = [range(n) for i in range(m)]
    for i in range(n):
    	for j i n range(m):
    		if i == 0:
    			costo[i][j] = img[i][j]
    		elif j == 0:
    			if costo[i-1][j]<costo[i-1][j+1]:
    				costo[i][j] = costo[i-1][j]+img[i][j]
    			else:
    				costo[i][j] = costo[i-1][j+1]+img[i][j]
    		elif j == (len(img[i])-1):
    			if costo[i-1][j]<costo[i-1][j-1]:
    				costo[i][j] = costo[i-1][j]+img[i][j]
    			else:
    				costo[i][j] = costo[i-1][j-1]+img[i][j]
    		else:
    			if costo[i-1][j-1]<costo[i-1][j]:
    				costo[i][j] = costo[i-1][j-1]+img[i][j]
    			elif costo[i-1][j+1]:
    				costo[i][j] = costo[i-1][j+1]+img[i][j]
    			else:
    				costo[i][j] = costo[i-1][j]+img[i][j]
   min = min(costo[len(costo)-1])
   ind = costo[len(costo)-1].index(min)
   camino = []
   camino.append(ind)
   for i in range(2,n):
		rest = min - img[n+1-i][ind]
		if ind == 0:
			if costo[n-i][ind] == rest:
				ind = ind
			else
				ind = ind+1
		elif ind == m:
			if costo[n-i][ind] == rest:
				ind = ind
			else:
				ind = ind-1
		else
			if costo[n-i][ind] == rest:
				ind = ind
			elif costo[n-i][ind+1] == rest:
				ind = ind+1
			else
				ind = ind-1
		camino.append(ind)
	return camino

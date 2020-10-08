def contracting(l):
  
  result = True
  for i in range(len(l)-1):
    if i == 0:
      diff = abs(l[i] - l[i+1])
    else:
      adjDiff = abs(l[i] - l[i+1])
      if adjDiff >= diff:
        result = False
        break
        
  return(result)


def counthv(l):
  
  (hc,vc) = (0,0)
  for i in range(1,len(l)-1):
    if (l[i] > l[i-1]) and (l[i] > l[i+1]):
      hc += 1
    elif (l[i] < l[i-1]) and (l[i] < l[i+1]):
      vc +=1
  
  return([hc,vc])


def leftrotate(m):
  
  n = len(m)
  rotatedMatrix = []
  for i in range(n):
    tempList = []
    for j in range(n):
      tempList.append(m[j][n-(i+1)])
    rotatedMatrix.append(tempList)
    
  return(rotatedMatrix)
    
      
  

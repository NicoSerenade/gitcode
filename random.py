def entero_minimo(l: int, r: int, d: int)->int:
    if d < l or d > r:
        x = d
        return x
    
    else:
        a = (r // d) + 1
        return int(d * a)
 
print(entero_minimo(4,100,5))

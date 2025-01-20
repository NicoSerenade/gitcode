'''Se lanza una pelota hacia arriba con una velocidad de 10 m/s. Después de 1 s, ¿cuál es su velocidad y qué altura habrá alcanzado? (Utiliza g = 9.8 m/s²).'''

#datos iniciales
vo = 10
g = 9.8

#encontrando el tiempo de caida
t_caida = vo/g #after clearing the time
v_en_hmax = 0
h_max = ((vo - v_en_hmax)/2) * t_caida
h_max = (g/2) * t_caida**2
#igualo las 2 expresiones: (vo/2) * t_caida = (g/2) * t_caida**2
# despejo el tiempo
t_caida = vo/g
print("t_caida", t_caida)
print("h_max", h_max)
d_caida1 = (g/2) * 1**2
print("d_caida1", d_caida1)

#altura tras 1 segundo
h_en_1 = (vo * 1) - d_caida1
print("h_en_1", h_en_1)

#velocidad tras 1 segundo
v_en_1 = g * (t_caida - 1)
print("v_en_1", v_en_1)

def crear_sospechoso(codigo: int, nombre: str, edad: int, altura: float, pantalon: str, camisa: str, usaba_gafas: bool, salon: str, coartada_confirmada: bool, huellas_confirmadas: bool) -> dict:
    sospechoso = {"codigo": codigo, "nombre": nombre, "edad": edad, "altura": altura, "pantalon": pantalon, "camisa": camisa, "usaba_gafas": usaba_gafas, "salon": salon, "coartada_confirmada": coartada_confirmada, "huellas_confirmadas": huellas_confirmadas}
    return sospechoso

def crear_perfil_culpable(edad_estimada: int, altura_estimada: float, color_pantalon: str, color_camisa: str, usaba_gafas: bool, salon_incidente: str) -> dict:
    perfil_culpable = {"edad_estimada": edad_estimada, "altura_estimada": altura_estimada, "color_pantalon": color_pantalon, "color_camisa": color_camisa, "usaba_gafas": usaba_gafas, "salon_incidente": salon_incidente}
    return perfil_culpable

def buscar_por_codigo(codigo: int, s1: dict, s2: dict, s3: dict, s4: dict) -> dict:
    sospechosos = [s1,s2,s3,s4]
    for s in sospechosos:
        if codigo == s["codigo"]:
            return s
        else:
            return {}

def filtrar_sospechosos_por_ubicacion(perfil_culpable: dict, s1: dict, s2: dict, s3: dict, s4: dict) -> str:
    salon_to_match = perfil_culpable["salon_incidente"].lower()
    sospechosos = [s1,s2,s3,s4]
    matching_codigos = []
    for s in sospechosos:
        if s["salon"].lower() == salon_to_match:
            matching_codigos.append(str(s["codigo"]))

    if matching_codigos:
        return ", ".join(matching_codigos)
    else:
        return "Ninguno"

def filtrar_sospechosos_por_vestimenta(perfil_culpable: dict, s1: dict, s2: dict, s3: dict, s4: dict) -> str:
    pant_to_match = perfil_culpable["color_pantalon"].lower()
    camisa_to_match = perfil_culpable["color_camisa"].lower()
    gafas_to_match = perfil_culpable["usaba_gafas"]
    sospechosos = [s1,s2,s3,s4]
    matching_codigos = []
    for s in sospechosos:
        if pant_to_match in s["pantalon"].split(";")[0].strip().lower() and camisa_to_match in s["camisa"].split(";")[0].strip().lower() and gafas_to_match == s["usaba_gafas"]:
            matching_codigos.append(str(s["codigo"]))

    if matching_codigos:
        return ", ".join(matching_codigos)
    else:
        return "Ninguno"

def filtrar_sospechosos_por_edad_altura(perfil_culpable: dict, s1: dict, s2: dict, s3: dict, s4: dict) -> str:
    edad_to_match = perfil_culpable["edad_estimada"]
    altura_to_match = perfil_culpable["altura_estimada"]
    sospechosos = [s1,s2,s3,s4]
    matching_codigos = []
    for s in sospechosos:
        if s["edad"] <= edad_to_match and altura_to_match - 10 <= s["altura"] <= altura_to_match + 10:
            matching_codigos.append(str(s["codigo"]))

    if matching_codigos:
        return ", ".join(matching_codigos)
    else:
        return "Ninguno"

def calcular_probabilidad_de_culpabilidad(codigo: int, perfil_culpable: dict, s1: dict, s2: dict, s3: dict, s4: dict) -> float:
    target = None
    sospechosos = [s1,s2,s3,s4]
    for s in sospechosos:
        if s["codigo"] == codigo:
            target = s
            break
    
    if target:
        a = 1 if str(target["codigo"]) in filtrar_sospechosos_por_ubicacion(perfil_culpable, s1, s2, s3, s4) else 0
        b = 1 if str(target["codigo"]) in filtrar_sospechosos_por_vestimenta(perfil_culpable, s1, s2, s3, s4) else 0
        c = 1 if str(target["codigo"]) in filtrar_sospechosos_por_edad_altura(perfil_culpable, s1, s2, s3, s4) else 0

        probabilidad = (a * 0.45) + (b * 0.35) + (c * 0.20)

    else:
        probabilidad = 0.0

    return round(probabilidad,2)

def encontrar_sospechoso_con_mayor_probabilidad(perfil_culpable: dict, s1: dict, s2: dict, s3: dict, s4: dict) -> dict:
    p_s1 = calcular_probabilidad_de_culpabilidad(s1["codigo"], perfil_culpable, s1, s2, s3, s4)
    p_s2 = calcular_probabilidad_de_culpabilidad(s2["codigo"], perfil_culpable, s1, s2, s3, s4)
    p_s3 = calcular_probabilidad_de_culpabilidad(s3["codigo"], perfil_culpable, s1, s2, s3, s4)
    p_s4 = calcular_probabilidad_de_culpabilidad(s4["codigo"], perfil_culpable, s1, s2, s3, s4)
                     
    sospechoso_principal = s1
    max_prob = p_s1

    if p_s2 > max_prob:
        max_prob = p_s2
        sospechoso_principal = s2

    if p_s3 > max_prob:
        max_prob = p_s3
        sospechoso_principal = s3

    if p_s4 > max_prob:
        max_prob = p_s4
        sospechoso_principal = s4

    tie1 = p_s1 == max_prob
    tie2 = p_s2 == max_prob
    tie3 = p_s3 == max_prob
    tie4 = p_s4 == max_prob

    draw = ((tie1 and tie2) or (tie1 and tie3) or (tie1 and tie4) or 
              (tie2 and tie3) or (tie2 and tie4) or (tie3 and tie4))

    if draw:
        no_cua1 = tie1 and not s1["coartada_confirmada"]
        no_cua2 = tie2 and not s2["coartada_confirmada"]
        no_cua3 = tie3 and not s3["coartada_confirmada"]
        no_cua4 = tie4 and not s4["coartada_confirmada"]

        if ((no_cua1 and no_cua2) or (no_cua1 and no_cua3) or (no_cua1 and no_cua4) or 
              (no_cua2 and no_cua3) or (no_cua2 and no_cua4) or (no_cua3 and no_cua4) or not any([no_cua1 and no_cua2 and no_cua3 and no_cua4])):
            
            huella1 = no_cua1 and s1["huellas_confirmadas"]
            huella2 = no_cua2 and s2["huellas_confirmadas"]
            huella3 = no_cua3 and s3["huellas_confirmadas"]
            huella4 = no_cua4 and s4["huellas_confirmadas"]

            if huella1:
                sospechoso_principal = s1
            elif huella2:
                sospechoso_principal = s2
            elif huella3:
                sospechoso_principal = s3
            elif huella4:
                sospechoso_principal = s4

            else:
                if no_cua1:
                    sospechoso_principal = s1
                elif no_cua2:
                    sospechoso_principal = s2
                elif no_cua3:
                    sospechoso_principal = s3
                elif no_cua4:
                    sospechoso_principal = s4                 

        else:
            if no_cua1:
                sospechoso_principal = s1
            elif no_cua2:
                sospechoso_principal = s2
            elif no_cua3:
                sospechoso_principal = s3
            elif no_cua4:
                sospechoso_principal = s4    

        
    return sospechoso_principal
            
import os

def valida_fecha(dia, mes, anio, semestre):
    return True

def devuelve_situaciones(identificador):
    if identificador == 'a':
        return "Hechos de violencia sexual"
    elif identificador == 'b':
        return "Hechos de acoso sexual"
    elif identificador == 'c':
        return "Hechos con connotación sexista"
    else: 
        return "Comportamientos y acciones de violencia"

def devuelve_genero(identificador):
    if identificador == 'm':
        return "Mujer"
    elif identificador == 'v':
        return "Varón"
    else:
        return "Otre"

def devuelve_claustro(identificador):
    if identificador == 'e':
        return "Estudiante"
    elif identificador == 'n':
        return "No Docente"
    elif identificador == 'd':
            return "Docente"
    else:
        return "Graduade"

def solicita_tipos_situaciones():
    tipos = ''
    contador = 0
    flag = True
    print("Tipos de situaciones vivenciadas:")
    print("a) Hechos de violencia sexual \nb) Hechos de acoso sexual \nc) Hechos con connotación sexista \nd) Comportamientos y acciones de violencia")
    while flag:
        tipo = input("Elija una opción: ")
        
        if tipo != 'a' and tipo != 'b' and tipo != 'c' and tipo != 'd':
            print("La opción ingresada es incorrecta.")
        else:
            print("--DEBUG-- Eligió", tipo)
            tipos = tipos + devuelve_situaciones(tipo) + " - "
            eleccion = input("¿Desea ingresar otra opción? S/N: ")
            contador = contador + 1
            if eleccion == 'N' or eleccion == 'n':
                flag = False
                
    return tipos, contador

def mostrar_denuncia(anio, semestre, nro_exp, dia, mes, genero_denunciante, claustro_denunciante, genero_denunciado, claustro_denunciado, tipos_situaciones):
    os.system('cls')
    print("Datos de la denuncia:")
    print("Número de expediente:", nro_exp)
    print("Fecha de denuncia:", dia, "/", mes, "/", anio)
    print("Genero auto percibido de la persona denunciante:", devuelve_genero(genero_denunciante))
    print("Claustro al que pertenece la persona denunciante:", devuelve_claustro(claustro_denunciante))
    print("Tipo/s de situación/es vivenciada/s:", tipos_situaciones)
    print("Género de la persona denunciada:", devuelve_genero(genero_denunciado))
    print("Claustro de la persona denunciada:", devuelve_claustro(claustro_denunciado))
    input("Presione Enter para continuar.")

def main():
    anio = 0
    while anio < 2021:
        anio = int(input("Ingrese en año del informe: "))
        if anio < 2021:
            print("El año ingresado es incorrecto!")
    
    semestre = 0
    while semestre != 1 and semestre != 2:
        semestre = int(input("Ingrese en semestre del informe: "))
        if semestre != 1 and semestre != 2:
            print("El semestre ingresado es incorrecto!")
    
    cant_den_mujeres = cant_den_varones = cant_den_otres = cant_den_estudiantes = cant_den_nodocentes = cant_den_docentes = cant_den_graduades = mayor_exp = cant_pares = acum_varios_tipos = 0
    
    continuar = 'S'
    while continuar == 'S':
        # EXPEDIENTE
        expediente = int(input("Ingrese el número de expediente: "))
        if expediente > mayor_exp:
            mayor_exp = expediente
        
        #FECHA
        fecha_valida = False
        while not fecha_valida:
            dia = int(input("Ingrese el día de la denuncia: "))
            mes = int(input("Ingrese el mes de la denuncia: "))
            fecha_valida = valida_fecha(dia, mes, anio, semestre)
            if not fecha_valida:
                print("Los datos ingresados son incorrectos! Reingrese día y mes")

        # GENERO DENUNCIANTE
        genero_denunciante = '-'
        while genero_denunciante != 'm' and genero_denunciante != 'v' and genero_denunciante != 'x':
            genero_denunciante = input("Ingrese el género autopercibido de la persona denunciante: (x - m - v)")
            if genero_denunciante != 'm' and genero_denunciante != 'v' and genero_denunciante != 'x':
                print("El dato ingresado es incorrecto! Reingrese el género.")
        if genero_denunciante == 'm':
            cant_den_mujeres = cant_den_mujeres + 1  
        elif genero_denunciante == 'v':
            cant_den_varones = cant_den_varones + 1   
        else:    
            cant_den_otres = cant_den_otres + 1
        
        #CLAUSTRO DENUNCIANTE
        claustro_denunciante = '-'
        while claustro_denunciante != 'e' and claustro_denunciante != 'n' and claustro_denunciante != 'd' and claustro_denunciante != 'd':
            claustro_denunciante = input("Ingrese el género autopercibido de la persona denunciante: (e, n, d, g)")
            if claustro_denunciante != 'e' and claustro_denunciante != 'n' and claustro_denunciante != 'd' and claustro_denunciante != 'd':
                print("El dato ingresado es incorrecto! Reingrese el claustro.")
        if claustro_denunciante == 'e':
            cant_den_estudiantes = cant_den_estudiantes + 1  
        elif claustro_denunciante == 'n':
            cant_den_nodocentes = cant_den_nodocentes + 1   
        elif claustro_denunciante == 'd':
            cant_den_docentes = cant_den_docentes + 1  
        else:    
            cant_den_graduades = cant_den_graduades + 1            
                
        # TIPOS
        tipos_situaciones, cont_tipos = solicita_tipos_situaciones()
        if cont_tipos > 1:
            acum_varios_tipos = acum_varios_tipos + 1
        
        # GENERO DENUNCIADO
        genero_denunciado = '-'
        while genero_denunciado != 'm' and genero_denunciado != 'v' and genero_denunciado != 'x':
            genero_denunciado = input("Ingrese el género autopercibido de la persona denunciante: (x - m - v)")
            if genero_denunciado != 'm' and genero_denunciado != 'v' and genero_denunciado != 'x':
                print("El dato ingresado es incorrecto! Reingrese el género.")
        
        #CLAUSTRO DENUNCIANTE
        claustro_denunciado = '-'
        while claustro_denunciado != 'e' and claustro_denunciado != 'n' and claustro_denunciado != 'd' and claustro_denunciado != 'g':
            claustro_denunciado = input("Ingrese el género autopercibido de la persona denunciante: (e, n, d, g)")
            if claustro_denunciado != 'e' and claustro_denunciado != 'n' and claustro_denunciado != 'd' and claustro_denunciado != 'g':
                print("El dato ingresado es incorrecto! Reingrese el claustro.")
  
        if claustro_denunciado == claustro_denunciante:
            cant_pares = cant_pares + 1
            
        mostrar_denuncia(anio, semestre, expediente, dia, mes, genero_denunciante, claustro_denunciante, genero_denunciado, claustro_denunciado, tipos_situaciones)

main()
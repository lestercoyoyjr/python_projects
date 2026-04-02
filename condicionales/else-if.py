ingreso_mensual = 100000

if ingreso_mensual < 10000:
    if ingreso_mensual < 5000:
        print("Eres clase baja baja")
    else:        
        print("Eres clase baja")
elif ingreso_mensual < 50000:
    print("Eres clase media")
elif ingreso_mensual >= 100000:
    print("Eres clase alta")
else:    
    print("No se pudo determinar tu clase social")
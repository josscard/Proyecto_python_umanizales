
asignatures = [{"name_asignature": "espa", "cant_credit": 3, "cost_credit": 30000, "students_registered": []},
            {"name_asignature": "ingles", "cant_credit": 3, "cost_credit": 36000, "students_registered": []},
            {"name_asignature": "religion", "cant_credit": 3, "cost_credit": 36000, "students_registered": []}]



def register_asignature():
    try:
        n_asignature= input("Ingrese el nombre de la asignatura: ")
        for asig in asignatures:
            if asig["name_asignature"] == n_asignature:
                print(f"La asignatura {n_asignature} ya se encuentra creada.")
                return
        cant_credit= int(input("Ingrese la cantidad de créditos que tendrá la asignatura: "))
        cost_credit= float(input("ingrese el costo de cada crédito de la asignatura: "))
        asignatures.append({"name_asignature":n_asignature, "cant_credit":cant_credit, "cost_credit":cost_credit, "students_registered":[]})
        print(f"la asignatura {n_asignature} ha sido registrada satisfactoriamente")        
    except ValueError: 
        print("Ingrese valores numéricos válidos")              
        


def register_student():
    asignature= input("Ingrese el nombre de la asignatura donde va a registrar el estudiante: ")
    
    for asig in asignatures:
        if asig["name_asignature"]== asignature:
            try: 
                name = input("Ingrese el nombre del estudiante: ")
                gender = input("Ingrese el genero del estudiante: ")
                age = int(input("Ingrese la edad del estudiante: "))
                stratum = int(input("Ingrese el estrato del estudiante (1,2,3,4,5 o 6): "))
                if stratum not in [1,2,3,4,5,6]:
                    print("Estrato inválido, ingrese (1,2,3,4,5 o 6)")
                    return
                asig["students_registered"].append({"name":name, "gender":gender, "age":age, "stratum":stratum})
                print(f"El estudiante {name} ha sido registrado satisfactoriamente en {asignature}")
                return
            except ValueError:
                print("Por favor Ingrese valores válidos.")
            
    print(f"La asignatura {asignature} no ha sido encontrada")
        
    
def calculate_cost_tuition(asignature):
    total_cost_tuition= 0
    for asig in asignatures:
        if asig["name_asignature"] == asignature:
            for student in asig["students_registered"]:
                discount_by_stratum = {1: 0.5, 2: 0.3, 3: 0.1, 4: 0, 5: 0, 6: 0}.get(student["stratum"], 0)
                cost_asignature = asig["cant_credit"] * asig["cost_credit"]
                total_cost_tuition += cost_asignature * (1 - discount_by_stratum)
    return total_cost_tuition

    
def show_students_registereds_asignatures():
    for asig in asignatures:
        students = len(asig["students_registered"])
        print(f"Asignatura: {asig["name_asignature"]}, Estudiantes: {students}")
        
def show_asignature_most_money_collected():
    max_collected_by_tuition= 0
    asignature_most_money_collected=""
    
    for asig in asignatures:
        money_collected = calculate_cost_tuition(asig["name_asignature"])  
        if money_collected > max_collected_by_tuition:
            max_collected_by_tuition = money_collected
            asignature_most_money_collected = asig["name_asignature"]
    print(f"Asignatura con más dinero recaudado es: {asignature_most_money_collected}")
            
def promedium_cost_credits():
    total_cost_credits = 0
    total_cant_asignatures = len(asignatures)
    for asig in asignatures:
        total_cost_credits += asig["cost_credit"]
    promedium = total_cost_credits / total_cant_asignatures if total_cant_asignatures > 0 else 0
    print(f"Promedio de costos de créditos: {promedium}")
    
def show_total_money_collected_tuition():
    total_money_collected_all_asignature = 0
    
    for asig in asignatures:
        money_collected = calculate_cost_tuition(asig["name_asignature"])  
        total_money_collected_all_asignature += money_collected
    print(f"Total dinero recaudado: {total_money_collected_all_asignature}")
    
    




def calculate_discount_by_stratum(stratum):
    total_discount= 0
    for asig in asignatures:
        for student in asig["students_registered"]:
            if student["stratum"] == stratum:
                discount= {1: 0.5, 2: 0.3, 3: 0.1, 4: 0, 5: 0, 6: 0}[stratum]
                cost = asig["cant_credit"] * asig["cost_credit"]
                total_discount += cost * discount
    print(f"Total descuento para estrato {stratum} es: {total_discount}")
    
    
def students_by_stratum(asignature, stratum):
    for asig in asignatures:
        if asig["name_asignature"]== asignature:
            total = sum(1 for student in asig["students_registered"] 
                        if student["stratum"] == stratum)
            print(f"En la asignatura {asignature} hay {total} estudiantes de estrato {stratum}")
            
def show_asignatures():
    for asig in asignatures:
        print(f"Asignatura: {asig["name_asignature"]}, costo crédito: {asig["cost_credit"]}, cantidad créditos: {asig["cant_credit"]}")
    
def menu():
    while True:
        print("...............................................................")
        print("******************MENÚ REGISTRO ACADÉMICO**********************")  
        print("*******************SELECCIONE UNA OPCIÓN***********************")       
        print("*             1. REGISTRAR ASIGNATURA                         *")   
        print("*             2. REGISTRAR ESTUDIANTE                         *")  
        print("*             3. CALCULAR DESCUENTO POR ESTRATO               *")
        print("*             4. VER INFORMACIÓN REGISTRADA                   *")
        print("*             5. VER ESTUDIANTES POR ESTRATO                  *")
        print("*             6. VER ASIGNATURAS REGISTRADAS                  *")
        print("*             7. SALIR DEL SISTEMA                            *")
        opcion = input("SELECCIONE UNA OPCION: ")
    
    
    
        if opcion == "1":
                register_asignature()
        elif opcion == "2":
                register_student()
        elif opcion == "3":
                stratum = int(input("Ingrese el estrato para calcular descuentos (1, 2 o 3): "))
                calculate_discount_by_stratum(stratum)
        elif opcion == "4":
                menu_option_four()
        elif opcion == "5":
                asignatura = input("Ingrese el nombre de la asignatura: ")
                estrato = int(input("Ingrese el estrato: "))
                students_by_stratum(asignatura, estrato)
                
        elif opcion == "6":
            show_asignatures()
        elif opcion == "7":
                print("Saliendo...")
                break
        else:
            print("Opción no válida, intente de nuevo.")
            
def menu_option_four():
    while True:
        print("...............................................................")
        print("******************MENÚ INFORMACIÓN REGISTRADA******************")  
        print("*********************SELECCIONE UNA OPCIÓN*********************")       
        print("*          1. ESTUDIANTES MATRICULADOS POR ASIGNATURA         *")   
        print("*         2. ASIGNATURA CON MAS DINERO RECAUDADO              *")  
        print("*         3. PROMEDIO DE COSTOS DE CRÉDITOS ASIGNATURAS       *")
        print("*         4. TOTAL DINERO RECAUDADO                           *")
        print("*         5. REGRESAR AL MENÚ PRINCIPAL                       *")
        opcion = input("SELECCIONE UNA OPCION: ")

        if opcion == "1":
                show_students_registereds_asignatures()
                
        elif opcion == "2":
                show_asignature_most_money_collected()
        elif opcion == "3":
                promedium_cost_credits()
        elif opcion == "4":
                show_total_money_collected_tuition()
        elif opcion == "5":
                menu()
                
        else:
            print("Opción no válida, intente de nuevo.")

    
menu()
        

        
from operaciones import OperacionesDB

def mostrar_menu():
    print("\n--- Menú de Opciones ---")
    print("1. Insertar un registro en una Colección")
    print("2. Insertar varios registros en una Colección")
    print("3. Actualizar un registro de una Colección")
    print("4. Actualizar varios registros en una Colección")
    print("5. Obtener registros por un filtro (un atributo)")
    print("6. Obtener registros por un filtro (varios atributos)")
    print("7. Obtener registros sin valores nulos en un atributo")
    print("8. Obtener registros sin un atributo específico")
    print("9. Obtener registros que coincidan con una lista de valores")
    print("10. Obtener registros con valores numéricos superiores a un filtro")
    print("11. Obtener registros que cumplan una condición u otra")
    print("12. Obtener registros que no cumplan una condición")
    print("13. Eliminar un registro de una Colección")
    print("14. Eliminar varios registros de una Colección")
    print("15. Buscar y ordenar de forma ascendente")
    print("16. Buscar y ordenar de forma descendente")
    print("17. Buscar y limitar a 10 registros")
    print("18. Filtrar por una expresión regular")
    print("19. Filtrar por operación de tipo Array")
    print("20. Filtrar por operación de tipo Evaluation")
    print("0. Salir")

def main():
    db = OperacionesDB()
    
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción: ")

        if opcion == "0":
            print("Saliendo del programa...")
            break
        elif opcion == "1":
            db.insertar_un_registro()
        elif opcion == "2":
            db.insertar_varios_registros()
        elif opcion == "3":
            db.actualizar_un_registro()
        elif opcion == "4":
            db.actualizar_varios_registros()
        elif opcion == "5":
            db.obtener_registros_por_estado()
        elif opcion == "6":
            db.obtener_por_filtro_estado_y_no_video()
        elif opcion == "7":
            db.obtener_registros_sin_null_en_video()
        elif opcion == "8":
            db.obtener_registros_sin_atributo()
        elif opcion == "9":
            db.obtener_por_lista_de_valores()
        elif opcion == "10":
            db.obtener_usuarios_con_mas_de_x_cursos()
        elif opcion == "11":
            db.obtener_usuarios_cursando_o_con_cursos()
        elif opcion == "12":
            db.obtener_usuarios_no_disponibles()
        elif opcion == "13":
            db.eliminar_resenia()
        elif opcion == "14":
            db.eliminar_todas_resenas()    
        elif opcion == "15":
            db.buscar_orden_ascendente()
        elif opcion == "16":
            db.buscar_orden_descendente()
        elif opcion == "17":
            db.buscar_limite_10()
        elif opcion == "18":
            db.filtrar_por_regex()
        elif opcion == "19":
            db.filtrar_array()
        elif opcion == "20":
            db.insertar_datos()
        else:
            print("Opción inválida. Intenta de nuevo una opción de entre las mostradas.")

if __name__ == "__main__":
    main()
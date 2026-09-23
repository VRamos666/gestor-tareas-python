import json
import os

# Nombre del archivo donde se guardarán los datos
ARCHIVO_DATOS = "mis_tareas.json"

def cargar_tareas():
    """Lee el archivo JSON si existe. Si no, regresa una lista vacía."""
    if os.path.exists(ARCHIVO_DATOS):
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    return []

def guardar_tareas(tareas):
    """Guarda la lista de tareas en el archivo JSON."""
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
        json.dump(tareas, archivo, indent=4, ensure_ascii=False)

def main():
    # Cargamos las tareas guardadas previamente
    tareas = cargar_tareas()

    while True:
        print("\n=== 📝 MI GESTOR DE TAREAS ===")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Eliminar tarea")
        print("4. Salir")
        
        opcion = input("\nElige una opción (1-4): ")

        if opcion == "1":
            print("\n--- TUS TAREAS ---")
            if not tareas:
                print("No tienes tareas pendientes.")
            else:
                for i, tarea in enumerate(tareas, 1):
                    print(f"{i}. {tarea}")

        elif opcion == "2":
            nueva_tarea = input("\nEscribe la nueva tarea: ").strip()
            if nueva_tarea:
                tareas.append(nueva_tarea)
                guardar_tareas(tareas)
                print(f"¡Tarea '{nueva_tarea}' guardada con éxito!")
            else:
                print("No puedes agregar una tarea vacía.")

        elif opcion == "3":
            if not tareas:
                print("\nNo hay tareas para eliminar.")
            else:
                print("\n--- ELIMINAR TAREA ---")
                for i, tarea in enumerate(tareas, 1):
                    print(f"{i}. {tarea}")
                
                try:
                    num = int(input("\nIngresa el número de la tarea a eliminar: "))
                    if 1 <= num <= len(tareas):
                        tarea_eliminada = tareas.pop(num - 1)
                        guardar_tareas(tareas)
                        print(f"¡Tarea '{tarea_eliminada}' eliminada!")
                    else:
                        print("Número no válido.")
                except ValueError:
                    print("Por favor, ingresa solo números.")

        elif opcion == "4":
            print("\n¡Hasta luego! Tus tareas han quedado guardadas.")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
from clases import GestionImagenes


def menu():
    print("1. Ingresar Paciente (DICOM)")
    print("2. Ingresar Imagen (JPG/PNG)")
    print("3. Rotar Imagen DICOM")
    print("4. Binarizar y Transformar Imagen JPG/PNG")
    print("5. Salir")


gestion_imagenes = GestionImagenes()

while True:
    menu()
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        ruta_dicom = input("Ingrese la ruta del archivo DICOM: ")
        gestion_imagenes.cargar_dicom(ruta_dicom)

    elif opcion == "2":
        ruta_imagen = input("Ingrese la ruta de la imagen (JPG/PNG): ")
        gestion_imagenes.cargar_jpg_png(ruta_imagen)

    elif opcion == "3":
        clave = input("Ingrese el ID del paciente cuya imagen desea rotar: ")
        grados = int(input("Ingrese los grados de rotación (90, 180 o 270): "))
        gestion_imagenes.rotar_dicom(clave, grados)

    elif opcion == "4":
        clave = input("Ingrese la clave de la imagen JPG/PNG a binarizar y transformar: ")
        umbral = int(input("Ingrese el umbral de binarización: "))
        tam_kernel = int(input("Ingrese el tamaño del kernel para la transformación morfológica: "))
        gestion_imagenes.binarizar_transformar(clave, umbral, tam_kernel)

    elif opcion == "5":
        break

    else:
        print("Opción inválida. Por favor, elija una opción válida.")

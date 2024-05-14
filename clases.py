import numpy as np
import pydicom
from PIL import Image
from skimage import io, morphology, util
from skimage.transform import rotate


class Paciente:
    def __init__(self, nombre, edad, ID, imagen_nifti):
        self.nombre = nombre
        self.edad = edad
        self.ID = ID
        self.imagen_nifti = imagen_nifti

class GestionImagenes:
    def __init__(self):
        self.pacientes = {}
        self.archivos = {}

    def cargar_dicom(self, ruta):
        
        ds = pydicom.dcmread(ruta)
        nombre = ds.PatientName
        edad = ds.PatientAge
        ID = ds.PatientID

        paciente = Paciente(nombre, edad, ID, ruta)

        imagen_nifti = "simulacion_nifti.nii"
        
        self.pacientes[ID] = paciente
        
        self.archivos[ruta] = imagen_nifti

        print("Paciente cargado exitosamente.")

    def cargar_jpg_png(self, ruta):
        
        imagen = io.imread(ruta)

        self.archivos[ruta] = imagen

        print("Imagen cargada exitosamente.")

    def rotar_dicom(self, clave, grados):
        if clave in self.pacientes:
            ruta_dicom = self.pacientes[clave].imagen_nifti
            ds = pydicom.dcmread(ruta_dicom)
            imagen = ds.pixel_array

           
            imagen_rotada = np.rot90(imagen, grados // 90)

            
            ds.PixelData = imagen_rotada.tobytes()
            ds.Rows, ds.Columns = ds.Columns, ds.Rows  
            ds.save_as("imagen_rotada.dcm")

            print("Imagen DICOM rotada y guardada exitosamente.")
        else:
            print("Clave de paciente no encontrada.")

    def binarizar_transformar(self, clave, umbral, tam_kernel):
        if clave in self.archivos:
            imagen = self.archivos[clave]

            imagen_binarizada = util.img_as_ubyte(imagen > umbral)

            kernel = morphology.disk(tam_kernel)
            imagen_transformada = morphology.binary_opening(imagen_binarizada, kernel)

            imagen_transformada_texto = Image.fromarray(imagen_transformada)
            texto = f"Imagen binarizada\nUmbral: {umbral}, Tamaño de kernel: {tam_kernel}"
            imagen_transformada_texto.save(f"imagen_transformada_{clave}.png")

            print("Imagen binarizada y transformada guardada exitosamente.")
        else:
            print("Clave de imagen no encontrada.")

import sys
import os
from datetime import datetime

# Agregar el directorio raíz al path para imports
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from Logic.VersionLogic import VersionLogic
from Dto.Version import Version


class ProbarVersion:
    """Clase para probar la funcionalidad de VersionLogic"""
    
    def __init__(self):
        """Inicializa la clase de prueba"""
        self.logic = VersionLogic()
    
    def probar_insercion(self):
        """
        Prueba la inserción de una versión en la base de datos
        """
        try:
            # Crear una versión de prueba
            nueva_version = Version(
                VersionId="v1.0",
                VersionBd="1.0.0",
                VersionSistema="1.0.0",
                Descripcion="Primera versión",
                FechaInstalacion=datetime.now(),
                Activo=True
            )
            
            print("Intentando insertar versión...")
            print(f"Datos: {nueva_version}")
            
            # Insertar en la base de datos
            resultado = self.logic.insertar_version(nueva_version)
            
            if resultado:
                print("✓ Versión insertada exitosamente")
            else:
                print("✗ Error al insertar la versión")
                
        except Exception as e:
            print(f"✗ Error durante la prueba: {e}")
            
    def probarListar(self):
        try:
            print("\nListando versiones...")
            resultado = self.logic.listar_versiones()
            
            if resultado:
                print(f"✓ Se encontraron {len(resultado)} versión(es):")
                for version in resultado:
                    print(f"  - {version}")
            else:
                print("No hay versiones registradas")
                
        except Exception as e:
            print(f"✗ Error al listar versiones: {e}")


# Ejecutar prueba si se ejecuta directamente
if __name__ == "__main__":
    print("=== Prueba de inserción de versión ===\n")
    
    prueba = ProbarVersion()
    prueba.probar_insercion()
    prueba.probarListar()
    
    print("\n=== Fin de la prueba ===")

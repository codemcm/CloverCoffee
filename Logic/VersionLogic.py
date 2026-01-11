import sys
import os
from datetime import datetime

# Agregar el directorio raíz al path para imports
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from DataAccess.Mysql import MysqlConnector
from Dto.Version import Version


class VersionLogic:
    """Clase de lógica de negocio para gestionar versiones del sistema"""
    
    def __init__(self):
        """Inicializa la lógica de versiones"""
        pass
    
    def insertar_version(self, version: Version) -> bool:
        """
        Inserta una nueva versión en la base de datos
        
        Args:
            version: Objeto Version con los datos a insertar
            
        Returns:
            True si la inserción fue exitosa, False en caso contrario
            
        Raises:
            Exception: Si ocurre un error durante la inserción
        """
        try:
            # Crear conexión a la base de datos
            with MysqlConnector() as db:
                # Formatear la fecha para MySQL
                fecha_str = version.FechaInstalacion.strftime('%Y-%m-%d %H:%M:%S') if version.FechaInstalacion else datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                
                # Construir la consulta SQL INSERT
                sql = f"""
                    INSERT INTO version 
                    (VersionId, VersionBD, VersionSistema, Descripcion, FechaInstalacion, Activo) 
                    VALUES 
                    ('{version.VersionId}', '{version.VersionBd}', '{version.VersionSistema}', 
                     '{version.Descripcion}', '{fecha_str}', {1 if version.Activo else 0})
                """
                
                # Ejecutar la consulta
                db.consulta_simple(sql)
                
                return True
                
        except Exception as e:
            raise Exception(f"Error al insertar versión: {e}")
    
    def obtener_version_activa(self) -> Version:
        """
        Obtiene la versión activa del sistema
        
        Returns:
            Objeto Version con la versión activa, o None si no hay ninguna
        """
        try:
            with MysqlConnector() as db:
                sql = "SELECT * FROM versiones WHERE activo = 1 LIMIT 1"
                cursor = db.consulta_retorno(sql)
                
                row = cursor.fetchone()
                if row:
                    return Version(
                        version_id=row['version_id'],
                        version_bd=row['version_bd'],
                        version_sistema=row['version_sistema'],
                        descripcion=row['descripcion'],
                        fecha_instalacion=row['fecha_instalacion'],
                        activo=bool(row['activo'])
                    )
                return None
                
        except Exception as e:
            raise Exception(f"Error al obtener versión activa: {e}")
    
    def listar_versiones(self) -> list[Version]:
        """
        Lista todas las versiones del sistema
        
        Returns:
            Lista de objetos Version
        """
        try:
            with MysqlConnector() as db:
                sql = "SELECT * FROM versiones ORDER BY fecha_instalacion DESC"
                cursor = db.consulta_retorno(sql)
                
                versiones = []
                for row in cursor:
                    version = Version(
                        version_id=row['version_id'],
                        version_bd=row['version_bd'],
                        version_sistema=row['version_sistema'],
                        descripcion=row['descripcion'],
                        fecha_instalacion=row['fecha_instalacion'],
                        activo=bool(row['activo'])
                    )
                    versiones.append(version)
                
                return versiones
                
        except Exception as e:
            raise Exception(f"Error al listar versiones: {e}")

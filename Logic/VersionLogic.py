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
        pass
    
    def insertar_version(self, version: Version) -> bool:
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
                sql = "SELECT * FROM version WHERE Activo = 1 LIMIT 1"
                cursor = db.consulta_retorno(sql)
                
                row = cursor.fetchone()
                if row:
                    return Version(
                        VersionId=row['VersionId'],
                        VersionBd=row['VersionBD'],
                        VersionSistema=row['VersionSistema'],
                        Descripcion=row['Descripcion'],
                        FechaInstalacion=row['FechaInstalacion'],
                        Activo=bool(row['Activo'])
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
                sql = "SELECT * FROM version ORDER BY FechaInstalacion DESC"
                cursor = db.consulta_retorno(sql)
                
                versiones = []
                for row in cursor:
                    version = Version(
                        VersionId=row['VersionId'],
                        VersionBd=row['VersionBD'],
                        VersionSistema=row['VersionSistema'],
                        Descripcion=row['Descripcion'],
                        FechaInstalacion=row['FechaInstalacion'],
                        Activo=bool(row['Activo'])
                    )
                    versiones.append(version)
                
                return versiones
                
        except Exception as e:
            raise Exception(f"Error al listar versiones: {e}")

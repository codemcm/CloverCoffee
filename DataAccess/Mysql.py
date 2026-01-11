import mysql.connector
import configparser
import os
from typing import Optional, Any


class MysqlConnector:
    """Conector MySQL para Python basado en MysqlConnector.php"""
    
    def __init__(self):
        """
        Inicializa la conexión a MySQL leyendo la configuración desde configDev.ini
        """
        # Leer configuración del archivo .ini
        config_path = os.path.join(os.path.dirname(__file__), "configDev.ini")
        config = configparser.ConfigParser()
        config.read(config_path)
        
        # Obtener credenciales de la configuración
        self.host = config.get('DEFAULT', 'host')
        self.username = config.get('DEFAULT', 'username')
        self.password = config.get('DEFAULT', 'pass')
        self.database = config.get('DEFAULT', 'database')
        
        # Establecer conexión
        try:
            self.con = mysql.connector.connect(
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.database,
                charset='utf8mb4',
                collation='utf8mb4_general_ci'
            )
            
            if not self.con.is_connected():
                raise Exception("Database connection failed")
                
        except mysql.connector.Error as err:
            raise Exception(f"Database connection failed: {err}")
    
    def consulta_simple(self, sql: str) -> Any:
        """
        Ejecuta una consulta SQL simple (INSERT, UPDATE, DELETE)
        
        Args:
            sql: La consulta SQL a ejecutar
            
        Returns:
            El cursor con los resultados
            
        Raises:
            Exception: Si ocurre un error en la consulta
        """
        try:
            cursor = self.con.cursor()
            cursor.execute(sql)
            self.con.commit()
            return cursor
        except mysql.connector.Error as e:
            raise Exception(f"Query error: {e}")
    
    def consulta_retorno(self, sql: str) -> Any:
        """
        Ejecuta una consulta SQL que retorna resultados (SELECT)
        
        Args:
            sql: La consulta SQL a ejecutar
            
        Returns:
            El cursor con los resultados
            
        Raises:
            Exception: Si ocurre un error en la consulta
        """
        try:
            cursor = self.con.cursor(dictionary=True)
            cursor.execute(sql)
            return cursor
        except mysql.connector.Error as e:
            raise Exception(f"Query error: {e}")
    
    def get_connection(self) -> mysql.connector.MySQLConnection:
        """
        Obtiene la conexión MySQL
        
        Returns:
            La conexión MySQL
        """
        return self.con
    
    def close(self):
        """
        Cierra la conexión a la base de datos
        """
        if self.con and self.con.is_connected():
            self.con.close()
    
    def __enter__(self):
        """Soporte para context manager"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Cierra la conexión al salir del context manager"""
        self.close()

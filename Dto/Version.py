from datetime import datetime
from typing import Optional


class Version:
    """Clase DTO para representar una versión del sistema"""
    
    def __init__(
        self,
        VersionId: str = "",
        VersionBd: str = "",
        VersionSistema: str = "",
        Descripcion: str = "",
        FechaInstalacion: Optional[datetime] = None,
        Activo: bool = False
    ):
        """
        Inicializa una nueva instancia de Version
        
        Args:
            VersionId: Identificador de la versión
            VersionBd: Versión de la base de datos
            VersionSistema: Versión del sistema
            Descripcion: Descripción de la versión
            FechaInstalacion: Fecha de instalación de la versión
            Activo: Indica si la versión está activa
        """
        self.VersionId = VersionId
        self.VersionBd = VersionBd
        self.VersionSistema = VersionSistema
        self.Descripcion = Descripcion
        self.FechaInstalacion = FechaInstalacion or datetime.now()
        self.Activo = Activo
    
    def __repr__(self) -> str:
        """Representación en string del objeto"""
        return (
            f"Version(VersionId='{self.VersionId}', "
            f"VersionBd='{self.VersionBd}', "
            f"VersionSistema='{self.VersionSistema}', "
            f"Descripcion='{self.Descripcion}', "
            f"FechaInstalacion={self.FechaInstalacion}, "
            f"Activo={self.Activo})"
        )
    
    def __str__(self) -> str:
        """Representación legible del objeto"""
        return f"Versión {self.VersionSistema} - BD: {self.VersionBd} - Activo: {self.Activo}"
    
    def to_dict(self) -> dict:
        """
        Convierte el objeto a un diccionario
        
        Returns:
            Diccionario con las propiedades del objeto
        """
        return {
            'VersionId': self.VersionId,
            'VersionBd': self.VersionBd,
            'VersionSistema': self.VersionSistema,
            'Descripcion': self.Descripcion,
            'FechaInstalacion': self.FechaInstalacion.isoformat() if self.FechaInstalacion else None,
            'Activo': self.Activo
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Version':
        """
        Crea una instancia de Version desde un diccionario
        
        Args:
            data: Diccionario con los datos de la versión
            
        Returns:
            Nueva instancia de Version
        """
        fecha = data.get('FechaInstalacion')
        if isinstance(fecha, str):
            fecha = datetime.fromisoformat(fecha)
        
        return cls(
            VersionId=data.get('VersionId', ''),
            VersionBd=data.get('VersionBd', ''),
            VersionSistema=data.get('VersionSistema', ''),
            Descripcion=data.get('Descripcion', ''),
            FechaInstalacion=fecha,
            Activo=data.get('Activo', False)
        )

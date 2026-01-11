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
    
    def __str__(self) -> str:
        """Representación legible del objeto"""
        return f"Versión {self.VersionSistema} - BD: {self.VersionBd} - Activo: {self.Activo}"

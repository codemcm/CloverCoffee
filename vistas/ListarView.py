import sys
import os
import tkinter as tk
from tkinter import ttk, messagebox

# Agregar el directorio raíz al path para imports
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from Logic.VersionLogic import VersionLogic


class ListarView:
    """Ventana para listar versiones del sistema"""
    
    def __init__(self):
        """Inicializa la ventana"""
        self.logic = VersionLogic()
        self.ventana = tk.Tk()
        self.ventana.title("Listar Versiones")
        self.ventana.geometry("700x400")
        
        # Crear componentes
        self.crear_interfaz()
    
    def crear_interfaz(self):
        """Crea los componentes de la interfaz"""
        
        # Título
        titulo = tk.Label(
            self.ventana, 
            text="Lista de Versiones del Sistema",
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=10)
        
        # Botón para cargar versiones
        boton_cargar = tk.Button(
            self.ventana,
            text="Cargar Versiones",
            command=self.cargar_versiones,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 12),
            padx=20,
            pady=10
        )
        boton_cargar.pack(pady=10)
        
        # Frame para la tabla
        frame_tabla = tk.Frame(self.ventana)
        frame_tabla.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(frame_tabla)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Treeview (tabla)
        self.tabla = ttk.Treeview(
            frame_tabla,
            columns=("VersionId", "VersionBD", "VersionSistema", "Descripcion", "FechaInstalacion", "Activo"),
            show="headings",
            yscrollcommand=scrollbar.set
        )
        
        # Configurar columnas
        self.tabla.heading("VersionId", text="Version ID")
        self.tabla.heading("VersionBD", text="Version BD")
        self.tabla.heading("VersionSistema", text="Version Sistema")
        self.tabla.heading("Descripcion", text="Descripción")
        self.tabla.heading("FechaInstalacion", text="Fecha Instalación")
        self.tabla.heading("Activo", text="Activo")
        
        # Ajustar ancho de columnas
        self.tabla.column("VersionId", width=80)
        self.tabla.column("VersionBD", width=80)
        self.tabla.column("VersionSistema", width=100)
        self.tabla.column("Descripcion", width=200)
        self.tabla.column("FechaInstalacion", width=140)
        self.tabla.column("Activo", width=60)
        
        self.tabla.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.tabla.yview)
        
        # Label para contador
        self.label_contador = tk.Label(
            self.ventana,
            text="Total de versiones: 0",
            font=("Arial", 10)
        )
        self.label_contador.pack(pady=5)
    
    def cargar_versiones(self):
        """Carga las versiones desde la base de datos"""
        try:
            # Limpiar tabla
            for item in self.tabla.get_children():
                self.tabla.delete(item)
            
            # Obtener versiones
            versiones = self.logic.listar_versiones()
            
            if versiones:
                # Agregar cada versión a la tabla
                for version in versiones:
                    self.tabla.insert("", tk.END, values=(
                        version.VersionId,
                        version.VersionBd,
                        version.VersionSistema,
                        version.Descripcion,
                        version.FechaInstalacion.strftime('%Y-%m-%d %H:%M:%S') if version.FechaInstalacion else "",
                        "Sí" if version.Activo else "No"
                    ))
                
                # Actualizar contador
                self.label_contador.config(text=f"Total de versiones: {len(versiones)}")
                messagebox.showinfo("Éxito", f"Se cargaron {len(versiones)} versión(es)")
            else:
                self.label_contador.config(text="Total de versiones: 0")
                messagebox.showinfo("Información", "No hay versiones registradas")
                
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar versiones:\n{str(e)}")
    
    def mostrar(self):
        """Muestra la ventana"""
        self.ventana.mainloop()


# Ejecutar si se ejecuta directamente
if __name__ == "__main__":
    app = ListarView()
    app.mostrar()

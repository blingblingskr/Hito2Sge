
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import mysql.connector
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# Función para conectar a la base de datos
def conectar_db():
    
    """Conectar a la base de datos MySQL."""
    return mysql.connector.connect(
        host="localhost",
        user="root",     
        password="campusfp",  
        database="ENCUESTAS"  
    )

def limpiar_campos():
    # Limpiar todos los campos de entrada
    entry_idEncuesta.delete(0, 'end')
    entry_edad.delete(0, 'end')
    entry_sexo.delete(0, 'end')
    entry_bebidasSemana.delete(0, 'end')
    entry_cervezasSemana.delete(0, 'end')
    entry_bebidasFinSemana.delete(0, 'end')
    entry_bebidasDestiladasSemana.delete(0, 'end')
    entry_vinosSemana.delete(0, 'end')
    entry_perdidasControl.delete(0, 'end')
    entry_diversionDependenciaAlcohol.delete(0, 'end')
    entry_problemasDigestivos.delete(0, 'end')
    entry_tensionAlta.delete(0, 'end')
    entry_dolorCabeza.delete(0, 'end')
    
def insertar_datos():
    # Obtener los valores de los campos de entrada
    edad = entry_edad.get()
    sexo = entry_sexo.get()
    bebidas_semana = entry_bebidasSemana.get()
    cervezas_semana = entry_cervezasSemana.get()
    bebidas_fin_semana = entry_bebidasFinSemana.get()
    bebidas_destiladas_semana = entry_bebidasDestiladasSemana.get()
    vinos_semana = entry_vinosSemana.get()
    perdidas_control = entry_perdidasControl.get()
    diversion_dependencia_alcohol = entry_diversionDependenciaAlcohol.get()
    problemas_digestivos = entry_problemasDigestivos.get()
    tension_alta = entry_tensionAlta.get()
    dolor_cabeza = entry_dolorCabeza.get()

    # Establecer la conexión con la base de datos
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Consulta SQL para insertar los datos
    query = """
    INSERT INTO ENCUESTA (edad, Sexo, BebidasSemana, CervezasSemana, BebidasFinSemana, 
    BebidasDestiladasSemana, VinosSemana, PerdidasControl, DiversionDependenciaAlcohol, 
    ProblemasDigestivos, TensionAlta, DolorCabeza) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    # Valores para el INSERT
    valores = (edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana,
               bebidas_destiladas_semana, vinos_semana, perdidas_control, diversion_dependencia_alcohol,
               problemas_digestivos, tension_alta, dolor_cabeza)

    try:
        # Ejecutar la consulta SQL
        cursor.execute(query, valores)
        # Confirmar los cambios en la base de datos
        conexion.commit()
        mostrar_datos()
        # Mostrar mensaje de éxito
        messagebox.showinfo("Éxito", "Datos insertados correctamente")

    except mysql.connector.Error as err:
        # Mostrar mensaje de error
        messagebox.showerror("Error", f"Error al insertar los datos: {err}")

    finally:
        # Cerrar la conexión
        cursor.close()
        conexion.close()
        
def actualizar_datos():
    # Obtener los valores de los campos de entrada
    id_encuesta = entry_idEncuesta.get()
    edad = entry_edad.get()
    sexo = entry_sexo.get()
    bebidas_semana = entry_bebidasSemana.get()
    cervezas_semana = entry_cervezasSemana.get()
    bebidas_fin_semana = entry_bebidasFinSemana.get()
    bebidas_destiladas_semana = entry_bebidasDestiladasSemana.get()
    vinos_semana = entry_vinosSemana.get()
    perdidas_control = entry_perdidasControl.get()
    diversion_dependencia_alcohol = entry_diversionDependenciaAlcohol.get()
    problemas_digestivos = entry_problemasDigestivos.get()
    tension_alta = entry_tensionAlta.get()
    dolor_cabeza = entry_dolorCabeza.get()

    # Establecer la conexión con la base de datos
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Consulta SQL para actualizar los datos
    query = """
    UPDATE ENCUESTA
    SET edad = %s, Sexo = %s, BebidasSemana = %s, CervezasSemana = %s, BebidasFinSemana = %s, 
        BebidasDestiladasSemana = %s, VinosSemana = %s, PerdidasControl = %s, DiversionDependenciaAlcohol = %s, 
        ProblemasDigestivos = %s, TensionAlta = %s, DolorCabeza = %s
    WHERE idEncuesta = %s
    """

    # Valores para el UPDATE
    valores = (edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana,
               bebidas_destiladas_semana, vinos_semana, perdidas_control, diversion_dependencia_alcohol,
               problemas_digestivos, tension_alta, dolor_cabeza, id_encuesta)

    try:
        # Ejecutar la consulta SQL
        cursor.execute(query, valores)
        
        # Verificar si alguna fila fue actualizada
        if cursor.rowcount > 0:
            # Confirmar los cambios en la base de datos
            conexion.commit()
            mostrar_datos()
            # Mostrar mensaje de éxito
            messagebox.showinfo("Éxito", "Datos actualizados correctamente")
        else:
            # Si no se actualizó ninguna fila
            messagebox.showwarning("Advertencia", "No se encontró el ID Encuesta para actualizar")
            
    except mysql.connector.Error as err:
        # Mostrar mensaje de error
        messagebox.showerror("Error", f"Error al actualizar los datos: {err}")

    finally:
        # Cerrar la conexión
        cursor.close()
        conexion.close()
        
def borrar_dato():
    # Obtener los valores de los campos de entrada
    id_encuesta = entry_idEncuesta.get()
    # Establecer la conexión con la base de datos
    conexion = conectar_db()
    cursor = conexion.cursor()
    # Consulta SQL para eliminar los datos
    query = """
    DELETE FROM ENCUESTA
    WHERE idEncuesta = %s
    """
    # Valores para el DELETE
    valores = (id_encuesta,)  # Cambié esto para ser una tupla
    try:
        # Ejecutar la consulta SQL
        cursor.execute(query, valores)
        
        # Verificar si alguna fila fue eliminada
        if cursor.rowcount > 0:
            # Confirmar los cambios en la base de datos
            conexion.commit()
            limpiar_campos()
            mostrar_datos()
            # Mostrar mensaje de éxito
            messagebox.showinfo("Éxito", "Datos eliminados correctamente")
        else:
            # Si no se eliminó ninguna fila
            messagebox.showwarning("Advertencia", "No se encontró el ID Encuesta para eliminar")
    except mysql.connector.Error as err:
        # Mostrar mensaje de error
        messagebox.showerror("Error", f"Error al eliminar los datos: {err}")
    finally:
        # Cerrar la conexión
        cursor.close()
        conexion.close()

def mostrar_datos():
   
    # Limpiar la tabla antes de mostrar los nuevos datos
    for row in treeview.get_children():
        treeview.delete(row)
    
    # Establecer la conexión con la base de datos
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Consulta SQL para recuperar todos los datos
    query = "SELECT * FROM ENCUESTA"
    
    try:
        # Ejecutar la consulta
        cursor.execute(query)
        # Obtener todos los resultados
        datos = cursor.fetchall()

        # Verificar si se obtuvieron datos
        if datos:
            # Insertar los resultados en la tabla
            for row in datos:
                treeview.insert("", "end", values=row)  # Inserta cada fila de datos
        else:
            messagebox.showinfo("Sin Datos", "No hay datos para mostrar.")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al obtener los datos: {err}")

    finally:
        # Cerrar la conexión
        cursor.close()
        conexion.close()
        
def ordenar_resultados():
    # Obtener el campo seleccionado
    campo_orden = combo_orden.get()
    # Determinar el orden (ascendente o descendente)
   
    
    # Establecer la conexión con la base de datos
    conexion = conectar_db()
    cursor = conexion.cursor()
    
    # Consulta SQL con ORDER BY
    query = f"SELECT * FROM ENCUESTA ORDER BY {campo_orden} ASC"
    
    try:
        cursor.execute(query)
        # Obtener los resultados
        resultados = cursor.fetchall()
        
        # Limpiar la tabla (si es necesario)
        for row in treeview.get_children():
            treeview.delete(row)
        
        # Mostrar los resultados en el Treeview
        for row in resultados:
            treeview.insert("", "end", values=row)
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conexion.close()
             
def on_treeview_select(event):
    
    selected_items = treeview.selection()
    if not selected_items:
        return  # Si no hay fila seleccionada, salimos de la función
    # Obtener el ID de la fila seleccionada
    selected_item = treeview.selection()[0]
    
    # Obtener los valores de la fila seleccionada
    item_values = treeview.item(selected_item, 'values')
    
    # Asignar los valores a los campos de entrada
    entry_idEncuesta.config(state="normal")  # Habilitar el campo ID Encuesta
    entry_idEncuesta.delete(0, tk.END)  # Limpiar el campo
    entry_idEncuesta.insert(0, item_values[0])  # Asignar ID Encuesta
    
    entry_edad.delete(0, tk.END)
    entry_edad.insert(0, item_values[1])  # Asignar Edad
    
    entry_sexo.delete(0, tk.END)
    entry_sexo.insert(0, item_values[2])  # Asignar Sexo
    
    entry_bebidasSemana.delete(0, tk.END)
    entry_bebidasSemana.insert(0, item_values[3])  # Asignar Bebidas por semana
    
    entry_cervezasSemana.delete(0, tk.END)
    entry_cervezasSemana.insert(0, item_values[4])  # Asignar Cervezas por semana
    
    entry_bebidasFinSemana.delete(0, tk.END)
    entry_bebidasFinSemana.insert(0, item_values[5])  # Asignar Bebidas fin de semana
    
    entry_bebidasDestiladasSemana.delete(0, tk.END)
    entry_bebidasDestiladasSemana.insert(0, item_values[6])  # Asignar Bebidas destiladas por semana
    
    entry_vinosSemana.delete(0, tk.END)
    entry_vinosSemana.insert(0, item_values[7])  # Asignar Vinos por semana
    
    entry_perdidasControl.delete(0, tk.END)
    entry_perdidasControl.insert(0, item_values[8])  # Asignar Pérdidas de control
    
    entry_diversionDependenciaAlcohol.delete(0, tk.END)
    entry_diversionDependenciaAlcohol.insert(0, item_values[9])  # Asignar Diversión/Dependencia alcohol
    
    entry_problemasDigestivos.delete(0, tk.END)
    entry_problemasDigestivos.insert(0, item_values[10])  # Asignar Problemas digestivos
    
    entry_tensionAlta.delete(0, tk.END)
    entry_tensionAlta.insert(0, item_values[11])  # Asignar Tensión alta
    
    entry_dolorCabeza.delete(0, tk.END)
    entry_dolorCabeza.insert(0, item_values[12])  # Asignar Dolor de cabeza
    
    entry_idEncuesta.config(state="disabled")  # Deshabilitar nuevamente el campo ID Encuesta        

def aplicar_filtro():
    # Obtener los valores de los filtros
    edad = entry_edad.get()
    sexo = entry_sexo.get()
    bebidas_semana = entry_bebidasSemana.get()
    cervezas_semana = entry_cervezasSemana.get()
    bebidas_fin_semana = entry_bebidasFinSemana.get()
    bebidas_destiladas_semana = entry_bebidasDestiladasSemana.get()
    vinos_semana = entry_vinosSemana.get()
    perdidas_control = entry_perdidasControl.get()
    diversion_dependencia_alcohol = entry_diversionDependenciaAlcohol.get()
    problemas_digestivos = entry_problemasDigestivos.get()
    tension_alta = entry_tensionAlta.get()
    dolor_cabeza = entry_dolorCabeza.get()

    # Establecer la conexión con la base de datos
    conexion = conectar_db()
    cursor = conexion.cursor()
    
    # Crear una lista de condiciones para el filtro
    condiciones = []
    valores = []

    # Agregar condiciones de filtro basadas en los valores ingresados
    if edad:
        condiciones.append("edad = %s")
        valores.append(edad)
    if sexo:
        condiciones.append("sexo = %s")
        valores.append(sexo)
    if bebidas_semana:
        condiciones.append("BebidasSemana = %s")
        valores.append(bebidas_semana)
    if cervezas_semana:
        condiciones.append("CervezasSemana = %s")
        valores.append(cervezas_semana)
    if bebidas_fin_semana:
        condiciones.append("BebidasFinSemana = %s")
        valores.append(bebidas_fin_semana)
    if bebidas_destiladas_semana:
        condiciones.append("BebidasDestiladasSemana = %s")
        valores.append(bebidas_destiladas_semana)
    if vinos_semana:
        condiciones.append("VinosSemana = %s")
        valores.append(vinos_semana)
    if perdidas_control:
        condiciones.append("PerdidasControl = %s")
        valores.append(perdidas_control)
    if diversion_dependencia_alcohol:
        condiciones.append("DiversionDependenciaAlcohol = %s")
        valores.append(diversion_dependencia_alcohol)
    if problemas_digestivos:
        condiciones.append("ProblemasDigestivos = %s")
        valores.append(problemas_digestivos)
    if tension_alta:
        condiciones.append("TensionAlta = %s")
        valores.append(tension_alta)
    if dolor_cabeza:
        condiciones.append("DolorCabeza = %s")
        valores.append(dolor_cabeza)

    # Si hay condiciones de filtro, se agregan a la consulta
    if condiciones:
        query = "SELECT * FROM ENCUESTA WHERE " + " AND ".join(condiciones)
    else:
        query = "SELECT * FROM ENCUESTA"
    
    try:
        # Ejecutar la consulta SQL con los filtros
        cursor.execute(query, tuple(valores))
        # Obtener los resultados
        resultados = cursor.fetchall()

        # Limpiar la tabla (si es necesario)
        for row in treeview.get_children():
            treeview.delete(row)

        # Mostrar los resultados en el Treeview
        for row in resultados:
            treeview.insert("", "end", values=row)

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conexion.close()

        
# Crear la ventana principal
root = tk.Tk()
root.geometry("800x800")  


# Botón para insertar los datos en la base de datos
boton_borrar = tk.Button(root, text="Limpiar", command=limpiar_campos)
boton_borrar.grid(row=0, column=2)

# Etiquetas y campos de entrada
label_idEncuesta = tk.Label(root, text="ID Encuesta:")
label_idEncuesta.grid(row=0, column=0)  # Añadir espacio (padding)
entry_idEncuesta = tk.Entry(root)
entry_idEncuesta.grid(row=0, column=1)
entry_idEncuesta.config(state="disabled")  # Deshabilitar el campo ID Encuesta

label_edad = tk.Label(root, text="Edad:")
label_edad.grid(row=1, column=0)
entry_edad = tk.Entry(root)
entry_edad.grid(row=1, column=1)

label_sexo = tk.Label(root, text="Sexo:")
label_sexo.grid(row=2, column=0)
entry_sexo = ttk.Combobox(root, values=["","Hombre", "Mujer"])
entry_sexo.grid(row=2, column=1)

label_bebidasSemana = tk.Label(root, text="Bebidas por semana:")
label_bebidasSemana.grid(row=3, column=0)
entry_bebidasSemana = tk.Entry(root)
entry_bebidasSemana.grid(row=3, column=1)

label_cervezasSemana = tk.Label(root, text="Cervezas por semana:")
label_cervezasSemana.grid(row=4, column=0)
entry_cervezasSemana = tk.Entry(root)
entry_cervezasSemana.grid(row=4, column=1)

label_bebidasFinSemana = tk.Label(root, text="Bebidas fin de semana:")
label_bebidasFinSemana.grid(row=5, column=0)
entry_bebidasFinSemana = tk.Entry(root)
entry_bebidasFinSemana.grid(row=5, column=1)

label_bebidasDestiladasSemana = tk.Label(root, text="Bebidas destiladas por semana:")
label_bebidasDestiladasSemana.grid(row=6, column=0)
entry_bebidasDestiladasSemana = tk.Entry(root)
entry_bebidasDestiladasSemana.grid(row=6, column=1)

label_vinosSemana = tk.Label(root, text="Vinos por semana:")
label_vinosSemana.grid(row=7, column=0)
entry_vinosSemana = tk.Entry(root)
entry_vinosSemana.grid(row=7, column=1)

label_perdidasControl = tk.Label(root, text="Pérdidas de control:")
label_perdidasControl.grid(row=8, column=0)
entry_perdidasControl = tk.Entry(root)
entry_perdidasControl.grid(row=8, column=1)

label_diversionDependenciaAlcohol = tk.Label(root, text="Diversión/Dependencia alcohol:")
label_diversionDependenciaAlcohol.grid(row=9, column=0)
entry_diversionDependenciaAlcohol = ttk.Combobox(root, values=["","Sí", "No"])
entry_diversionDependenciaAlcohol.grid(row=9, column=1)

label_problemasDigestivos = tk.Label(root, text="Problemas digestivos:")
label_problemasDigestivos.grid(row=10, column=0)
entry_problemasDigestivos = ttk.Combobox(root,values=["","Sí","No"])
entry_problemasDigestivos.grid(row=10, column=1)

label_tensionAlta = tk.Label(root, text="Tensión alta:")
label_tensionAlta.grid(row=11, column=0)
entry_tensionAlta =  ttk.Combobox(root,values=["","Sí","No","No lo se"])
entry_tensionAlta.grid(row=11, column=1)


label_dolorCabeza = tk.Label(root, text="Dolor de cabeza:")
label_dolorCabeza.grid(row=12, column=0)
entry_dolorCabeza =  ttk.Combobox(root,values=["","Nunca","Alguna vez","A menudo","Muy amenudo"])
entry_dolorCabeza.grid(row=12, column=1)



# Botón para insertar los datos en la base de datos
boton_insertar = tk.Button(root, text="Insertar", command=insertar_datos)
boton_insertar.grid(row=13, column=1)

# Botón para actualizar los datos en la base de datos
boton_actualizar = tk.Button(root, text="Actualizar", command=actualizar_datos)
boton_actualizar.grid(row=14, column=1)
# Botón para actualizar los datos en la base de datos
boton_actualizar = tk.Button(root, text="Borrar", command=borrar_dato)
boton_actualizar.grid(row=15, column=1)


# Crear un Combobox para seleccionar el campo de orden
label_orden = tk.Label(root, text="Selecciona campo para ordenar:")
label_orden.grid(row=16, column=0)
combo_orden = ttk.Combobox(root, values=["edad", "sexo", "BebidasSemana", "ProblemasDigestivos", "BebidasDestiladasSemana"])
combo_orden.grid(row=16, column=1)
combo_orden.set("edad")  # Valor predeterminado

# Botón para ordenar
boton_ordenar = tk.Button(root, text="Ordenar", command=ordenar_resultados)
boton_ordenar.grid(row=17, column=1)

boton_ordenar = tk.Button(root, text="Filtrar", command=aplicar_filtro)
boton_ordenar.grid(row=18, column=1)

  
# Crear la tabla para mostrar los datos
columns = ("idEncuesta", "edad", "sexo", "bebidasSemana", "cervezasSemana", "bebidasFinSemana", 
           "bebidasDestiladasSemana", "vinosSemana", "perdidasControl", "diversionDependenciaAlcohol", 
           "problemasDigestivos", "tensionAlta", "dolorCabeza")

treeview = ttk.Treeview(root, columns=columns, show="headings",height=12)

for col in columns:
    treeview.heading(col, text=col)
    treeview.column(col, width=100, anchor="center")
treeview.grid(row=19,column=0,columnspan=3)




TipoGrafica = tk.Label(root, text="Tipo de grafica")
TipoGrafica.grid(row=20, column=0)
entry_TipoGrafica =  ttk.Combobox(root,values=["Lineas","Pastel","Barras"])
entry_TipoGrafica.grid(row=21, column=0)

 #Combobox para seleccionar la columna a graficar
Label_Columna = tk.Label(root, text="Columna a graficar")
Label_Columna.grid(row=20, column=1)
entry_Columna = ttk.Combobox(root, values=columns)
entry_Columna.grid(row=21, column=1)
# Función para generar la gráfica
def generar_grafica():
    tipo = entry_TipoGrafica.get()
    columna = entry_Columna.get()

    if not tipo or not columna:
        print("Seleccione un tipo de gráfica y una columna.")
        return

    # Extraer los datos de la columna seleccionada, filtrando solo valores numéricos
    x_data = []
    y_data = []
    for item in treeview.get_children():
        valores = treeview.item(item)["values"]
        x_data.append(valores[0])  # Suponiendo que el idEncuesta es el eje X
        y_data.append(valores[columns.index(columna)])

    # Crear la figura de matplotlib
    fig, ax = plt.subplots()

    # Generar la gráfica según el tipo seleccionado
    if tipo == "Líneas":
        ax.plot(x_data, y_data, marker='o')
        ax.set_title(f"Gráfica de Líneas - {columna}")
        ax.set_xlabel("idEncuesta")
        ax.set_ylabel(columna)
    elif tipo == "Barras":
        ax.bar(x_data, y_data)
        ax.set_title(f"Gráfica de Barras - {columna}")
        ax.set_xlabel("idEncuesta")
        ax.set_ylabel(columna)
    elif tipo == "Pastel":
        if all(isinstance(val, (int, float)) for val in y_data):
            ax.pie(y_data, labels=x_data, autopct='%1.1f%%')
            ax.set_title(f"Gráfica de Pastel - {columna}")
        else:
            print("La gráfica de pastel requiere datos numéricos.")
            return
    else:
        print("Seleccione un tipo de gráfica válido.")
        return

     # Crear una nueva ventana emergente para mostrar la gráfica
    ventana_grafica = tk.Toplevel(root)
    ventana_grafica.title(f"Gráfica de {columna}")
    
    # Mostrar la gráfica en la ventana emergente
    canvas = FigureCanvasTkAgg(fig, master=ventana_grafica)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
# Botón para generar la gráfica
boton_ordenar = tk.Button(root, text="Generar Gráfica", command=generar_grafica)
boton_ordenar.grid(row=23, column=0)


def exportar_excel():
    # Abrir un cuadro de diálogo para guardar el archivo
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    if not file_path:
        return

    # Extraer los datos del Treeview
    data = []
    for item in treeview.get_children():
        data.append(treeview.item(item)["values"])

    # Crear un DataFrame de pandas con los datos del Treeview
    df = pd.DataFrame(data, columns=columns)

    # Exportar el DataFrame a Excel
    df.to_excel(file_path, index=False, engine='openpyxl')

    print(f"Datos exportados exitosamente a {file_path}")
# Botón para generar la gráfica
boton_exportarEXEL = tk.Button(root, text="Generar EXEL", command=exportar_excel)
boton_exportarEXEL.grid(row=22, column=0)   


# Asociar el evento de selección con la función
treeview.bind('<<TreeviewSelect>>', on_treeview_select)

# Cargar los datos automáticamente al iniciar la aplicación
mostrar_datos()

# Ejecutar el bucle principal de la interfaz gráfica
root.mainloop()

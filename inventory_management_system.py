import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import mysql.connector as sql

conn = sql.connect(
    host='localhost',
    user='root',
    password='admin',
    # port='3306',
    database='inventario'
)
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS inventario(
    id INT NOT NULL AUTO_INCREMENT,
    producto VARCHAR(100) NOT NULL,
    marca VARCHAR(50),
    descripcion TEXT,
    precio_unidad DECIMAL(9,2),
    cantidad INT,
    PRIMARY KEY(id)
)""")
cursor.close()
conn.close()

def main() :
    window = ctk.CTk(fg_color='#F8F895')
    window.geometry('850x400+230+150')
    window.resizable(False, False)
    window.title('Inventory Management')

    # SEARCH WINDOW
    def search_window():
        buscar_window = tk.Toplevel(window, bg='#CEF9CC')
        buscar_window.geometry('950x550+150+100')
        buscar_window.title('Search')
        buscar_window.columnconfigure([0,1,2,3,4,5], weight=1)

        buscar_lb = ctk.CTkLabel(
            buscar_window,
            text='Buscar',
            fg_color='#F2F4F4',
            text_color='#000000',
            font=('Constantia',32))
        buscar_lb.grid(column=0, columnspan=6, row=0, sticky='nsew')
        
        # ETIQUETAS Y ENTRIES DE search_window.

        # ID
        # ETIQUETA
        id_lb = ctk.CTkLabel(
            buscar_window,
            text='ID: ',
            text_color='#000000',
            font=('Calibri Black', 20))
        id_lb.grid(column=0, row=1, pady=50, sticky='e')
        # ENTRADA
        id_entry = ctk.CTkEntry(
            buscar_window,
            fg_color='#FFFFFF',
            text_color='#000000',
            placeholder_text='Número o "0"',
            border_width=1.3,
            font=('Calibri Black', 16))
        id_entry.grid(column=1, row=1, pady=50, sticky='w')

        # PRODUCTO
        # ETIQUETA
        producto_lb = ctk.CTkLabel(
            buscar_window,
            text='Producto: ',
            text_color='#000000',
            font=('Calibri Black', 20))
        producto_lb.grid(column=2, row=1, pady=50, sticky='e')
        # ENTRADA
        producto_entry = ctk.CTkEntry(
            buscar_window,
            fg_color='#FFFFFF',
            text_color='#000000',
            placeholder_text='Nombre o "Todos"',
            border_width=1.3,
            font=('Calibri Black', 16))
        producto_entry.grid(column=3, row=1, pady=50, sticky='w')
        
        # MARCA
        # ETIQUETA
        marca_lb = ctk.CTkLabel(
            buscar_window,
            text='Marca: ',
            text_color='#000000',
            font=('Calibri Black', 20))
        marca_lb.grid(column=4, row=1, pady=50, sticky='e')
        # ENTRADA
        marca_entry = ctk.CTkEntry(
            buscar_window,
            fg_color='#FFFFFF',
            text_color='#000000',
            placeholder_text='Marca o "Todas"',
            border_width=1.3,
            font=('Calibri Black', 16))
        marca_entry.grid(column=5, row=1, pady=50, sticky='w')
        
        # DESCRIPCIÓN. 
        # ETIQUETA
        descrip_lb = ctk.CTkLabel(
            buscar_window,
            text='Descripción: ',
            text_color='#000000',
            font=('Calibri Black', 20))
        descrip_lb.grid(column=0, row=3, sticky='e')
        # ENTRADA
        descrip_entry = ctk.CTkEntry(
            buscar_window,
            fg_color='#FFFFFF',
            text_color='#000000',
            placeholder_text='Palabras clave...',
            border_width=1.3,
            height=35,
            font=('Calibri Black', 16))
        descrip_entry.grid(column=1, columnspan=5, row=3, sticky='we', padx=10)
        
        # Buscar los datos ingresados.
        def accion() :
            id1 = id_entry.get()
            producto1 = producto_entry.get()
            marca1 = marca_entry.get()
            words = descrip_entry.get()

            fila = 6

            query = f"SELECT * FROM inventario WHERE id={id1} OR producto='{producto1}' OR marca='{marca1}' OR descripcion LIKE '%{words}%';"
        
            if id1 == '' or producto1 =='' or marca1 == '' or words == '' :
                messagebox.showerror('Error', 'Faltan datos en la búsqueda de elementos, revisar los campos.')
            else :
                conn = sql.connect(
                    host='localhost',
                    user='root',
                    password='admin',
                    # port='3306',
                    database='inventario'
                )
                cursor = conn.cursor()
                cursor.execute(query)
                rows = cursor.fetchall()
                if rows :
                    for row in rows :
                        ctk.CTkLabel(buscar_window,
                        fg_color='#CCD1D1',
                        text=f'{row[0]}',
                        text_color='#000000',
                        font=('Calibri Black', 16),
                        corner_radius=0).grid(column=0, row=fila, sticky='nswe',padx=2, pady=2)

                        ctk.CTkLabel(buscar_window,
                        fg_color='#CCD1D1',
                        text=f'{row[1]}',
                        text_color='#000000',
                        font=('Calibri Black', 16),
                        corner_radius=0).grid(column=1, row=fila, sticky='nswe',padx=2, pady=2)

                        ctk.CTkLabel(buscar_window,
                        fg_color='#CCD1D1',
                        text=f'{row[2]}',
                        text_color='#000000',
                        font=('Calibri Black', 16),
                        corner_radius=0).grid(column=2, row=fila, sticky='nswe',padx=2, pady=2)

                        ctk.CTkLabel(buscar_window,
                        fg_color='#CCD1D1',
                        text=f'{row[3]}',
                        text_color='#000000',
                        font=('Calibri Black', 16),
                        corner_radius=0).grid(column=3, row=fila, sticky='nswe',padx=2, pady=2)

                        ctk.CTkLabel(buscar_window,
                        fg_color='#CCD1D1',
                        text=f'{row[4]}',
                        text_color='#000000',
                        font=('Calibri Black', 16),
                        corner_radius=0).grid(column=4, row=fila, sticky='nswe',padx=2, pady=2)

                        ctk.CTkLabel(buscar_window,
                        fg_color='#CCD1D1',
                        text=f'{row[5]}',
                        text_color='#000000',
                        font=('Calibri Black', 16),
                        corner_radius=0).grid(column=5, row=fila, sticky='nswe',padx=2, pady=2)
                        fila += 1
                else :
                    messagebox.showerror('Error', 'No se han encontrado elementos en el inventario con esas características.')
                
                cursor.close()
                conn.close()
        # Botón de buscar
        boton_buscar = ctk.CTkButton(
            buscar_window,
            fg_color='#F6F6F6',
            text_color='#000000',
            border_width=1.4,
            border_color='#000000',
            hover_color='#C2C3C2',
            height=35,
            font=('Calibri Black', 17),
            text='BUSCAR',
            command=accion)
        boton_buscar.grid(column=2, columnspan=2, row=4, pady=20, sticky='we')

        # Salida de datos/output.
        id_output = ctk.CTkLabel(
            buscar_window,
            fg_color='#FFFFFF',
            text='ID',
            text_color='#2ECC71',
            font=('Calibri Black', 20),
            corner_radius=0)
        id_output.grid(column=0, row=5, sticky='nswe', padx=2)

        producto_output = ctk.CTkLabel(
            buscar_window,
            fg_color='#FFFFFF',
            text='Producto',
            text_color='#2ECC71',
            font=('Calibri Black', 20),
            corner_radius=0)
        producto_output.grid(column=1, row=5, sticky='nswe', padx=2)

        marca_output = ctk.CTkLabel(
            buscar_window,
            fg_color='#FFFFFF',
            text='Marca',
            text_color='#2ECC71',
            font=('Calibri Black', 20),
            corner_radius=0)
        marca_output.grid(column=2, row=5, sticky='nswe', padx=2)

        descrip_output = ctk.CTkLabel(
            buscar_window,
            fg_color='#FFFFFF',
            text='Descripción',
            text_color='#2ECC71',
            font=('Calibri Black', 20),
            corner_radius=0)
        descrip_output.grid(column=3, row=5, sticky='nswe', padx=2)

        precio_output = ctk.CTkLabel(
            buscar_window,
            fg_color='#FFFFFF',
            text='Precio/unidad',
            text_color='#2ECC71',
            font=('Calibri Black', 20),
            corner_radius=0)
        precio_output.grid(column=4, row=5, sticky='nswe', padx=2)

        cantidad_output = ctk.CTkLabel(
            buscar_window,
            fg_color='#FFFFFF',
            text='Cantidad',
            text_color='#2ECC71',
            font=('Calibri Black', 20),
            corner_radius=0)
        cantidad_output.grid(column=5, row=5, sticky='nswe', padx=2)
    
    # Ventana para cargar productos al inventario.
    def upload_window() :
        subir_window = tk.Toplevel(window, bg='#D6EAF8')
        subir_window.geometry('900x500+210+120')
        #subir_window.resizable(False, False)
        subir_window.title('Upload')
        subir_window.columnconfigure([0,1,2,3,4], weight=1)

        cargar_lb = ctk.CTkLabel(
            subir_window,
            text='Cargar Productos',
            fg_color='#F2F4F4',
            text_color='#000000',
            font=('Constantia',32),
            height=45)
        cargar_lb.grid(column=0, columnspan=5, row=0, sticky='new')

        def cargar() :
            producto2 = producto_entry.get()
            marca2 = marca_entry.get()
            precio2 = precio_entry.get()
            cantidad2 = cantidad_entry.get()
            descrip2 = descrip_entry.get()

            query1 = f"SELECT * FROM inventario WHERE producto='{producto2}' AND marca='{marca2}' AND precio_unidad={precio2} AND cantidad={cantidad2};"
            query2 = f"INSERT INTO inventario (producto, marca, descripcion, precio_unidad, cantidad) VALUES ('{producto2}', '{marca2}', '{descrip2}', {precio2}, {cantidad2});"

            if producto2 == '' or marca2 == '' or cantidad2 == '' or precio2 == '' :
                messagebox.showerror('Error', 'Datos de producto faltantes, revisa los campos.')
            else :
                conn = sql.connect(
                    host='localhost',
                    user='root',
                    password='admin',
                    # port='3306',
                    database='inventario'
                )
                cursor = conn.cursor()
                cursor.execute(query1)
                if cursor.fetchall() :
                    messagebox.showerror('Error', 'Ya existe un elemento con estas características dentro del inventario.')
                elif producto2 != '' and marca2 != '' and cantidad2 != '' and precio2 != '' :
                    cursor.execute(query2)
                    conn.commit()
                    messagebox.showinfo('Cargado', 'El elemento fue cargado al inventario.')
                
                cursor.close()
                conn.close()
        # Etiquetas y entradas de texto

        # Producto
        # Etiqueta
        producto_lb = ctk.CTkLabel(
            subir_window,
            text='Producto:',
            text_color='#000000',
            font=('Calibri Black', 18))
        producto_lb.grid(column=0, row=1, pady=20, padx=10, sticky='e')
        # Entrada
        producto_entry = ctk.CTkEntry(
            subir_window,
            font=('Calibri Black', 18),
            fg_color='#FFFFFF',
            placeholder_text='Nombre de producto...',
            height=30,
            text_color='#000000')
        producto_entry.grid(column=1, row=1, sticky='we')

        # Marca
        # Etiqueta
        marca_lb = ctk.CTkLabel(
            subir_window,
            text='Marca:',
            text_color='#000000',
            font=('Calibri Black', 18))
        marca_lb.grid(column=0, row=2, pady=20, padx=10, sticky='e')
        # Entrada
        marca_entry = ctk.CTkEntry(
            subir_window,
            font=('Calibri Black', 18),
            fg_color='#FFFFFF',
            placeholder_text='Nombre de marca...',
            height=30,
            text_color='#000000')
        marca_entry.grid(column=1, row=2, sticky='we')

        # Precio por unidad
        # Etiqueta
        precio_lb = ctk.CTkLabel(
            subir_window,
            text='Precio c/u:',
            text_color='#000000',
            font=('Calibri Black', 18))
        precio_lb.grid(column=2, row=1, pady=20, padx=10, sticky='e')
        # Entrada
        precio_entry = ctk.CTkEntry(
            subir_window,
            font=('Calibri Black', 18),
            fg_color='#FFFFFF',
            placeholder_text='Ej: 100,000.00',
            height=30,
            text_color='#000000')
        precio_entry.grid(column=3, row=1, sticky='we')

        # Cantidad disponible
        # Etiqueta
        cantidad_lb = ctk.CTkLabel(
            subir_window,
            text='Cantidad:',
            text_color='#000000',
            font=('Calibri Black', 18))
        cantidad_lb.grid(column=2, row=2, pady=20, padx=10, sticky='e')
        # Entrada
        cantidad_entry = ctk.CTkEntry(
            subir_window,
            font=('Calibri Black', 18),
            fg_color='#FFFFFF',
            placeholder_text='Cantidad disponible',
            height=30,
            text_color='#000000')
        cantidad_entry.grid(column=3, row=2, sticky='we')

        # Cantidad disponible
        # Etiqueta
        descrip_lb = ctk.CTkLabel(
            subir_window,
            text='Descripción:',
            text_color='#000000',
            font=('Calibri Black', 18))
        descrip_lb.grid(column=2, row=3, sticky='s', pady=10)
        # Entrada
        descrip_entry = ctk.CTkEntry(
            subir_window,
            font=('Calibri Black', 18),
            fg_color='#FFFFFF',
            placeholder_text='Descripción/palabras clave',
            height=35,
            text_color='#000000')
        descrip_entry.grid(column=0, columnspan=5, row=4, sticky='nwe', padx=50)

        # Botón para cargar el producto
        cargar_bt = ctk.CTkButton(
            subir_window,
            text='CARGAR AL INVENTARIO',
            font=('Calibri Black', 17),
            fg_color='#FFFFFF',
            border_color='#000000',
            border_width=1.4,
            text_color='#000000',
            hover_color='#C2C3C2',
            command=cargar)
        cargar_bt.grid(column=2, row=5, sticky='we', pady=20)
        
    # Ventana para modificar productos del inventario.
    def update_window() :
        modif_window = tk.Toplevel(window, bg='#BFC9CA')
        modif_window.geometry('900x500+210+120')
        #modif_window.resizable(False, False)
        modif_window.title('Edit')
        modif_window.columnconfigure([0,1,2,3,4,5], weight=1)

        modif_lb = ctk.CTkLabel(
            modif_window,
            text='Modificar Productos',
            fg_color='#F2F4F4',
            text_color='#000000',
            font=('Constantia',32),
            height=45)
        modif_lb.grid(column=0, columnspan=6, row=0, sticky='new')
        
        update_frame1 = ctk.CTkFrame(
            modif_window,
            fg_color='#F8F895',
            corner_radius=5)
        update_frame1.grid(column=0, columnspan=6, row=1, rowspan=4, sticky='nswe', padx=10, pady=20)

        update_frame1.columnconfigure([0,1,2,3,4,5,6,7,8,9], weight=1)
        update_frame1.rowconfigure([0,1,2], weight=1)
        
        # Etiquetas y entradas frame 1:
        
        # Producto
        # Etiqueta
        producto_lb = ctk.CTkLabel(
            update_frame1,
            text='Producto:',
            text_color='#000000',
            font=('Calibri Black', 18))
        producto_lb.grid(column=0, row=0, padx=10)
        # Entrada
        producto_entry = ctk.CTkEntry(
            update_frame1,
            font=('Calibri Black', 18),
            fg_color='#FFFFFF',
            placeholder_text='Nombre de producto actual...',
            height=30,
            text_color='#000000')
        producto_entry.grid(column=1, columnspan=7, row=0, sticky='we', pady=10)

        # Marca
        # Etiqueta
        marca_lb = ctk.CTkLabel(
            update_frame1,
            text='Marca:',
            text_color='#000000',
            font=('Calibri Black', 18))
        marca_lb.grid(column=0, row=1, padx=10)
        # Entrada
        marca_entry = ctk.CTkEntry(
            update_frame1,
            font=('Calibri Black', 18),
            fg_color='#FFFFFF',
            placeholder_text='Nombre de marca actual...',
            height=30,
            text_color='#000000')
        marca_entry.grid(column=1, columnspan=7, row=1, sticky='we', pady=10)

        # Descripción
        # Etiqueta
        descrip_lb = ctk.CTkLabel(
            update_frame1,
            text='Descripción:',
            text_color='#000000',
            font=('Calibri Black', 18))
        descrip_lb.grid(column=0, row=2, padx=10)
        # Entrada
        descrip_entry = ctk.CTkEntry(
            update_frame1,
            font=('Calibri Black', 18),
            fg_color='#FFFFFF',
            placeholder_text='Descripción/palabras clave...',
            height=30,
            text_color='#000000')
        descrip_entry.grid(column=1, columnspan=7, row=2, sticky='we', pady=10)

        def buscar_elemento() :
            producto = producto_entry.get()
            marca = marca_entry.get()
            descrip = descrip_entry.get()
            query1 = f"SELECT * FROM inventario WHERE producto='{producto}' AND marca='{marca}' AND descripcion LIKE '%{descrip}%';"
            
            if producto == '' or marca == '' or descrip == '' :
                messagebox.showerror('Error', 'Datos de producto faltantes, revisar los campos.')
            else :    
                conn = sql.connect(
                    host='localhost',
                    user='root',
                    password='admin',
                    # port='3306',
                    database='inventario'
                )
                cursor = conn.cursor()
                cursor.execute(query1)
                row = cursor.fetchall()
                if  row :
                    for i in row :
                        ctk.CTkLabel(modif_window,
                            fg_color='#FFFFFF',
                            text=f'{i[0]}',
                            text_color='#000000',
                            font=('Calibri Black', 17),
                            corner_radius=0).grid(column=0, row=6, sticky='nswe',padx=2, pady=2, ipady=10)

                        ctk.CTkLabel(modif_window,
                            fg_color='#FFFFFF',
                            text=f'{i[1]}',
                            text_color='#000000',
                            font=('Calibri Black', 17),
                            corner_radius=0).grid(column=1, row=6, sticky='nswe',padx=2, pady=2, ipady=10)

                        ctk.CTkLabel(modif_window,
                            fg_color='#FFFFFF',
                            text=f'{i[2]}',
                            text_color='#000000',
                            font=('Calibri Black', 17),
                            corner_radius=0).grid(column=2, row=6, sticky='nswe',padx=2, pady=2, ipady=10)

                        ctk.CTkLabel(modif_window,
                            fg_color='#FFFFFF',
                            text=f'{i[3]}',
                            text_color='#000000',
                            font=('Calibri Black', 17),
                            corner_radius=0).grid(column=3, row=6, sticky='nswe',padx=2, pady=2, ipady=10)

                        ctk.CTkLabel(modif_window,
                            fg_color='#FFFFFF',
                            text=f'{i[4]}',
                            text_color='#000000',
                            font=('Calibri Black', 17),
                            corner_radius=0).grid(column=4, row=6, sticky='nswe',padx=2, pady=2, ipady=10)

                        ctk.CTkLabel(modif_window,
                            fg_color='#FFFFFF',
                            text=f'{i[5]}',
                            text_color='#000000',
                            font=('Calibri Black', 17),
                            corner_radius=0).grid(column=5, row=6, sticky='nswe',padx=2, pady=2, ipady=10)
                        # Datos nuevos

                        # Frame datos nuevos
                        update_frame2 = ctk.CTkFrame(
                            modif_window,
                            fg_color='#CEF9CC',
                            corner_radius=5)
                        update_frame2.grid(column=0, columnspan=6, row=9, rowspan=4, sticky='nswe', padx=10, pady=20)

                        update_frame2.columnconfigure([0,1,2,3,4,5,6,7,8,9], weight=1)
                        update_frame2.rowconfigure([0,1,2,3,4,5], weight=1)

                        # Etiquetas y entradas frame 1:
                        ctk.CTkLabel(
                            update_frame2,
                            text='Cambios',
                            text_color='#000000',
                            font=('Calibri Black', 23),
                            fg_color='#58D68D'
                        ).grid(column=0, columnspan=10, row=0, sticky='nswe', ipady=10)
                        
                        # Producto
                        # Etiqueta
                        producto_nuevo_lb = ctk.CTkLabel(
                            update_frame2,
                            text='Producto:',
                            text_color='#000000',
                            font=('Calibri Black', 18))
                        producto_nuevo_lb.grid(column=0, row=1, padx=10)
                        # Entrada
                        producto_nuevo_entry = ctk.CTkEntry(
                            update_frame2,
                            font=('Calibri Black', 18),
                            fg_color='#FFFFFF',
                            placeholder_text='Nombre de producto nuevo...',
                            height=30,
                            text_color='#000000')
                        producto_nuevo_entry.grid(column=1, columnspan=7, row=1, sticky='we', pady=10)

                        # Marca
                        # Etiqueta
                        marca_nuevo_lb = ctk.CTkLabel(
                            update_frame2,
                            text='Marca:',
                            text_color='#000000',
                            font=('Calibri Black', 18))
                        marca_nuevo_lb.grid(column=0, row=2, padx=10)
                        # Entrada
                        marca_nuevo_entry = ctk.CTkEntry(
                            update_frame2,
                            font=('Calibri Black', 18),
                            fg_color='#FFFFFF',
                            placeholder_text='Nombre de marca nuevo...',
                            height=30,
                            text_color='#000000')
                        marca_nuevo_entry.grid(column=1, columnspan=7, row=2, sticky='we', pady=10)

                        # Precio nuevo
                        # Etiqueta
                        precio_nuevo_lb = ctk.CTkLabel(
                            update_frame2,
                            text='Precio:',
                            text_color='#000000',
                            font=('Calibri Black', 18))
                        precio_nuevo_lb.grid(column=0, row=3, padx=10)
                        # Entrada
                        precio_nuevo_entry = ctk.CTkEntry(
                            update_frame2,
                            font=('Calibri Black', 18),
                            fg_color='#FFFFFF',
                            placeholder_text='Nombre de precio nuevo...',
                            height=30,
                            text_color='#000000')
                        precio_nuevo_entry.grid(column=1, columnspan=7, row=3, sticky='we', pady=10)

                        # Cantidad
                        # Etiqueta
                        cantidad_nueva_lb = ctk.CTkLabel(
                            update_frame2,
                            text='Cantidad:',
                            text_color='#000000',
                            font=('Calibri Black', 18))
                        cantidad_nueva_lb.grid(column=0, row=4, padx=10)
                        # Entrada
                        cantidad_nueva_entry = ctk.CTkEntry(
                            update_frame2,
                            font=('Calibri Black', 18),
                            fg_color='#FFFFFF',
                            placeholder_text='Cantidad disponible ahora...',
                            height=30,
                            text_color='#000000')
                        cantidad_nueva_entry.grid(column=1, columnspan=7, row=4, sticky='we', pady=10)

                        # Descripción nueva
                        # Etiqueta
                        descrip_nueva_lb = ctk.CTkLabel(
                            update_frame2,
                            text='Descripción:',
                            text_color='#000000',
                            font=('Calibri Black', 18))
                        descrip_nueva_lb.grid(column=0, row=5, padx=10)
                        # Entrada
                        descrip_nueva_entry = ctk.CTkEntry(
                            update_frame2,
                            font=('Calibri Black', 18),
                            fg_color='#FFFFFF',
                            placeholder_text='Descripción/palabras clave...',
                            height=30,
                            text_color='#000000')
                        descrip_nueva_entry.grid(column=1, columnspan=7, row=5, sticky='we', pady=10)
                        # Función de update
                        def update_data() :
                            new_producto = producto_nuevo_entry.get()
                            new_marca = marca_nuevo_entry.get()
                            new_descrip = descrip_nueva_entry.get()
                            new_precio = precio_nuevo_entry.get()
                            new_cantidad = cantidad_nueva_entry.get()

                            query_a = f"SELECT * FROM inventario WHERE producto='{new_producto}' AND marca='{new_marca}' AND descripcion='{new_descrip}' AND precio_unidad={new_precio} AND cantidad={new_cantidad};"
                            query_b = f"UPDATE inventario SET producto='{new_producto}', marca='{new_marca}', descripcion='{new_descrip}', precio_unidad={new_precio}, cantidad={new_cantidad} WHERE id={i[0]};"

                            if new_producto == '' or new_marca == '' or new_descrip == '' or new_precio == '' or new_cantidad == '' :
                                messagebox.showerror('Error', 'Datos faltantes en los CAMBIOS, revisa los campos.')
                            else :
                                conn = sql.connect(
                                    host='localhost',
                                    user='root',
                                    password='admin',
                                    # port='3306',
                                    database='inventario'
                                )
                                cursor = conn.cursor()
                                cursor.execute(query_a)
                                if cursor.fetchone() :
                                    messagebox.showerror('Error', 'Ya existe en el inventario un elemento con esas características.')
                                else :
                                    cursor.execute(query_b)
                                    conn.commit()
                                    messagebox.showinfo('Cambios', 'Los cambios se guardaron correctamente')
                                
                                cursor.close()
                                conn.close()
                        # Botón de mofidicar
                        boton_modif = ctk.CTkButton(
                            update_frame2,
                            text='GUARDAR CAMBIOS',
                            text_color='#000000',
                            font=('Calibri Black', 18),
                            border_color='#000000',
                            border_width=1.4,
                            fg_color='#FFFFFF',
                            hover_color='#C2C3C2',
                            command=update_data) 
                        boton_modif.grid(column=8, columnspan=2, row=1, rowspan=5, sticky='nswe', padx=30, pady=30)
                else :
                    messagebox.showerror('Error', 'No se ha encontrado el elemento en el inventario.\nRevisa los datos ingresados.')
                
                cursor.close()
                conn.close()
        # Botón de buscar
        boton_buscar = ctk.CTkButton(
            update_frame1,
            text='BUSCAR',
            text_color='#000000',
            font=('Calibri Black', 18),
            border_color='#000000',
            border_width=1.4,
            fg_color='#FFFFFF',
            hover_color='#C2C3C2',
            command=buscar_elemento)
        boton_buscar.grid(column=8, columnspan=2, row=0, rowspan=3, sticky='nswe', padx=10, pady=10)

        # Output de consulta a la base
        id_output = ctk.CTkLabel(
            modif_window,
            fg_color='#FFFFFF',
            text='ID',
            text_color='#000000',
            font=('Calibri Black', 20),
            corner_radius=0)
        id_output.grid(column=0, row=5, sticky='nswe', padx=2, pady=2)

        producto_output = ctk.CTkLabel(
            modif_window,
            fg_color='#FFFFFF',
            text='Producto',
            text_color='#000000',
            font=('Calibri Black', 20),
            corner_radius=0)
        producto_output.grid(column=1, row=5, sticky='nswe', padx=2, pady=2)

        marca_output = ctk.CTkLabel(
            modif_window,
            fg_color='#FFFFFF',
            text='Marca',
            text_color='#000000',
            font=('Calibri Black', 20),
            corner_radius=0)
        marca_output.grid(column=2, row=5, sticky='nswe', padx=2, pady=2)

        descrip_output = ctk.CTkLabel(
            modif_window,
            fg_color='#FFFFFF',
            text='Descripción',
            text_color='#000000',
            font=('Calibri Black', 20),
            corner_radius=0)
        descrip_output.grid(column=3, row=5, sticky='nswe', padx=2, pady=2)

        precio_output = ctk.CTkLabel(
            modif_window,
            fg_color='#FFFFFF',
            text='Precio/unidad',
            text_color='#000000',
            font=('Calibri Black', 20),
            corner_radius=0)
        precio_output.grid(column=4, row=5, sticky='nswe', padx=2, pady=2)

        cantidad_output = ctk.CTkLabel(
            modif_window,
            fg_color='#FFFFFF',
            text='Cantidad',
            text_color='#000000',
            font=('Calibri Black', 20),
            corner_radius=0)
        cantidad_output.grid(column=5, row=5, sticky='nswe', padx=2, pady=2)

    # Ventana para eliminar productos del inventario.
    def delete_window() :
        eliminar_window = tk.Toplevel(window, bg='#E74C3C')
        eliminar_window.geometry('900x500+210+120')
        #eliminar_window.resizable(False, False)
        eliminar_window.title('Delete')
        eliminar_window.columnconfigure([0,1,2,3,4,5], weight=1)

        eliminar_lb = ctk.CTkLabel(
            eliminar_window,
            text='Eliminar Productos',
            fg_color='#F2F4F4',
            text_color='#000000',
            font=('Constantia',32),
            height=45)
        eliminar_lb.grid(column=0, columnspan=6, row=0, sticky='new')
        
        # Input frame
        delete_frame = ctk.CTkFrame(
            eliminar_window,
            fg_color='#F2F4F4',
            corner_radius=5)
        delete_frame.grid(column=0, columnspan=6, row=1, rowspan=4, sticky='nswe', padx=10, pady=35)
        delete_frame.columnconfigure([0,1,2,3], weight=1)
        delete_frame.rowconfigure([0,1,2,3], weight=1)

        # Instrucción 1
        ctk.CTkLabel(
            delete_frame,
            text='Introduzca el ID del elemento que desea eliminar.',
            text_color='#000000',
            fg_color='#FFFFFF',
            font=('Calibri Black', 20)
        ).grid(column=0, columnspan=4, row=0, sticky='nswe', ipady=5, pady=2)
        
        # Etiqueta e input ID.
        ctk.CTkLabel(
            delete_frame,
            text='ID:  ',
            text_color='#000000',
            fg_color='#F2F4F4',
            font=('Calibri Black', 23)
        ).grid(column=0, columnspan=2, row=1, pady=10, sticky='e')

        id_entry = ctk.CTkEntry(
            delete_frame,
            font=('Calibri Black', 18),
            fg_color='#FFFFFF',
            placeholder_text='Número de ID',
            text_color='#000000',
            height=35)
        id_entry.grid(column=2, columnspan=2, row=1, sticky='w', pady=10)
        
        # Instrucción 2
        ctk.CTkLabel(
            delete_frame,
            text='(Para saber el ID de un elemento, puede buscarlo en la opción 1 del inventario)',
            text_color='#000000',
            fg_color='#F2F4F4',
            font=('Calibri Black', 17)
        ).grid(column=0, columnspan=4, row=2, sticky='nswe', ipady=5)

        def ver_elemento() :
            see_id = id_entry.get()

            query = f"SELECT * FROM inventario WHERE id={see_id};"
            
            if see_id == '' :
                messagebox.showerror('Error', 'No se ha ingresado ningún ID.')
            else :
                conn = sql.connect(
                    host='localhost',
                    user='root',
                    password='admin',
                    # port='3306',
                    database='inventario'
                )
                cursor = conn.cursor()
                cursor.execute(query)
                fila = cursor.fetchall()
                if fila :
                    for i in fila :
                        ctk.CTkLabel(eliminar_window,
                            fg_color='#FFFFFF',
                            text=f'{i[0]}',
                            text_color='#000000',
                            font=('Calibri Black', 17),
                            corner_radius=0).grid(column=0, row=6, sticky='nswe',padx=2, pady=2, ipady=10)

                        ctk.CTkLabel(eliminar_window,
                            fg_color='#FFFFFF',
                            text=f'{i[1]}',
                            text_color='#000000',
                            font=('Calibri Black', 17),
                            corner_radius=0).grid(column=1, row=6, sticky='nswe',padx=2, pady=2, ipady=10)

                        ctk.CTkLabel(eliminar_window,
                            fg_color='#FFFFFF',
                            text=f'{i[2]}',
                            text_color='#000000',
                            font=('Calibri Black', 17),
                            corner_radius=0).grid(column=2, row=6, sticky='nswe',padx=2, pady=2, ipady=10)

                        ctk.CTkLabel(eliminar_window,
                            fg_color='#FFFFFF',
                            text=f'{i[3]}',
                            text_color='#000000',
                            font=('Calibri Black', 17),
                            corner_radius=0).grid(column=3, row=6, sticky='nswe',padx=2, pady=2, ipady=10)

                        ctk.CTkLabel(eliminar_window,
                            fg_color='#FFFFFF',
                            text=f'{i[4]}',
                            text_color='#000000',
                            font=('Calibri Black', 17),
                            corner_radius=0).grid(column=4, row=6, sticky='nswe',padx=2, pady=2, ipady=10)

                        ctk.CTkLabel(eliminar_window,
                            fg_color='#FFFFFF',
                            text=f'{i[5]}',
                            text_color='#000000',
                            font=('Calibri Black', 17),
                            corner_radius=0).grid(column=5, row=6, sticky='nswe',padx=2, pady=2, ipady=10)
                        
                        # Función para eliminar el elemento especificado
                        def eliminar_elemento() :
                            query = f"DELETE FROM inventario WHERE id={see_id}"
                            conn = sql.connect(
                                host='localhost',
                                user='root',
                                password='admin',
                                # port='3306',
                                database='inventario'
                            )
                            cursor = conn.cursor()
                            cursor.execute(query)
                            conn.commit()
                            messagebox.showinfo('Borrado', 'El elemento se ha borrado del inventario.')
                            cursor.close()
                            conn.close()

                        # Instrucción 3
                        ctk.CTkLabel(
                            eliminar_window,
                            text='Por favor, revise que los datos sean correctos.',
                            text_color='#FFFFFF',
                            fg_color='#E74C3C',
                            font=('Calibri Black', 21)
                        ).grid(column=3, row=7, sticky='we', pady=20)
                        
                        # Botón para eliminar el elemento
                        ctk.CTkButton(
                            eliminar_window,
                            text='ELIMINAR ELEMENTO',
                            text_color='#000000',
                            fg_color='#FFFFFF',
                            border_color='#000000',
                            border_width=1.5,
                            hover_color='#C2C3C2',
                            width=90,
                            font=('Calibri Black', 18),
                            corner_radius=7,
                            command=eliminar_elemento
                        ).grid(column=3, row=8, sticky='nswe', ipady=5, pady=2)       
                else :
                    messagebox.showerror('Error', 'No se ha encontrado ningún elemento con ese ID.')
                
                cursor.close()
                conn.close()
        # Botón para visualizar el elemento que se está por eliminar
        ctk.CTkButton(
            delete_frame,
            text='VER ELEMENTO',
            text_color='#000000',
            fg_color='#FFFFFF',
            border_color='#000000',
            border_width=1.4,
            hover_color='#C2C3C2',
            font=('Calibri Black', 18),
            command=ver_elemento
        ).grid(column=1, columnspan=2, row=3, sticky='nswe', ipady=1, pady=10)

        # Output de visualización
        id_output = ctk.CTkLabel(
            eliminar_window,
            fg_color='#FFFFFF',
            text='ID',
            text_color='#000000',
            font=('Calibri Black', 20),
            corner_radius=0)
        id_output.grid(column=0, row=5, sticky='nswe', padx=2, pady=2)

        producto_output = ctk.CTkLabel(
            eliminar_window,
            fg_color='#FFFFFF',
            text='Producto',
            text_color='#000000',
            font=('Calibri Black', 20),
            corner_radius=0)
        producto_output.grid(column=1, row=5, sticky='nswe', padx=2, pady=2)

        marca_output = ctk.CTkLabel(
            eliminar_window,
            fg_color='#FFFFFF',
            text='Marca',
            text_color='#000000',
            font=('Calibri Black', 20),
            corner_radius=0)
        marca_output.grid(column=2, row=5, sticky='nswe', padx=2, pady=2)

        descrip_output = ctk.CTkLabel(
            eliminar_window,
            fg_color='#FFFFFF',
            text='Descripción',
            text_color='#000000',
            font=('Calibri Black', 20),
            corner_radius=0)
        descrip_output.grid(column=3, row=5, sticky='nswe', padx=2, pady=2)

        precio_output = ctk.CTkLabel(
            eliminar_window,
            fg_color='#FFFFFF',
            text='Precio/unidad',
            text_color='#000000',
            font=('Calibri Black', 20),
            corner_radius=0)
        precio_output.grid(column=4, row=5, sticky='nswe', padx=2, pady=2)

        cantidad_output = ctk.CTkLabel(
            eliminar_window,
            fg_color='#FFFFFF',
            text='Cantidad',
            text_color='#000000',
            font=('Calibri Black', 20),
            corner_radius=0)
        cantidad_output.grid(column=5, row=5, sticky='nswe', padx=2, pady=2)

    inventario_lb = ctk.CTkLabel(
        window,
        text='Inventario',
        fg_color='#F2F4F4',
        text_color='#000000',
        font=('Constantia',42),
        height=50).pack(fill='x')

    frame_a = ctk.CTkFrame(window, fg_color='#F2F4F4', height= 500, corner_radius=10)
    frame_a.pack(padx=60, pady=50, fill='both')

    buscar_bt = ctk.CTkButton(
        frame_a,
        text='1)    Buscar por Producto/Marca/Descripción/ID',
        text_color='#000000',
        fg_color='#FEFFAB',
        hover_color='#E5E69E',
        border_color='#000000',
        border_width=1,
        height=35,
        font=('Constantia',18),
        anchor='w',
        command=search_window).pack(fill='x', padx=30, pady=10)

    cargar_bt = ctk.CTkButton(
        frame_a,
        text='2)    Cargar un Producto',
        text_color='#000000',
        fg_color='#FEFFAB',
        hover_color='#E5E69E',
        border_color='#000000',
        border_width=1,
        height=35,
        font=('Constantia',18),
        anchor='w',
        command=upload_window).pack(fill='x', padx=30, pady=10)

    modificar_bt = ctk.CTkButton(
        frame_a,
        text='3)    Modificar un Producto',
        text_color='#000000',
        fg_color='#FEFFAB',
        hover_color='#E5E69E',
        border_color='#000000',
        border_width=1,
        height=35,
        font=('Constantia',18),
        anchor='w',
        command=update_window).pack(fill='x', padx=30, pady=10)

    eliminar_bt = ctk.CTkButton(
        frame_a,
        text='4)    Eliminar un Producto',
        text_color='#000000',
        fg_color='#FEFFAB',
        hover_color='#E5E69E',
        border_color='#000000',
        border_width=1,
        height=35,
        font=('Constantia',18),
        anchor='w',
        command=delete_window).pack(fill='x', padx=30, pady=10)

    window.mainloop()

if __name__ == '__main__' :
    main()

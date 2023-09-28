from tkinter import *
from tkinter import ttk

#definir ventana
ventana = Tk()
#ventana.geometry("600x600")
ventana.minsize(600, 600)
ventana.title("Proyecto Tkinter")
ventana.resizable(0, 0)

def home():

    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=270,
        pady=20
    )
    home_label.grid(row=0, column=0)

    products_box.grid(row=2)

    #listar productos
    """
    for product in products:
        if len(product) == 3:
            product.append("added")
            Label(products_box, text=product[0]).grid()
            Label(products_box, text=product[1]).grid()
            Label(products_box, text=product[2]).grid()
            Label(products_box, text="----------------------").grid()
    """

    for product in products:
        if len(product) == 3:
            product.append("added")
            products_box.insert("", 0, text=product[0], values = (product[1]))
    #ocultar otras pantallas
    add_label.grid_remove()
    add_frame.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()


    return True

def add():
        #encabezado
        add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=250,
        pady=20
        )
        add_label.grid(row=0, column=0, columnspan=12)

        #campos del formulario
        add_frame.grid(row=1)
        add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
        add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
        add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        add_description_label.grid(row=3, column=0, padx=5, pady=5, sticky=NE)
        add_description_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
        add_description_entry.config(
             width=30,
             height=5,
             font=("Consolas",12),
             padx=15,
             pady=15
        )

        add_separator.grid(row=4)

        button.grid(row=5, column=1, sticky=NW)
        button.config(
             padx=15,
             pady=5,
             bg="lightgray",
             fg="black"
        )

        #ocultar otras pantallas
        home_label.grid_remove()
        products_box.grid_remove()
        info_label.grid_remove()
        data_label.grid_remove()

        return True


def info ():

    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=200,
        pady=20
    )
    info_label.grid(row=0, column=0)
    
    
    data_label.grid(row=1, column=0)

    #ocultar otras pantallas
    home_label.grid_remove()
    products_box.grid_remove()
    add_label.grid_remove()
    add_frame.grid_remove()

    return True

def add_product():
    products.append([
        name_data.get(),
        price_data.get(),
        add_description_entry.get("1.0", "end-1c")
    ])
    name_data.set("")
    price_data.set("")
    add_description_entry.delete("1.0", END)

    home()

#variables importantes
products = []
name_data = StringVar()
price_data = StringVar()

#def capos de pantalla (INICIO)
home_label = Label(ventana,text="Inicio")
#products_box = Frame(ventana, width=250)

Label(ventana).grid(row=1)
products_box = ttk.Treeview(height=12, columns=3)
products_box.grid(row=1, column=0, columnspan=3)
products_box.heading("#0", text="Producto", anchor=W)
products_box.heading("#1", text="Precio", anchor=W)

#def capos de pantalla (ADD)
add_label = Label(ventana,text="Añadir")

#campos del formulario
add_frame = Frame(ventana)
add_name_label = Label(add_frame, text="Nombre:")
add_name_entry = Entry(add_frame, textvariable=name_data)

add_price_label = Label(add_frame, text="Precio:")
add_price_entry = Entry(add_frame, textvariable=price_data)

add_description_label = Label(add_frame, text="Descripcion:")
add_description_entry = Text(add_frame)

add_separator = Label(add_frame)

button = Button(add_frame, text="Guardar", command=add_product)

#def capos de pantalla (INFO)
info_label = Label(ventana,text="Información")
data_label = Label(ventana, text="creado por wiwi a las 3am")

#cargar pantalla inicio
home()

#menu superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añandir", command=add)
menu_superior.add_command(label="Información", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)

#cargar menu
ventana.config(menu=menu_superior)

#cargar ventana
ventana.mainloop()
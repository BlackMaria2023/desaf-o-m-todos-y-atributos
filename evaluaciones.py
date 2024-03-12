from pizza import Pizza

# a. Mostrar valores de atributos de clase sin crear instancia
print("Ingredientes cárnicos:", Pizza.ingredientes_carne)
print("Ingredientes vegetales:", Pizza.ingredientes_vegetales)
print("Tipos de masa:", Pizza.tipos_masa)

# b. Validar elemento en lista sin crear instancia
print(Pizza.validar_elemento("salsa de tomate", ["salsa de tomate", "salsa bbq"]))

# c. Crear instancia y realizar pedido
mi_pizza = Pizza()
mi_pizza.realizar_pedido()

# d. Mostrar ingredientes y tipo de masa de la instancia creada
print("Ingredientes vegetales:", mi_pizza.ingrediente_vegetal1, mi_pizza.ingrediente_vegetal2)
print("Ingrediente proteico:", mi_pizza.ingrediente_proteico)
print("Tipo de masa:", mi_pizza.tipo_masa)
print("Es una pizza válida:", mi_pizza.es_valida)

# e. Mostrar si la clase Pizza es válida sin crear instancia
print("Es la clase Pizza válida:", Pizza().es_valida)  # Debería dar un error
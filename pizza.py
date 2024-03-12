class Pizza:
    # Atributos de clase
    ingredientes_carne = ["pollo", "vacuno", "carne vegetal"]
    ingredientes_vegetales = ["tomate", "aceitunas", "champiñones"]
    tipos_masa = ["tradicional", "delgada"]

    def __init__(self):
        # Atributos de instancia
        self.ingrediente_proteico = None
        self.ingrediente_vegetal1 = None
        self.ingrediente_vegetal2 = None
        self.tipo_masa = None
        self.es_valida = False

    @staticmethod
    def validar_elemento(elemento, valores_posibles):
        return elemento in valores_posibles

    def realizar_pedido(self):
        self.ingrediente_proteico = input("Ingrese el ingrediente proteico: ")
        self.ingrediente_vegetal1 = input("Ingrese el primer ingrediente vegetal: ")
        self.ingrediente_vegetal2 = input("Ingrese el segundo ingrediente vegetal: ")
        self.tipo_masa = input("Ingrese el tipo de masa (tradicional/delgada): ")

        # Validar ingreso
        self.es_valida = self.validar_pedido()

    def validar_pedido(self):
        return (
            self.validar_elemento(self.ingrediente_proteico, Pizza.ingredientes_carne)
            and self.validar_elemento(self.ingrediente_vegetal1, Pizza.ingredientes_vegetales)
            and self.validar_elemento(self.ingrediente_vegetal2, Pizza.ingredientes_vegetales)
            and self.validar_elemento(self.tipo_masa, Pizza.tipos_masa)
        )
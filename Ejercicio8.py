# Crea una clase Libro con los atributos titulo , autor y año_publicacion . Luego, crea una subclase llamada
# LibroDigital que tenga un atributo adicional

class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Año de Publicación: {self.año_publicacion}"

class LibroDigital(Libro):
    def __init__(self, titulo, autor, año_publicacion, formato):
        super().__init__(titulo, autor, año_publicacion)
        self.formato = formato
    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Año de Publicación: {self.año_publicacion}, Formato: {self.formato}"

# Ejemplo de uso:
if __name__ == "__main__":
    libro_fisico = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
    print(libro_fisico)

    libro_digital = LibroDigital("1984", "George Orwell", 1949, "PDF")
    print(libro_digital)
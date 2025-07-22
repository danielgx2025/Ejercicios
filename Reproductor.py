class FuenteAudio:
    def reproducir(self):
        # Este método debe ser implementado por cada clase que herede de FuenteAudio
        raise NotImplementedError("Cada fuente de audio debe implementar su propio método 'reproducir'.")

class mp3(FuenteAudio):
    def reproducir(self):
        return "Sonando MP3"

class CD(FuenteAudio):
    def reproducir(self):
        return "Sonando CD"

class Consola(FuenteAudio):
    def reproducir(self):
        return "Sonando Consola"

class reproductor: # Recomendación: Cambiar a 'Reproductor' (PascalCase)
    # constructor que inicializa los atributos
    def __init__(self):
        self._fuente_actual = mp3() # Atributo de la clase (Recomendación: _fuente_actual)
        
    def cambiar_fuente(self, nueva_fuente):      
        if isinstance(nueva_fuente, FuenteAudio):
            self._fuente_actual = nueva_fuente
        else:
            raise TypeError("La nueva fuente debe ser una instancia válida de FuenteAudio.")

    def reproducir(self):
        print(self._fuente_actual.reproducir())

##--------------------aqui implemento las llamadas-------------------------##


# 1. ¡Crea una instancia de tu clase reproductor!
mi_reproductor = reproductor() # Aquí creas el objeto real. Usa esta variable para interactuar.

# 2. Ahora, llama a los métodos usando esa instancia
mi_reproductor.reproducir()  # Salida: "Sonando MP3"

mi_reproductor.cambiar_fuente(CD())  
mi_reproductor.reproducir()  # Salida: "Sonando CD"

mi_reproductor.cambiar_fuente(Consola())  
mi_reproductor.reproducir()  # Salida: "Sonando Consola"
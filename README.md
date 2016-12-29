# FlappyDino-w-Pygame-
This is a project to create a video game using Pygame and Python as a programming langauges. This was done at a beginner level.

Descripción del juego “Flappy Dino”

  Flappy Dino es nuestra versión inspirada en el juego Flappy Bird. El jugador debe mantener a Dino volando para evitar que este se caiga y choque con los obstáculos que se presentan a lo largo del juego, presionando la tecla de flecha arriba. Hay tres niveles que el jugador puede pasar una vez alcance una puntuación mínima. Cuando el jugador alcance 5 puntos, la imagen de fondo se oscurece y si alcanza los 10 puntos, se pondrá aún más oscura. Una vez terminado el juego (Game Over) el usuario debe presionar el botón de quit para volver al menú principal.
  
  El desarrollo del juego se hizo en Python utilizando la librería Pygame. Gran parte del código del juego fue organizado en un total de quince funciones que se repiten dentro de otras funciones. Para la creación de las pantallas (main menu, pause, high scores, credits e instructions) se utilizó el código parecido con sus respectivos botones y las funciones de Credits e Instructions reciben como parámetro SourceScreen para saber a dónde tienen que regresar con el botón de back. Button también es otra función que se repite en todo screen que posea bontones para presionar y se ocupa de recibir un tamaño, posición, color, acción y variables extras necesarias para la función con la que opera. Hay funciones para dibujar las imágenes en posición y para escribir el texto deseado. Adicionalmente está la lista de puntuación que itera en un for loop para mostrar un máximo de las diez puntuaciones más altas. La lógica del juego y todos sus componentes se encuentran dentro de la función de gameLoop, aquí es donde se dibujan los objetos, las imágenes y se maneja el input del usuario dentro del juego. Finalmente dentro del Main loop es que se llama a un única función, gameIntro y aquí es comienza a llamarse a las funciones necesarias para poder jugar.

  El jugador podrá acceder al menú principal al comienzo del juego, antes y después de la partida y durante el juego en el modo pausa presionando la tecla escape (ESC). En el menú principal el usuario tiene varias opciones; puede comenzar un juego nuevo, ver las instrucciones y los créditos o salir del juego, así como ver las mejores puntuaciones.

  El usuario puede ver las mejores puntuaciones en el menú principal 
accediendo “High Scores”, esta opción no está disponible en el modo 
pausa.

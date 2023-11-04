# Discord.py

Un bot con múltiples funciones para ayudar a los servidores de Discord, ya sean privados o personales, puede enviar mensajes de bienvenida, despedida y proporcionar entretenimiento. Esta es solo la versión de lanzamiento, pero más adelante tendrá muchas más funciones. ¿Qué otras funciones les gustaría que tenga el bot? 🤖🎉

<p align="center">
  
<img src="https://img.shields.io/badge/version-1.0-green"/> 
<img src="https://img.shields.io/badge/author-RevayDev-blue"/> 
<img src="https://img.shields.io/badge/licencia-MIT-red"/> 
<img src="https://img.shields.io/badge/aria-Bot de discord.py-yellow"/>
  
</p>

## Instalacion
  1. Deberás clonar este repositorio. (Lo siguiente es hacerlo desde tu terminal de Git.)
   ```Bash
   git clone https://github.com/Revay3d/Discord.py.git
   ```
   ¿No tienes Git? https://git-scm.com/
  
  2. Descargar ``python``
   
   En sistemas operativos basados en Debian y Ubuntu, puedes usar el siguiente comando para descargar e instalar Python:
 ```Bash
 sudo apt update
 sudo apt install python3
 ```
  En sistemas operativos basados en Fedora, puedes usar el siguiente comando para descargar e instalar Python:
  ```Bash
 sudo dnf install python3
 ```
 En sistemas operativos basados en Arch Linux, puedes usar el siguiente comando para descargar e instalar Python:
 ```Bash
 sudo pacman -S python
 ```
 Después de ejecutar el comando apropiado para tu sistema operativo, Python debería estar instalado en tu computadora. Puedes verificar que se haya instalado correctamente ejecutando el 
 comando ``python3 --version`` en la terminal. Esto debería mostrar la versión de Python que acabas de instalar.

 otro sistema operativo o mas informacion al sitio oficial de Python: 
 https://www.python.org/downloads/
 
# Personalización
⚠ Por favor, sigue los siguientes pasos para configurar el bot y evitar cualquier error. Los pasos estarán detallados minuciosamente para aquellas personas que puedan tener dificultades para entender o asimilar la información. 😊

## Configura tu bot
+ Crea un archivo `.env` dentro de la `rais` 
  > La ruta del archivo debería ser así `.env`
  + escribe lo siguiente en el archivo `.env`:


    ```env
    Token = TU_TOKEN
    ```
  Reemplaza `TU_TOKEN` por el token de tu bot a conectar.
  
+ En el archivo `main.py` encontrarás una parte llamada variables como esta:
  ```Python
          #Variables
          class MyBot(commands.Bot):
          def __init__(self, *args, **kwargs):
    
          super().__init__(*args, **kwargs)
          self.color = 0xTU_COLOR
          self.bienvenidas = ID_CHANNEL
          self.chat = ID_CHANNEL
          self.despedidas = ID_CHANNEL

         bot = MyBot(command_prefix="+", intents=discord.Intents.all(), help_command=None)

  ```
  Tendras que remplasar las varibles segun tu necesidad `TU_COLOR` deveras usar un color hexadecimal
  > por ejemplo blanco: #ffffff en la variable `TU_COLOR` seria 0xffffff
  
  Ahora las variables `ID_CHANNEL` lo remplasarias por el id del canal que usaras para cada evento.
  
+ Fuera de la carpeta `src` está una llamada `template` dentro habrá plantillas para que tú mismo crees eventos, comandos, y más.


 3. Descarga los `pip` y modulos
  + Forma rapida de instalar los paquetes
       > Forma rapida y segura para ti y tu compu
      ```Bash
        python -m venv env
       ```
    Ruta en windows
       ```Bash
         source env/Scripts/activate
       ```
    Instalar todos los paquetes
       ```Bash
        pip install -r requirements.txt 
       ```

  + Forma lenta de instalar los paquetes   
    > No recomendable para ti y tu compu  
      
      
       
    + discord.py
       ```Bash
        pip install discord.py
       ```
       
     + interactions
       ```Bash
         pip install discord.py.interactions
       ```
       Si te da error instalalo asi
        ```Bash
       pip install python-discord.py.interactions
       ```
          
    + dotenv
      ```Bash
       pip install dotenv
      ```
      Si te da error instalalo asi
        ```Bash
       pip install python-dotenv
       ```
    + colorama
      ```Bash
      pip install colorama
      ```  
    + tabulate
      ```Bash
       pip install tabulate
       ```
        Si te da error instalalo asi
        ```Bash
       pip install python-tabulate
       ```
   Si tienes problemas al instalar los anteriores modulos investica como instalar modulos en tu version de pip.
      
## © Licencia MIT
   + Este codigo tiene una ``licencia MIT``
      

         
  

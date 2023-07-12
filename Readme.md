# Threads.Net Data Analysis

API No Oficial en Python para recopilar los threads de perfiles de usuario y analizar la data correspondientes. 

## Estructura del Proyecto

* ```threads_api.py```: Contiene el script de conexión a Threads realizando ingeniería inversa. [**Leer aviso legal**](#aviso-legal)
* ```get_user_profile_threads.py```: Permite obtener los threads de un usuario en particular. Este código puede ser usado de forma individual o como interfaz para otras implementaciones.
* ```getData.py```: Permite obtener los threads, limpiarlos, procesarlos, incluirlos en un dataframe para su exploración y exportar la data en un archivo csv.
* ```threads.ipynb```: Es una implementación que muestra el uso de la data exportada lista para trabajarla con cualquier API.
* ```ai-samples```: Notebooks con implementaciones de modelos de procesamiento de lenguaje natural para el análisis de sentimientos con la data extraída del API.
    * ```text-analytics.ipynb```: Notebook para realizar análisis de sentimientos con la data extraída de ```getData``` y procesada por ```threads.ipynb```.
    * ```mined-opinions.ipynb```: Notebook para realizar minado de opiniones con la data extraída de ```getData``` y procesada por ```threads.ipynb```.
* ```data```: Es la carpeta que almacena el archivo generado al trabajar con el archivo ```getData.py```.

### Obtener los threads de un usuario

#### get_user_profile_threads
El script realiza las siguientes acciones:

- Se conecta a una API ```threads_api.py``` y obtiene una lista de threads de un perfil de usuario utilizando la función `get_user_profile_threads` del módulo `get_user_profile_threads`.
- Procesa estos threads y limpia el texto eliminando una serie de caracteres específicos.
- Separa y recopila los datos de "me gusta" de los threads.
- Almacena la información procesada en un DataFrame de Pandas.
- Exporta el DataFrame a un archivo CSV para su posterior análisis.

#### Cómo usar

Este script se ejecuta desde la línea de comandos de la siguiente manera:

```shell
python <get_user_profile_threads>.py
```

#### Dependencias

Este script depende de los siguientes paquetes de Python:

- asyncio
- pandas

Para instalar estas dependencias, puede usar el siguiente comando:

```shell
pip install pandas asyncio
```

#### Documentación del Código

##### Importaciones

```python
from get_user_profile_threads import get_user_profile_threads
import asyncio
import pandas as pd
```

Importamos las bibliotecas y funciones necesarias para el script. Esto incluye `get_user_profile_threads` (una función personalizada que debe estar definida en un archivo en el mismo directorio), así como las bibliotecas estándar de Python `asyncio` y `pandas`.

#### Recopilación de Datos

```python
threads_data = asyncio.run(get_user_profile_threads())
```

Recoge los datos de los threads del perfil de un usuario utilizando una función asíncrona.

#### Limpieza de Datos

```python
if threads_data is not None:
    cleanThreads = []
    likes_data =[]
    chars = ['"', "'", '}', '{', 'text', '\n', ':', '\'', '\"']
```

Si `threads_data` no está vacío, el script crea dos listas vacías, `cleanThreads` y `likes_data`. La lista `chars` define los caracteres que se eliminarán del texto del hilo.

#### Procesamiento de Datos

El siguiente bloque de código procesa cada hilo en `threads_data`, limpia el texto y recoge los datos de "me gusta".

```python
for thread in threads_data:
    for char in chars:
        thread = str(thread).lstrip(' ')
        thread = str(thread).replace(char, '').lstrip('"\'')
    if ', likes' in thread:
        split_data = thread.split(', likes')
        cleanThreads.append(split_data[0])
        likes_data.append(split_data[1])
    else:
        cleanThreads.append(thread)
        likes_data.append('0')
```

#### Creación de DataFrame

```python
df = pd.DataFrame({
    'Cleaned Text': cleanThreads,
    'Likes': likes_data
})
print(df)
```

Se crea un DataFrame de Pandas con los datos de texto limpios y los "me gusta", y luego imprime este DataFrame.

#### Exportación de Datos

```python
df.to_csv('./data/data.csv', index=False,header=False)
```

Por último, el script exporta el DataFrame a un archivo CSV, sin índice ni encabezado, para su posterior análisis, en el archivo ```threads.ipynb```


### Limitaciones

Esta biblioteca actualmente tiene espacios reservados para las clases Extensions, Thread, y ThreadsUser y no realiza ninguna comprobación de errores o limitación de velocidad. Debes asegurarte de que tienes permiso para acceder a cualquier dato que solicites y manejar cualquier error devuelto por la API de threads.net.

### Aviso Legal

Este proyecto es puramente educativo. Se trata de una implementación de la versión 1.0.4 del proceso de ingeniería inversa realizado por el usuario Daniel 1 en su repositorio en [GitHub](https://github.com/Danie1/threads-api).

La base de este trabajo proviene de la documentación proporcionada en el blog [Intuitive Explanations](https://intuitiveexplanations.com/tech/messenger) sobre ingeniería inversa, descrita en el artículo "Reverse Engineering the Facebook Messenger API".

De acuerdo con el artículo, la ingeniería inversa es ética, pro-democrática y está protegida bajo la ley de Estados Unidos, pero aún es necesario ejercer integridad y responsabilidad al interactuar con cualquier sistema en línea. El comportamiento irresponsable, como enviar spam a otros usuarios, descargar datos de las personas sin su consentimiento o poner una carga indebida en la infraestructura que no estás pagando, es inapropiado independientemente de cómo se logre.

La ingeniería inversa, cuando se usa correctamente, es una forma de dar a uno mismo y a otros una mayor agencia, libertad y creatividad en línea. Sin embargo, Facebook a menudo suspende o prohíbe automáticamente a las personas que interactúan con su API de una manera que les parece sospechosa, incluso si no están haciendo nada malo. Por lo tanto, se recomienda explorar con precaución.

Para más detalles y para entender el proceso de ingeniería inversa llevado a cabo, recomendamos leer el artículo completo en [Intuitive Explanations](https://intuitiveexplanations.com/tech/messenger).

El propósito de este proyecto es ayudar a las personas a entender cómo funcionan las aplicaciones y los sistemas, y no se debe usar para violar la privacidad de otros usuarios ni abusar de las infraestructuras de sistemas ajenos. Los desarrolladores no se hacen responsables del mal uso de este código.

### Contribución

¿Encontraste una mejora que se puede implementar o te gustaría solicitar un cambio? Puedes abrir un [Issue](https://github.com/FernandaOchoa/ThreadsAPI/issues) solicitando el cambio o enviar directamente un [Pull Request](https://github.com/FernandaOchoa/ThreadsAPI/pulls) con tu cambio.

Para cualquier duda o aclaración, puedes contactarme [Fernanda Ochoa](https://github.com/FernandaOchoa):

Email: fochoa@daliaempower.com | monsh8a@gmail.com  
Twitter: [@imonsh](https://twitter.com/imonsh)  
Instagram: [@fherz8a](https://www.instagram.com/fherz8a/)

## Licencia


[MIT License](https://github.com/FernandaOchoa/ThreadsAPI/blob/main/LICENSE)

Derechos de autor (c) 2023 Fernanda Ochoa

---

Este código está sujeto a la licencia MIT que se muestra arriba. Al utilizar este código, aceptas dar crédito al autor original mencionando su nombre en el código y en cualquier documentación relacionada con el proyecto.

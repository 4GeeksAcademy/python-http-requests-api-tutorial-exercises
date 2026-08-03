<!-- hide -->
<div align="center">

# Aprende a hacer requests HTTP con Python

![Tutorial certificado por 4Geeks Academy](https://img.shields.io/badge/4Geeks%20Academy-tutorial%20certificado-2563eb) ![13 ejercicios autocorregidos con LearnPack](https://img.shields.io/badge/LearnPack-13%20ejercicios%20autocorregidos-2563eb) [![Abrir en GitHub Codespaces](https://img.shields.io/badge/Abrir%20en-Codespaces-fb5a1f)](https://codespaces.new/?repo=4GeeksAcademy/python-http-requests-api-tutorial-exercises)

![Portada del tutorial Learn how to build HTTP requests with Python, con el título sobre un fondo azul claro decorado con corchetes de código, flechas y etiquetas con nombres de estudiantes](https://raw.githubusercontent.com/4GeeksAcademy/python-http-requests-api-tutorial-exercises/master/preview.png)

</div>

*These instructions [are available in English](https://github.com/4GeeksAcademy/python-http-requests-api-tutorial-exercises/blob/HEAD/README.md) 🇺🇸*
<!-- endhide -->

Este tutorial interactivo enseña a hacer requests HTTP con Python a través de **14 ejercicios**, 13 de ellos corregidos automáticamente por **35 comprobaciones de pytest**. Empiezas apuntando un simple `requests.get()` a una URL y terminas enviando un POST con cuerpo JSON y cabecera `Content-Type`. Por el camino manejas códigos de estado, lees `response.text`, parseas `response.json()` y recorres diccionarios y listas anidadas. Duración estimada: 4 horas. Dificultad: fácil.

<!-- hide -->
## 📋 Ficha del tutorial

+ **Dificultad:** fácil, pensado como primer contacto con HTTP.
+ **Duración estimada:** 4 horas.
+ **Ejercicios:** 14 carpetas, 13 con tests automáticos y solución de referencia.
+ **Tecnologías:** Python 3, el paquete `requests`, pytest y `mock` para la corrección.
+ **Corrección:** automática, con LearnPack.
+ **Idiomas:** instrucciones en español e inglés. La versión en español incluye además un vídeo explicativo en cada uno de los 13 ejercicios de código.
<!-- endhide -->

## 🎯 ¿Qué vas a aprender?

Cada concepto se practica contra un endpoint real, no se explica en abstracto:

+ Lanzar un GET con `requests.get(url)` y leer `response.status_code`.
+ Reaccionar a códigos de estado como 200, 400, 404 y 503, y tratar cualquier otro como código desconocido.
+ Distinguir `response.text` (el cuerpo tal cual, en texto) de `response.json()` (el cuerpo convertido en diccionario o lista de Python).
+ Recorrer JSON anidado: un diccionario dentro de una lista dentro de otro diccionario, y acceder por posición.
+ Escribir funciones que *retornan* datos en lugar de imprimirlos, que es como envolverías una API en código real.
+ Enviar un POST con su payload JSON y sus cabeceras.

> 💡 El tutorial practica los dos verbos que más vas a usar, GET y POST. PUT y DELETE se mencionan como parte de la familia de métodos HTTP, pero no se practican en los ejercicios.

## 👀 ¿Qué vas a construir?

Catorce pasos. Cada uno es una carpeta dentro de `exercises/` con sus instrucciones y, a partir del `01`, un `app.py` que editas y un `test.py` que lo corrige:

+ **00 · welcome** — el único paso sin código que escribir: qué es el paquete `requests` y qué viene después.
+ **01 · creating-a-request** — cambia la variable `url` para que el GET apunte a `hello.php` e imprima un status 200.
+ **02 · random-status** — el endpoint devuelve un status distinto en cada llamada; imprime uno de cinco mensajes exactos según cuál sea. Es el ejercicio con más comprobaciones: 6.
+ **03 · response-body** — imprime `response.text` cuando el status es 200 y `Something went wrong` para cualquier otro código.
+ **04 · response-body-json** — parsea un endpoint que devuelve la hora en JSON e imprime una línea tipo `Current time: 19 hrs 45 min and 06 sec`.
+ **05 · project-name** — saca la clave `name` de un objeto JSON e imprime solo ese valor.
+ **06 · project-list** — el cuerpo es una lista JSON; imprime el nombre del **segundo** proyecto usando su índice.
+ **07 · project-list-image** — imprime la **última** imagen del **último** proyecto: una lista dentro de otra lista.
+ **08 · blog-post-author** — recorre `body["posts"][0]["author"]["name"]` para obtener el autor del primer post.
+ **09 · list-of-blog-titles** — escribe `get_titles()`, que recorre los posts y **retorna** una lista con todos los títulos.
+ **10 · get-post-tags** — escribe `get_post_tags(post_id)`, que busca el post cuyo `id` coincide y retorna su lista de tags.
+ **11 · get-attachment-by-id** — escribe `get_attachment_by_id(attachment_id)`, un doble bucle sobre los posts y sus adjuntos que retorna el título del adjunto como string.
+ **12 · post-request** — tu primer `requests.post(url)`, imprimiendo lo que responda el servidor.
+ **13 · post-request-body** — un POST con `headers={"Content-Type": "application/json"}` y un cuerpo JSON con `id` y `title`.

Del 08 al 11 todos atacan el mismo endpoint de "portafolio raro", cuya respuesta anida posts, autores, tags y adjuntos en varios niveles. Este diagrama del ejercicio 08 muestra la forma de ese cuerpo:

![Diagrama de un cuerpo de respuesta JSON anotado en rojo, que señala que el cuerpo entero es un diccionario, que la clave posts contiene una lista, que el primer post es un diccionario y que la clave tags contiene una lista de diccionarios de etiquetas](https://raw.githubusercontent.com/4GeeksAcademy/python-http-requests-api-tutorial-exercises/master/assets/traversion_json.png)

## 🎓 ¿Qué necesitas saber antes de empezar?

+ **Python básico.** Variables, condicionales, bucles `for`, listas, diccionarios y cómo declarar una función. Del 09 al 11 se da por hecho que sabes escribir una función que retorna un valor.
+ **Nada de HTTP.** Códigos de estado, cabeceras, cuerpo del request y content types se introducen desde cero.
+ **Ninguna API key, ninguna cuenta, ningún método de pago.** Todos los endpoints son APIs públicas de ejemplo que no piden autenticación.
+ **Un entorno funcionando.** Python 3 y el paquete `requests`, o un clic en GitHub Codespaces, que levanta un contenedor con Python 3.10 y todo preinstalado.

## ✅ ¿Cómo funciona la corrección automática?

Trece de las catorce carpetas traen un fichero `test.py`, y entre todas suman **35 comprobaciones de pytest**. Cada una imprime una descripción legible cuando falla, así que siempre sabes qué requisito no estás cumpliendo.

Casi todas sustituyen la red por el paquete `mock`: se parchean `requests.get` y `requests.post`, y tu código recibe una respuesta falsa fija en lugar de la del servidor real. Esto tiene dos consecuencias que conviene tener presentes:

+ La corrección es determinista. El ejercicio 02 puede probar sus cinco ramas de status en una sola ejecución aunque el endpoint real devuelva un código al azar.
+ Los datos falsos no son los datos reales. El ejercicio 05 se corrige contra `Sample Project`, un nombre que no aparece ni en el JSON de ejemplo de su propio enunciado ni en lo que responde el endpoint real, así que copiar lo que leas no pasa la comprobación.

La excepción es el ejercicio 12: una de sus dos comprobaciones deja pasar el POST real y revisa el texto que responde el servidor, así que trabaja con conexión a internet.

Cada uno de los 13 ejercicios corregidos trae además una solución de referencia que LearnPack puede mostrarte, y los tests revisan tres cosas distintas según el ejercicio: la URL exacta que le pasas a `requests`, el texto exacto que imprimes en consola, o el valor que retorna tu función.

## 💡 ¿Qué errores debes evitar?

+ **Imprimir cuando el test espera un return.** En los ejercicios 09, 10 y 11 el corrector importa tu función y mira lo que retorna. Un `print()` dentro de la función le resulta invisible; lo que cuenta es el `return`.
+ **Dejar salida de más.** Varias comprobaciones comparan la salida *entera* de consola con `==`, no con "contiene". Un `print()` de depuración olvidado, o imprimir el status antes del mensaje, tumba una respuesta por lo demás correcta.
+ **Llamar dos veces al endpoint.** Algunas comprobaciones usan `assert_called_once_with(url)`, así que un request extra, o pasar la URL como argumento con nombre en lugar de como primer argumento posicional, falla.
+ **Copiar valores del navegador.** Las respuestas corregidas son inventadas. El ejercicio 06 espera el segundo proyecto de la lista *simulada* y el 11 espera el título `Training Certificate`; ninguno se adivina abriendo el endpoint real.
+ **Serializar el cuerpo del POST a mano.** En el ejercicio 13 la comprobación lee el argumento `json` de `requests.post`, así que `requests.post(url, json=payload, headers=...)` pasa y `data=json.dumps(payload)` no. La cabecera `Content-Type: application/json` se verifica aparte.
+ **Traducir los textos esperados.** Los cinco mensajes del ejercicio 02 se comparan literalmente en inglés, aunque estés siguiendo las instrucciones en español.

## ❓ Preguntas frecuentes

### ¿Necesito saber HTTP antes de empezar este tutorial?

No. El tutorial parte de cero en HTTP e introduce métodos, códigos de estado, cuerpos de respuesta y cabeceras según hacen falta. Lo que sí necesitas es soltura con listas, diccionarios, bucles y funciones de Python, porque la mayoría de los ejercicios consisten en moverse por un JSON ya parseado.

### ¿Cuál es la diferencia entre response.text y response.json()?

`response.text` te da el cuerpo tal cual, como string de Python, que es lo que imprime el ejercicio 03. `response.json()` parsea ese mismo cuerpo y te devuelve un diccionario o una lista que puedes recorrer, que es de lo que dependen todos los ejercicios a partir del 04. Llamar a `.json()` sobre un cuerpo que no es JSON válido lanza un error.

### ¿Cómo envío un cuerpo JSON con el paquete requests?

Pasa tu diccionario en el argumento `json` y deja que `requests` lo serialice: `requests.post(url, json={"id": 2323, "title": "Very big project"}, headers={"Content-Type": "application/json"})`. Es exactamente lo que corrige el ejercicio 13. El argumento `json` ya fija el content type por su cuenta, pero el ejercicio te pide declararlo de forma explícita para que aprendas dónde viven las cabeceras.

### ¿Por qué falla el ejercicio si la salida parece correcta?

Nueve de cada diez veces es un tema de espacios o de salida sobrante. Las comprobaciones comparan la salida completa carácter a carácter, así que un mensaje de más, una mayúscula distinta o un espacio que falte en `Current time: 19 hrs 45 min and 06 sec` hacen que falle. Lee la descripción del test en la terminal: te dice el string exacto que espera.

### ¿Los tests necesitan conexión a internet?

Casi todos funcionan sin conexión, porque `requests.get` y `requests.post` están parcheados con mocks que devuelven datos fijos. La excepción es el ejercicio 12, donde una comprobación hace el POST real y lee la respuesta del servidor, así que cuenta con estar online.

### ¿Cuánto se tarda y cuánto cuesta?

El paquete está estimado en 4 horas para los 14 ejercicios, y es realista si escribes el código en lugar de pegar las soluciones. Ejecutarlo no cuesta nada: el repositorio es público en GitHub y todos los endpoints son APIs de ejemplo gratuitas. Ten en cuenta que el repositorio no incluye fichero LICENSE, así que no está publicado bajo una licencia de código abierto; las soluciones que escribas son tuyas.

<!-- hide -->
## 📚 Tutoriales relacionados

Si todavía estás construyendo tu base de Python, o quieres seguir después de este:

+ [Aprende Python Interactivamente (principiante)](https://4geeks.com/es/interactive-exercise/python-beginner-exercises-es)
+ [Aprende las funciones de Python Interactivamente](https://4geeks.com/es/interactive-exercise/python-function-exercises-es)
+ [Aprende listas y bucles de Python Interactivamente](https://4geeks.com/es/interactive-exercise/python-loops-lists-exercises-es)
+ [Domina Python Practicando](https://4geeks.com/es/interactive-exercise/master-python-exercises-es)
+ [Aprende Programación Orientada a Objetos con Python](https://4geeks.com/es/interactive-exercise/aprende-programacion-orientada-a-objetos-con-python)
+ [Aprende las mejores prácticas de Python](https://4geeks.com/es/interactive-exercise/aprende-las-mejores-practicas-de-python)

## 🚀 Cómo empezar

Lo más rápido es [abrir el repositorio en GitHub Codespaces](https://codespaces.new/?repo=4GeeksAcademy/python-http-requests-api-tutorial-exercises), que levanta un contenedor con Python 3.10, Node 22, LearnPack y todas las dependencias ya instaladas. [Gitpod](https://gitpod.io#https://github.com/4GeeksAcademy/python-http-requests-api-tutorial-exercises) también funciona.

Cuando se abra VSCode, LearnPack debería arrancar solo. Si no lo hace, ejecuta esto en la terminal:

```bash
learnpack start
```

## 💻 Instalación local

1. Instala [Python 3](https://www.python.org/downloads/), Node.js 14 o superior y [LearnPack](https://learnpack.co/):

    ```bash
    npm i @learnpack/learnpack -g
    learnpack plugins:install @learnpack/python
    ```

2. Clona el repositorio e instala las dependencias de Python que necesitan los tests:

    ```bash
    pip3 install pytest==6.2.5 pytest-testdox mock requests toml
    ```

3. Desde la misma carpeta donde está [learn.json](https://github.com/4GeeksAcademy/python-http-requests-api-tutorial-exercises/blob/HEAD/learn.json), arranca el tutorial:

    ```bash
    learnpack start
    ```

## 📝 Cómo están organizados los ejercicios

Cada ejercicio vive en su propia carpeta dentro de `exercises/` y contiene hasta cinco ficheros:

+ **README.md** y **README.es.md** — las instrucciones, en inglés y en español.
+ **app.py** — el fichero que editas y el que ejecuta Python.
+ **test.py** — el script de corrección. No hace falta que lo abras, pero leerlo es la forma más rápida de entender por qué falla una comprobación.
+ **solution.hide.py** — una solución de referencia, oculta por LearnPack hasta que la pides.

> 💡 Los tests son estrictos a propósito. Toma una comprobación fallida como una pista sobre el texto exacto o el valor de retorno que se te pide, no como un veredicto sobre tu código.

## 🤝 Colaboradores

Creado por [Alejandro Sánchez](https://github.com/alesanchezr) (código, tests, tutorial, documentación), [Paolo (plucodev)](https://github.com/plucodev) (reporte de bugs, código, traducción) y [otros colaboradores](https://github.com/4GeeksAcademy/python-http-requests-api-tutorial-exercises/graphs/contributors).

Este proyecto sigue la especificación [all-contributors](https://github.com/kentcdodds/all-contributors) y toda contribución es bienvenida. ¿Encontraste una errata, un endpoint caído o un test confuso? [Abre un issue](https://github.com/learnpack/learnpack/issues/new).

Este y muchos otros tutoriales interactivos se construyen en [4Geeks Academy](https://4geeksacademy.com/es/coding-bootcamps/desarrollador-full-stack).
<!-- endhide -->

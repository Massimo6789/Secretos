from flask import Flask
import random
app = Flask(__name__)

datos = ["La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos",
"Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.",

"El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna",
"Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo",

"Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo",

"Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos",
"Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan una enorme cantidad de información sobre nosotros, que luego puede utilizarse para manipular nuestros pensamientos y comportamientos",

"Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas"]

secretos = ["¿Qué se encuentra una vez en un minuto, dos veces en un momento pero ninguno en cien años? Respuesta: la letra m",
"Redondo, redondo, barril sin fondo. ¿Qué es? Respuesta: un anillo",
"¿Qué es lo que sopla sin boca y vuela sin alas? Respuesta: el viento"]

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1> <a href="/dato_random"> Ver Dato Random </a>'
@app.route("/dato_random")
def dato():
    return f'<h1>{random.choice(datos)}</h1> <a href="/"> Ir A Pagina Principal </a>'
@app.route("/Secreto_random")
def secreto():
    return f'<h1>{random.choice(secretos)}</h1><img src="https://static.guiainfantil.com/media/29838/reno-adivinanza.jpg" alt="Navidad 1"> <a href="/dato_random"> Ir A Pagina De Datos </a>'
app.run(debug=True)
print("hello world")

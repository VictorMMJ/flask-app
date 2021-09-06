from __future__ import division

import re
import sys
import aiml
import os
from datetime import datetime
import time

BRAIN_FILE = "brain.brn"

fechaSesion = datetime.now().strftime("%d%m%Y%H%M%S")
sessionFileName = "historial_dialogo_" + fechaSesion + ".txt"

kernel = aiml.Kernel()
if os.path.isfile(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    kernel.loadBrain(BRAIN_FILE)
else:
    print("Parsing aiml files")
    kernel.bootstrap(learnFiles="std-startup.xml", commands="load aiml b")
    print("Saving brain file: " + BRAIN_FILE)
    kernel.saveBrain(BRAIN_FILE)  

#Se establecen las propiedades del bot
kernel.setBotPredicate("name","Mari")
kernel.setBotPredicate("age","40")
kernel.setBotPredicate("gender","Mujer")
kernel.setBotPredicate("birth_place","Puebla")

#Se establecen constantes dentro que el bot puede utilizar
#Se establecen los predicados en la sessionId=1
kernel.setPredicate("patient_name", "Tere",1)
kernel.setPredicate("last_job","Ama de casa",1)
kernel.setPredicate("fam1_name", "Maribel",1)
kernel.setPredicate("fam1_par", "hija",1)
kernel.setPredicate("fam1_age", "48",1)
kernel.setPredicate("fam2_name", "Enrique",1)
kernel.setPredicate("fam2_par", "hijo",1)
kernel.setPredicate("fam2_age", "54",1)
kernel.setPredicate("fam2_name", "Carlitos",1)
kernel.setPredicate("fam2_par", "nieto",1)
kernel.setPredicate("fam2_age", "12",1)

#Se establecen los predicados en la sessionId=2
kernel.setPredicate("nombre completo_paciente", "Amador de Jesús Cameda",2)
kernel.setPredicate("primer_nombre_paciente", "Amador", 2)
kernel.setPredicate("nombre_preferido_paciente", "Cameda", 2)
kernel.setPredicate("sexo_paciente", "Masculino", 2)
kernel.setPredicate("fecha_nacimiento_paciente","30 de abril de 1940", 2)
kernel.setPredicate("lugar_nacimiento_paciente", "Izucar de Matamoros", 2)
kernel.setPredicate("lugar_residencia_paciente", "Cuautla", 2)
kernel.setPredicate("nivel_estudios_paciente", "primaria", 2)
kernel.setPredicate("ultima_ocupacion_paciente", "militar", 2)
kernel.setPredicate("religion_paciente", "catolica", 2)
kernel.setPredicate("nombre_cuidador_paciente", "Patricia", 2)
kernel.setPredicate("parentesco_cuidador_paciente", "hija", 2)
kernel.setPredicate("fam1_name", "Patricia",2)
kernel.setPredicate("fam1_par", "hija",2)
kernel.setPredicate("fam1_age", "58",2)
kernel.setPredicate("fam2_name", "Antonio",2)
kernel.setPredicate("fam2_par", "hijo",2)
kernel.setPredicate("fam2_age", "49",2)
kernel.setPredicate("fam2_name", "Fernandita",2)
kernel.setPredicate("fam2_par", "nieta",2)
kernel.setPredicate("fam2_age", "17",2)
kernel.setPredicate("fam2_name", "Marquitos",2)
kernel.setPredicate("fam2_par", "nieto",2)
kernel.setPredicate("fam2_age", "25",2)
kernel.setPredicate("habito1", "tomar cafe por las mañanas", 2)
kernel.setPredicate("habito2", "bolear sus zapatos todos los dias", 2)
kernel.setPredicate("actividad_hogar1", "barrer el patio", 2)
kernel.setPredicate("habilidad1", "hacer figuas de madera", 2)
kernel.setPredicate("habilidad2", "cantar", 2)
kernel.setPredicate("pasatiempo1", "leer la biblia", 2)
kernel.setPredicate("pasatiempo2", "salir a caminar", 2)
kernel.setPredicate("comida1", "caldo de pollo", 2)
kernel.setPredicate("comida2", "mole", 2)
kernel.setPredicate("comida3", "cecina", 2)
kernel.setPredicate("bebida1", "agua de naranja", 2)
kernel.setPredicate("bebida2", "cafe", 2)
kernel.setPredicate("bebida3",'refresco de piña', 2)
kernel.setPredicate("genero1", "boleros", 2)
kernel.setPredicate("genero2", "norteñas", 2)
kernel.setPredicate("cantante1", "Javier Solis", 2)
kernel.setPredicate("cantante2", "Antonio Aguilar", 2)
kernel.setPredicate("cantante3", "Joan Sebastian", 2)
kernel.setPredicate("cancion1", "Esclavo y amo de Javier Solis", 2)
kernel.setPredicate("cancion2", "100 años de Pedro Infante",2)
kernel.setPredicate("programa_pelicula", "ninguno", 2)
kernel.setPredicate("actor1", "Pedro Infante", 2)
kernel.setPredicate("actor2", "Joaquin Bernabé", 2)
kernel.setPredicate("deporte1", "Beisball", 2)
kernel.setPredicate("deporte2", "Basketball",2)
kernel.setPredicate("deporte3", "Corridas de toros", 2)
kernel.setPredicate("equipo1", "Los pericos de Puebla", 2)
kernel.setPredicate("equipo2", "Los tomateros de Culiacan", 2)
kernel.setPredicate("festividad", "El día del padre", 2)
kernel.setPredicate("festividad", "Navidad", 2)
kernel.setPredicate("festividad", "El cumpleaños de mi hija", 2)
kernel.setPredicate("lugar1", "Acapulco", 2)
kernel.setPredicate("lugar2", "Oaxaca", 2)
kernel.setPredicate("lugar3", "Huajuapan", 2)


def genera_respuesta(transcript):
    transcript = transcript.replace('á','a')
    transcript = transcript.replace('é','e')
    transcript = transcript.replace('í','i')
    transcript = transcript.replace('ó','o')
    transcript = transcript.replace('ú','u')
    respuesta_aiml = kernel.respond(transcript, 2)
    #print("Mari:",respuesta_aiml)
    return respuesta_aiml


def main():
    while True:
        utterance = input('>:')
        respuesta_sistema = genera_respuesta(utterance)
        print(respuesta_sistema)
        if re.search(r"\b(adios|hasta luego|nos vemos|bye)\b", utterance, re.I):
            break

if __name__ == "__main__":
    main()
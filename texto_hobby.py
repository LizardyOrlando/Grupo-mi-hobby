frase1= "Diversion: Lo Que Mas me Gusta de este pasatiempo es pasar el dia afuera con o sin gente mi nivel de habilidad es avanzado porque lo practico desde muy joven. Este hobby es accesible para todos los generos sin distincion alguna."
frase2 = "234"
#divide la palabra clave 
primera_llave = frase1.split(":")

#frase1 sin espacios al principio y al final
frase_sin_espacios = frase1.strip()

#separa la frase en linea
frase_en_lineas = frase1.splitlines()

#cambia la palabra que se elige por otra
replace_frase = frase1.replace("Diversion", "Asombroso")

#frase minuscula
frase_minus = frase1.lower()

#frase mayuscula
frase_mayus = frase1.upper()

#tira true o false dependiendo la frase de inicio
empieza_con = frase1.startswith("Diversion")

#tira true o false dependiendo la frase al final
termina_con = frase1.endswith("a.")

#tira true si todos los caracteres son letras del alfabeto
is_text = frase2.isalpha()

#tira true si todos los caracteres son numeros 
is_digit= frase2.isdigit()

primer = frase1.split()

print(primera_llave[8])


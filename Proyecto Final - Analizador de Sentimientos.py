import openai  

class ApiKey:
    def __init__(self):
        self.client = openai.OpenAI(api_key="esta api_key es privada") #en esta clase dejo el apikey, no lo pude subir al github por una cuestion de que cada API es privada y no se puede compartir.
    
class Chatbot(ApiKey):
        def __init__(self, texto: str):
             super().__init__() #heredo el apikey
             if texto.isnumeric() == True:
                  raise TypeError("El texto ingresado es un numero, intenta de nuevo") #si el texto es de valor numerico, se invalida la ejecuccion, de lo contrario se valida el texto 
             else:
                  self.texto = texto
        def output(self):
            chat_completion = self.client.chat.completions.create( #uso el apikey en self.client
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": f"Analiza el sentimiento o emocion del siguiente texto: {self.texto}, solamente imprime el sentimiento en una sola palabra, toma de ejemplo, si alguien dice estoy extremadamente contento imprime positivo"}],  #este es mi prompt
            temperature=1,
            max_tokens=2048,  
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
            self.sentimiento = chat_completion.choices[0].message.content #guardo el output de chatgpt en self.sentimiento y lo retorno
            return self.sentimiento

class AnalizadorDeSentimientos:
    def __init__(self, sentimiento): 
        self.sentimiento = sentimiento
    def output(self):
        print(f"El sentimiento del texto es: {self.sentimiento.lower()}") #imprimo el output


while True:
    texto = Chatbot(input("Ingresa tu texto a analizar, solo letras y espacios: "))
    sentimiento = texto.output()  
    analizador = AnalizadorDeSentimientos(sentimiento)  
    analizador.output()



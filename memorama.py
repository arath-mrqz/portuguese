import random

class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

class FlashcardDeck:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def shuffle_cards(self):
        random.shuffle(self.cards)

    def study(self,language):
        errors = 0
        missed_words = []
        for card in self.cards:
            if language == 1:
                question_prompt = f"\nPortuguese: {card.question}\nSpanish: "
            else:
                question_prompt = f"\nSpanish: {card.question}\nPortuguese: "
                
            answer = input(question_prompt)
            
            if answer == card.answer:
                
                print('Correct\n')
            else:
                print(f'Wrong, the word is: {card.answer}')
                errors+=1
                missed_words.append(card.question)       
            
        return missed_words, errors

            

def main():
    portuguese_words = [
    "como", "eu", "seu", "que", "ele", "foi", "para", "em", "são", "com",
    "eles", "ser", "em", "umo", "tem", "este", "a partir de", "por", "quente", "palavra",
    "mas", "oque", "alguns", "é", "ele", "você", "ou", "teve", "o", "de", "a",
    "e", "aquele", "em", "nós", "lata", "fora", "outro", "foram", "que", "fazer",
    "seu", "tempo", "se", "vontade", "como", "disse", "uma", "cada", "dizer", "faz",
    "conjunto", "três", "quer", "ar", "bem", "também", "jogar", "pequeno", "fim", "colocar",
    "casa", "ler", "mão", "port", "grande", "somar", "adicionar", "mesmo", "terra", "aqui",
    
    "necessário", "grande", "alto", "tais", "seguir", "atuar", "porque", "perguntar", "laranja",
    "trocar", "fui", "luz", "tipo", "pai", "precisar", "casa", "imagem", "tentar", "nós",
    "novamente", "animais", "ponto", "mãe", "mundo", "perto", "construir", "auto", "terra", "avô",
    "qualquer", "novo", "trabalho", "parte", "tomar", "obter", "lugar", "feito", "viver", "onde",
    "depois", "voltar", "pouco", "apenas", "rodada", "homem", "ano", "veio", "exposição", "cada",
    "bom", "me", "dar", "nossa", "debaixo", "nome", "muito", "através", "justo", "forma",
    "frase", "grande", "supor", "dizer", "ajudar", "baixo", "linha", "diferir", "turno", "causa",
    "muito", "significar", "antes", "mudança", "direito", "menino", "velho", "também", "mesmo", "ela",
    "tudo", "lá", "quando", "arriba", "usar", "seu", "maneira", "sobre", "muitos", "depois",
    "eles", "escrever", "faria", "como", "assim", "estes", "seu", "longo", "fazer", "coisa",
    "veja", "ele", "dois", "tem", "olhar", "mais", "dia", "poderia", "ir", "vir",
    "fez", "número", "som", "não", "mais", "pessoa", "meu", "sobre", "sei", "água",
    "que", "chamada", "primeiro", "que", "pode", "baixo", "lado", "sido", "agora", "encontrar"]
    
    spanish_words = [
    "cómo", "yo", "su", "que", "él", "fue", "para", "en", "son", "con",
    "ellos", "ser", "en", "uno", "tiene", "este", "a partir de", "por", "caliente", "palabra",
    "pero", "qué", "algunos", "es", "él", "usted", "o", "tuvo", "o", "de", "a",
    "y", "aquel", "en", "nosotros", "lata", "fuera", "otro", "fueron", "que", "hacer",
    "su", "tiempo", "si", "voluntad", "cómo", "dijo", "una", "cada", "decir", "hace",
    "conjunto", "tres", "quiere", "aire", "bien", "también", "jugar", "pequeño", "fin", "poner",
    "casa", "leer", "mano", "puerto", "grande", "sumar", "añadir", "mismo", "tierra", "aquí",
    "necesario", "grande", "alto", "tal", "seguir", "actuar", "porque", "preguntar", "naranja",
    "cambiar", "fui", "luz", "tipo", "padre", "necesitar", "casa", "imagen", "intentar", "nosotros",
    "nuevamente", "animales", "punto", "madre", "mundo", "cerca", "construir", "auto", "tierra", "abuelo",
    "cualquier", "nuevo", "trabajo", "parte", "tomar", "obtener", "lugar", "hecho", "vivir", "donde",
    "después", "volver", "poco", "apenas", "redonda", "hombre", "año", "vino", "exposición", "cada",
    "bueno", "me", "dar", "nuestro", "debajo", "nombre", "mucho", "a través de", "justo", "forma",
    "frase", "gran", "suponer", "decir", "ayudar", "bajo", "línea", "diferir", "turno", "causa",
    "mucho", "significar", "antes", "cambio", "derecho", "niño", "viejo", "también", "mismo", "ella",
    "todo", "allí", "cuando", "arriba", "usar", "su", "manera", "sobre", "muchos", "después",
    "ellos", "escribir", "haría", "como", "así", "estos", "su", "largo", "hacer", "cosa",
    "ver", "él", "dos", "tiene", "mirar", "más", "día", "podría", "ir", "venir",
    "hizo", "número", "sonido", "no", "más", "persona", "mi", "sobre", "sé", "agua",
    "que", "llamada", "primero", "que", "puede", "bajo", "lado", "sido", "ahora", "encontrar"]
    
    # portuguese_words_part1 = portuguese_words[:50]
    # portuguese_words_part2 = portuguese_words[50:100]
    # portuguese_words_part3 = portuguese_words[100:]
    
    # spanish_words_part1 = spanish_words[:50]
    # spanish_words_part2 = spanish_words[50:100]
    # spanish_words_part3 = spanish_words[100:]
    
    level = int(input("which part of words do you want to practice? 1, 2 or 3\n"))
    
    if level ==1:
        spanish_words = spanish_words[:50]
        portuguese_words = portuguese_words[:50]
    elif level == 2:
        spanish_words = spanish_words[50:100]
        portuguese_words = portuguese_words[50:100]
    elif level == 3:
        spanish_words = spanish_words[100:]
        portuguese_words = portuguese_words[100:]
        
        

    language = int(input("Which you want to write down?\n[1] Spanish\n[2] Portuguese\n"))
    
    if language == 1:
        cards = dict(zip(portuguese_words,spanish_words))
    else:
        cards = dict(zip(spanish_words,portuguese_words))

    

    # Create a deck of flashcards
    deck = FlashcardDeck()

    # Add some sample cards
    
    if language == 1:
        for portuguese, spanish in cards.items():
            deck.add_card(Flashcard(portuguese,spanish))
    else:
        for spanish, portuguese in cards.items():
            deck.add_card(Flashcard(spanish,portuguese))

    # Shuffle the cards for a random order
    deck.shuffle_cards()

    # Start studying
    
    print("Welcome to the Flashcards Program!")
    
    input("Press Enter to begin studying...")

    # Study the flashcards
    missed_words, errors = deck.study(language)
    
    print(f'You missed {errors} words\n')
    for missed_word in missed_words:
        print(f'{missed_word} : {cards[missed_word]}')
    

if __name__ == "__main__":
    main()

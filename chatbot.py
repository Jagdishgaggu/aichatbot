from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
#import speech_recognition as sr
#r = sr.Recognizer()



chatbot = ChatBot(
    "Terminal",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        #'chatterbot.logic.MathematicalEvaluation',
        #'chatterbot.logic.TimeLogicAdapter',
        
    ]
    )

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(chatbot)
#trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(conversation)

"""trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
)"""

print('Type something to begin...')

# The following loop will execute each time the user enters input
while True:
    try:

        bot_response = chatbot.get_response(input('Ask:'))
        print(bot_response)
        """with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
            try:
                #user_input = input('Ask:')
                
                # for testing purposes, we're just using the default API key
                # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                # instead of `r.recognize_google(audio)`
                print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
                bot_response = chatbot.get_response(r.recognize_google(audio))
                print(bot_response)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))"""
                 
    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
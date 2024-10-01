class Adaptee: # vanha luokka jota halutaan vielä käyttää
    def metodi_B(self):
        return "!oroM"

class Adapter: # adapteri-luokka, jolla sovitetaan vanha luokka uuteen järjestelmään
    def __init__(self, adaptee:Adaptee):
        self.adaptee = adaptee
    def metodi_A(self):
        return f"{self.adaptee.metodi_B()[::-1]}"

class Client: # uusi luokka, jonka pitää päästä käyttämään vanhaa palvelua
    def __init__(self):
        adaptee = Adaptee() # olio vanhantyylisestä luokasta
        adapter = Adapter(adaptee) # olio Adapteri-luokasta
        print(adapter.metodi_A()) # metodikutsu adapterin kautta

client = Client() # asiakasluokasta olio
# Testing
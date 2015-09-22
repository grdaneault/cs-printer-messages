from CurrentTutorProvider import CurrentTutorProvider
from Line import Line
from StaticMessageProvider import StaticMessageProvider

providers = [CurrentTutorProvider(), StaticMessageProvider("Welcome to the", "Tutoring Center!", center=True)]

last_sent = ''
seconds = 0
while True:
    for provider in providers:
        screen = provider.screen()
        screen.show(None)

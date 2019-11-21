from kivy.uix.screenmanager import Screen

class sc_menu(Screen):
        #function to go on the boatplacer screen
    def goToBoatPlacer(sender,nbr):
        global GAME_TYPE
        GAME_TYPE = nbr
        sender.parent.current="sc_BoatPlacer"

    def goTo_score(sender):
        sender.parent.current="sc_score"
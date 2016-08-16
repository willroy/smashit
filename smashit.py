#!/usr/bin/env python3

import random

class SmashItEngine:
    def __init__(self, ui):
        self.ui = ui
        self.actions = ["bopit", "smashit", "twizzleit"]
        self.sequence = []

    def start(self):
        self.ui.say("start")

    def add_action(self):
        self.sequence.append(random.choice(self.actions))

    def take_turn(self, response_time):
        """This method should sequence the things required during the turn. e.g.
        1. Add an action to the sequence
        2. For each action in the sequence:
            a. tell the UI to let the user know which action to do.
            b. The UI should return a success or fail response from the "say" method.
            c. There should be a timeout on the response, after which we assume the user failed
            and we abort the loop with a fail. THIS IS THE HARD BIT!
        3. If we failed, tell the ui that we failed, and end the game.
        4. If we succeeded, take_turn again.
        (5. Future requirement level up)
        """

class SmashItTextUI:
    def __init__(self):
        self.responses = {
            "start": "Starting the Game in 3 seconds!",
            "bopit": "Bop It! (press B)",
            "smashit": "Smash It! (press S)",
            "twizzleit": "Twizzle It! (press T)"
        }

    def say(self):
        pass

    def fail(self):
        pass



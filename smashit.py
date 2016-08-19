#!/usr/bin/env python3

import random
import sys
import select

class SmashItEngine:
    def __init__(self, ui, choice_function=random.choice):
        self.ui = ui
        self.choice_function = choice_function
        self.actions = ["bopit", "smashit", "twizzleit"]

    def start(self):
        response_time = 5
        self.ui.start()
        while True:
            response = self.take_turn(response_time)
            if response == True:
                self.ui.correct()
            elif response == False:
                self.ui.fail()
                break
            else:
                self.ui.timedout()
                break
            
            

    def next_action(self):
        return self.choice_function(self.actions)

    def take_turn(self, response_time):
        action = self.next_action()
        return self.ui.get_response_to(action, response_time)
        
        """
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
        self.action_expected = {
            "bopit": "B",
            "smashit": "S",
            "twizzleit": "T"
        }

    def get_response_to(self, action, response_time):
        print(action)
        print(self.responses[action])

        user_response = self.get_response_from_user(response_time)
        if user_response == None:
            return None

        expected_response = self.action_expected[action]
        return user_response.strip() == expected_response

    def get_response_from_user(self, response_time):
        i, o, e = select.select([sys.stdin], [], [], response_time)
        return i[0].readline() if i else None

    def fail(self):
        print("You Lose!")
        
    def correct(self):
        print("Correct!!")
        
    def timedout(self):
        print("Too Slow!")
        
    def start(self):
        print("Starting Game...")

ui = SmashItTextUI()
smashitengine = SmashItEngine(ui)
smashitengine.start()



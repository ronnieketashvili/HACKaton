import Inputs
import main
import random


def question_1():
    print("Oh.. There some trash over there, what are you going to do with it?\n"
          "A: Pick it up\n"
          "B: Leave it there\n")

    answer = Inputs.valid_answer()

    if answer == 'a':
        print("Nice, Plastic waste kills up to one million seabirds, 100,000 sea mammals, "
              "marine turtles and countless fish each year, nice of you to save some turtles.")
    else:
        print("Uh, more than 8 million tons of plastic enter the oceans each year- "
              "equal to dumping a garbage truck of plastic every minute, "
              "and you couldn't be bothered to pick up one bag, not cool.")
        main.score -= 5


def question_2():
    print("Looks like you got back later than expected from your morning run. "
          "You don't have too much time to drink coffee, but at least you can"
          " choose the cup you will drink it from.\n"
          "A: Cardboard cup\n"
          "B: Glass cup\n")

    answer = Inputs.valid_answer()

    if answer == 'a':
        print("Cardboard is made from wood pulp and cellulose fibers, "
              "which means that in order to make new cardboard- "
              "it is necessary to cut down new trees.. you think your coffee is that important?.")
        main.score -= 5

    else:
        print("Since cardboard is biodegradable, "
              "it produces Methane(the greenhouse gas) as it breaks down, maybe we'll get to live a few more "
              "years until the sun collapses on us, thanks to your coffee.")

def question_3():
    random_answer = ["About 11 million cars were designed to cheat air pollution tests, did you cheat yours?",
                     "91% of the World’s Population Are Breathing in Polluted Air Every Day, happy to Happy to contribute?",
                     "Air pollution makes climate change worse, not that its news to you, but have fun in your car"]

    print("OK now you really don't have time, How are you going to get to work? "
          "A: Your private car\n"
          "B: Your bike\n")
    answer = Inputs.valid_answer()

    if answer == 'a':
        print(random.choice(random_answer))

    else:
        print("Diesel exhaust causes cancer, thanks for not using it.")

def question_4():
    pass
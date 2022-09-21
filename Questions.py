import Inputs
import main


def question_1():
    print("Oh.. There some trash over there, what are you going to do with it?\n"
          "A: Pick it up\n"
          "B: Leave it there\n")

    answer = Inputs.valid_answer()

    if answer == 'a':
        main.score += 5


def question_2():
    print("Looks like you got back later than expected from your morning run. "
          "You don't have too much time to drink coffee, but at least you can"
          " choose the cup you will drink it from.\n"
          "A: Cardboard cup\n"
          "B: Glass cup\n")

    answer = Inputs.valid_answer()

    if answer == 'a':
        main.score += 5

#car
def question_3():
    print("")

#air co
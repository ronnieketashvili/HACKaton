import Inputs
import main
import random


def question_1():
    # print("Oh.. There some trash over there, what are you going to do with it?\n"
    #       "A: Pick it up\n"
    #       "B: Leave it there\n")
    #
    # answer = Inputs.valid_answer()
    #
    # if answer == 'a':
    #     print("Nice, Plastic waste kills up to one million seabirds, 100,000 sea mammals, "
    #           "marine turtles and countless fish each year, nice of you to save some turtles.")
    # else:
    #     print("Uh, more than 8 million tons of plastic enter the oceans each year- "
    #           "equal to dumping a garbage truck of plastic every minute, "
    #           "and you couldn't be bothered to pick up one bag, not cool.")
    #     main.score -= 5

    question = "Oh.. There some trash over there, what are you going to do with it?\n" \
               "A: Pick it up\n" \
               "B: Leave it there\n"

    answer_a = "Nice, Plastic waste kills up to one million seabirds, 100,000 sea mammals, \n" \
               "marine turtles and countless fish each year, nice of you to save some turtles."

    answer_b = "Uh, more than 8 million tons of plastic enter the oceans each year- \n" \
               "equal to dumping a garbage truck of plastic every minute, \n" \
               "and you couldn't be bothered to pick up one bag, not cool."

    return (question, answer_a, answer_b)


def question_2():
    # print("Looks like you got back later than expected from your morning run. "
    #       "You don't have too much time to drink coffee, but at least you can"
    #       " choose the cup you will drink it from.\n"
    #       "A: Cardboard cup\n"
    #       "B: Glass cup\n")
    #
    # answer = Inputs.valid_answer()
    #
    # if answer == 'a':
    #     print("Cardboard is made from wood pulp and cellulose fibers, "
    #           "which means that in order to make new cardboard- "
    #           "it is necessary to cut down new trees.. you think your coffee is that important?.")
    #     main.score -= 5
    #
    # else:
    #     print("Since cardboard is biodegradable, "
    #           "it produces Methane(the greenhouse gas) as it breaks down, maybe we'll get to live a few more "
    #           "years until the sun collapses on us, thanks to your coffee.")

    # print("Looks like you got back later than expected from your morning run.\n "
    #       "You don't have too much time to drink coffee, but at least you can\n"
    #       "choose the cup you will drink it from.\n"
    #       "A: Cardboard cup\n"
    #       "B: Glass cup\n")

    question = "Looks like you got back later than expected from your morning run.\n" \
               "You don't have too much time to drink coffee, but at least you can\n" \
               "choose the cup you will drink it from.\n" \
               "A: Glass cup\n" \
               "B: Cardboard cup\n" \

    answer_a = "Since cardboard is biodegradable, \n" \
               "it produces Methane(the greenhouse gas) as it breaks down, maybe we'll get to live a few more \n" \
               "years until the sun collapses on us, thanks to your coffee."

    answer_b = "Cardboard is made from wood pulp and cellulose fibers,\n" \
               "which means that in order to make new cardboard-\n" \
               "it is necessary to cut down new trees.. you think your coffee is that important?."

    # answer = Inputs.valid_answer()
    #
    # if answer == 'b':
    #     main.score -= 5

    return (question, answer_a, answer_b)


def question_3():
    # random_answer = ["About 11 million cars were designed to cheat air pollution tests, did you cheat yours?",
    #                  "91% of the World’s Population Are Breathing in Polluted Air Every Day, happy to Happy to contribute?",
    #                  "Air pollution makes climate change worse, not that its news to you, but have fun in your car"]
    #
    # print("OK now you really don't have time, How are you going to get to work? "
    #       "A: Your private car\n"
    #       "B: Your bike\n")
    # answer = Inputs.valid_answer()
    #
    # if answer == 'a':
    #     print(random.choice(random_answer))
    #     main.score -= 5
    #
    # else:
    #     print("Diesel exhaust causes cancer, thanks for not using it.")

    question = "OK now you really don't have time, How are you going to get to work?\n" \
               "A: Your private car\n" \
               "B: Your bike\n"

    return question


def question_4():
    print("its sooooo hot in here, even my GPU is about to go up in flames, what are you going to do?\n"
          "A: Turn on the AC"
          "B: Dont turn on the AC")

    answer = Inputs.valid_answer()

    if answer == 'a':
        print("Okay, turn it on. But just so you know, electrical waves cause- ", end=" ")
        print("headaches, dizziness, nausea, difficulty concentrating, "
              "memory loss, irritability, depression, anxiety, insomnia, fatigue, weakness, tremors, muscle spasms, "
              "numbness, tingling, altered reflexes, muscle and joint pain, "
              "leg/foot pain, “Flue-like” symptoms, fever, palpitations, "
              "arrhythmias, pain or pressure in the chest, low or high blood pressure, "
              "slow or fast heart rate, shortness of breath,  "
              "sinusitis, bronchitis, pneumonia, asthma, skin rash, itching, burning, facial flushing, pain or burning in the eyes, "
              "pressure in/behind the eyes, deteriorating vision, floaters, cataracts.")
        main.score -= 5

    else:
        print("Nice, you avoided the side effects of electrical waves, which by the way are- ")
        print("headaches, dizziness, nausea, difficulty concentrating, "
              "memory loss, irritability, depression, anxiety, insomnia, fatigue, weakness, tremors, muscle spasms, "
              "numbness, tingling, altered reflexes, muscle and joint pain, "
              "leg/foot pain, “Flue-like” symptoms, fever, palpitations, "
              "arrhythmias, pain or pressure in the chest, low or high blood pressure, "
              "slow or fast heart rate, shortness of breath,  "
              "sinusitis, bronchitis, pneumonia, asthma, skin rash, itching, burning, facial flushing, pain or burning in the eyes, "
              "pressure in/behind the eyes, deteriorating vision, floaters, cataracts.")


def question_5():
    # question = "UH looks like there was an error and your printer printed 647298473 extra pages. You need to get rid of it" \
    #            "A: Go to the floor recycling bin\n" \
    #            "B: Go to my trash can? What else you want me to do?"
    #
    # answer = Inputs.valid_answer()
    #
    # if answer == 'a':
    #     print("good, you just saved some trees")
    # else:
    #     print("What do you mean 'what else you want me to do'? I want you to think about the fact that "
    #           "In the last 40 years, paper usage has grown 400%. This means that over two million trees are felled every day for global paper consumption, "
    #           "meaning four billion trees are cut every year to serve our paper needs.")
    question = "UH looks like there was an error and your printer printed 647298473 extra pages. You need to get rid of it\n" \
               "A: Go to the floor recycling bin\n" \
               "B: Go to my trash can? What else you want me to do?"

    return question


question_list = [question_1(), '', question_2(), '', question_3(), '']
for ok in question_list:
    print(ok)

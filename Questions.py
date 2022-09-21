def scene_1():
    return ("I see you're awake! good, We have a lot of choices to make!..\n no, I mean things to do!")

def question_1():
    question = "Look! There's some trash over there, what are you going to do with it?\n" \
               "A: Pick it up\n" \
               "B: Leave it there\n "

    answer_a = "Nice, Plastic waste kills up to one million seabirds, 100,000 sea mammals, \n" \
               "marine turtles and countless fish each year, nice of you to save some turtles."

    answer_b = "Uh, more than 8 million tons of plastic enter the oceans each year- \n" \
               "equal to dumping a garbage truck of plastic every minute, \n" \
               "and you couldn't be bothered to pick up one bag, not cool."

    return (question, answer_a, answer_b)


def question_2():
    question = "Looks like you got back later than expected from your morning run.\n" \
               "You don't have too much time to drink coffee, but at least you can\n" \
               "choose the cup you will drink it from.\n" \
               "A: Glass cup\n" \
               "B: Cardboard cup\n"

    answer_a = "Since cardboard is biodegradable, \n" \
               "it produces Methane(the greenhouse gas) as it breaks down, maybe we'll get to live a few more \n" \
               "years until the sun collapses on us, thanks to your coffee."

    answer_b = "Cardboard is made from wood pulp and cellulose fibers,\n" \
               "which means that in order to make new cardboard-\n" \
               "it is necessary to cut down new trees.. you think your coffee is that important?."

    return (question, answer_a, answer_b)


def question_3():
    question = "OK now you really don't have time, How are you going to get to work?\n" \
               "A: Your private car\n" \
               "B: Your bike\n"

    answer_a = "Diesel exhaust causes cancer, thanks for not using it."

    answer_b = "91% of the World’s Population Are Breathing in Polluted Air Every Day, happy to Happy to contribute?"

    return (question, answer_a, answer_b)


def question_4():
    question = "It's sooooo hot in here, even my GPU is about to go up in flames, what are you going to do?\n" \
               "A: Turn on the AC\n" \
               "B: Dont turn on the AC"

    electric_waves_effet = "headaches, dizziness, nausea, difficulty concentrating, \n" \
                           "memory loss, irritability, depression, anxiety, insomnia, fatigue, weakness, tremors, muscle spasms, \n" \
                           "numbness, tingling, altered reflexes, muscle and joint pain, \n" \
                           "leg/foot pain, “Flue-like” symptoms, fever, palpitations, \n" \
                           "arrhythmias, pain or pressure in the chest, low or high blood pressure, \n" \
                           "slow or fast heart rate, shortness of breath,  \n" \
                           "sinusitis, bronchitis, pneumonia, asthma, skin rash, itching, burning, facial flushing, pain or burning in the eyes, \n" \
                           "pressure in/behind the eyes, deteriorating vision, floaters, cataracts."

    answer_a = "Nice, you avoided the side effects of electrical waves, which by the way are- \n" + electric_waves_effet

    answer_b = "Okay, turn it on. But just so you know, electrical waves cause- \n" + electric_waves_effet

    return (question, answer_a, answer_b)


def question_5():
    question = "Looks like there was an error and your printer printed 647298473 extra pages. You need to get rid of it\n" \
               "A: Go to the floor recycling bin\n" \
               "B: Go to my trash can? What else you want me to do?"

    answer_a = "good, you just saved some trees"

    answer_b = "What do you mean 'what else you want me to do'? I want you to think about the fact\n" \
               " that In the last 40 years, paper usage has grown 400%. This means that over two million trees are felled every day for global paper consumption, \n" \
               "meaning four billion trees are cut every year to serve our paper needs."

    return (question, answer_a, answer_b)


def question_6():
    question = "Get in user!! we are going shopping!!!\n" \
               "A: Buy slow fashion\n" \
               "B: Buy fast fashion"

    answer_a = "That's good, we should not support an industry that encourages customers to keep buying the latest trends, and as a result " \
               "The quantity of unworn clothing in the average fashionista’s closet just keeps increasing"

    answer_b = "Fast fashion? Did you know that according to the International Union for Conservation of Nature, " \
               "35 percent of microplastics that enter the ocean come from synthetic fibers.. I hope you picked up that plastic bug"

    return (question, answer_a, answer_b)


question_list = ['', scene_1(),'', '', question_1(), '', question_2(), '', question_3(),'', question_4(),'', question_5(),'',  question_6(), '', '', '']
picture = ["images/20.jpg", "images/19.jpg", "images/5.png", "images/8.jpg", "images/9.png", "images/10.png", "images/12.jpg", "images/14.jpg", "images/15.jpg", "images/19.jpg", "images/20.jpg"]

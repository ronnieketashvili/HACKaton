import pygame
import Questions
import music


def start_game():
    text_surf = None
    text_len = 0
    typewriter_event = pygame.USEREVENT + 1
    pygame.time.set_timer(typewriter_event, 20)

    run = True
    row = 0
    index = 0

    for questions in questions_tuples:
        if len(questions) != 0:
            user_input = ''
            row = 0
            window.blit(background, (0, 0))

            if len(questions) > 2:
                question_lines = questions[0].splitlines()
                answer_a = questions[1].splitlines()
                answer_b = questions[2].splitlines()
            else:
                question_lines = questions[0].splitlines()

            for line in question_lines:
                text = line
                row += 20
                run = True

                music.typing_sound()

                while run:
                    clock.tick(60)
                    for event in pygame.event.get():
                        if event.type == typewriter_event:
                            text_len += 1

                            if text_len > len(text):
                                text_len = 0
                                run = False

                            text_surf = None if text_len == 0 else font.render(text[:text_len], True, (255, 255, 255))

                    if text_surf:
                        window.blit(text_surf, (0, row))

                    pygame.display.flip()

            if len(questions) > 2:
                while user_input == '' and len(question_lines) != 0:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()

                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_a:
                                user_input = 'a'
                                print_answer(answer_a)
                                break

                            elif event.key == pygame.K_b:
                                user_input = 'b'
                                print_answer(answer_b)
                                break

            else:
                run = True

                while run:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            run = False

            window.blit(background, (0, 0))
            print(input)
            pygame.mixer.music.stop()

        else:  # image
            surface = pygame.display.set_mode((700, 700))
            pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(0, 0, 700, 700))

            background_img = pygame.image.load(picture_list[index]).convert_alpha()
            index += 1
            background_img = pygame.transform.scale(background_img, (700, 700))
            window.blit(background_img, (0, 0))
            pygame.display.flip()

            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        run = False

    pygame.quit()


def print_answer(answer):
    window.blit(background, (0, 0))

    run = True
    row = 0

    text_surf = None
    text_len = 0
    typewriter_event = pygame.USEREVENT + 1
    pygame.time.set_timer(typewriter_event, 20)

    for line in answer:
        text = line
        row += 20
        run = True

        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == typewriter_event:
                    text_len += 1

                    if text_len > len(text):
                        text_len = 0
                        run = False

                    text_surf = None if text_len == 0 else font.render(text[:text_len], True, (255, 255, 255))

            if text_surf:
                window.blit(text_surf, (0, row))

            pygame.display.flip()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return


pygame.init()
window = pygame.display.set_mode((700, 700))  # creating the screen window
clock = pygame.time.Clock()
font = pygame.font.SysFont('microsoftyibaiti', 20)  # setting the font of the text

background = pygame.Surface(window.get_size())  # creating the surface

questions_tuples = Questions.question_list
picture_list = Questions.picture

start_game()

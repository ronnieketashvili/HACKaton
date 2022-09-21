import pygame
import Questions

pygame.init()
window = pygame.display.set_mode((700, 700))  # creating the screen window
clock = pygame.time.Clock()  # ?
font = pygame.font.SysFont('microsoftyibaiti', 20)  # setting the font of the text

background = pygame.Surface(window.get_size())  # creating the surface

text = Questions.question_1()
lines = text.splitlines()

text_len = 0
typewriter_event = pygame.USEREVENT + 1
pygame.time.set_timer(typewriter_event, 50)
text_surf = None

run = True
row = 0

for line in lines:

    text = line
    row += 20
    run = True

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            # if event.type == pygame.QUIT:
            #     run = False
            if event.type == typewriter_event:
                text_len += 1
                if text_len > len(text):
                    text_len = 0
                    run = False
                text_surf = None if text_len == 0 else font.render(text[:text_len], True, (255, 255, 255))

        # window.blit(background, (0, 0))

        if text_surf:
            window.blit(text_surf, (0, row))
        pygame.display.flip()

input = ''
while input == '':
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                input = 'a'
            elif event.key == pygame.K_b:
                input = 'b'

print(input)
pygame.quit()

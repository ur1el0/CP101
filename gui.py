import pygame
import sys

pygame.init()

SCREEN = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Flashcard Quiz")
x = 600
y = 600

bg = pygame.image.load('/mnt/chromeos/MyFiles/Downloads/white-wall-lamp.jpg')

FLASHCARD_COLOUR = 46, 56, 86
FLIPPED_COLOUR = 89, 94, 109
FONT = pygame.font.SysFont("simonsays", 25)

newimage = pygame.transform.scale(bg, (x, y))
SCREEN.blit(newimage, (20, 20))

quiz_data = {
    "What is the largest mammal on Earth?": {
        "answer": "Blue Whale --",
        "trivia": "The Blue Whale holds the title for being the largest mammal on Earth, reaching lengths of up to 100 feet."
    },
    "Who wrote 'To Kill a Mockingbird'?": {
        "answer": "Harper Lee --",
        "trivia": "'To Kill a Mockingbird' was written by Harper Lee and was first published in 1960."
    },
    "What is the currency of Brazil?": {
        "answer": "Brazilian Real --",
        "trivia": "The official currency of Brazil is the Brazilian Real, abbreviated as BRL."
    },
    "Which planet is known as the 'Gas Giant'?": {
        "answer": "Jupiter --",
        "trivia": "Jupiter, the fifth planet from the Sun, is known as a 'Gas Giant' due to its predominantly gaseous composition."
    },
    "Anong taon lumubog ang barkong Titanic?": {
        "answer": "1912 --",
        "trivia": "The Titanic sank on April 15, 1912, during its maiden voyage from Southampton to New York City."
    },
    "Who is the author of 'The Great Gatsby'?": {
        "answer": "F. Scott Fitzgerald --",
        "trivia": "'The Great Gatsby' was written by F. Scott Fitzgerald and is considered a classic of American literature."
    },
    "What is the capital of Australia?": {
        "answer": "Canberra --",
        "trivia": "Canberra is the capital city of Australia, located in the Australian Capital Territory."
    },
    "Which element has the chemical symbol 'O'?": {
        "answer": "Oxygen --",
        "trivia": "Oxygen is a chemical element with the symbol 'O' and atomic number 8. It is essential for life on Earth."
    },
    "Who painted the 'Mona Lisa'?": {
        "answer": "Leonardo da Vinci --",
        "trivia": "The 'Mona Lisa' was painted by the Italian artist Leonardo da Vinci during the Renaissance period."
    },
    "What is the official language of China?": {
        "answer": "Mandarin --",
        "trivia": "Mandarin is the official language of China and is spoken by the majority of the Chinese population."
    },
}

def render_text(text, position, max_width):
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        test_line = current_line + " " + word if current_line else word
        test_width, _ = FONT.size(test_line)
        if test_width <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)

    for i, line in enumerate(lines):
        text_surface = FONT.render(line, True, "white")
        text_rect = text_surface.get_rect(center=(position[0], position[1] + i * 30 - 20))
        SCREEN.blit(text_surface, text_rect)

current_question = ""
current_answer = ""
current_trivia = ""

card_turned = False

index = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                card_turned = not card_turned
            elif pygame.key.get_pressed()[pygame.K_RIGHT] and index < len(quiz_data) - 1:
                index += 1
                card_turned = False
            elif pygame.key.get_pressed()[pygame.K_LEFT] and index > 0:
                index -= 1
                card_turned = False

    current_question = list(quiz_data)[index]
    current_answer = quiz_data[current_question]["answer"]
    current_trivia = quiz_data[current_question]["trivia"]

    card_width = 350
    card_height = 250

    if not card_turned:
        SCREEN.blit(newimage, (0, 0))
        pygame.draw.rect(SCREEN, FLASHCARD_COLOUR, (125, 175, card_width, card_height))
        render_text(current_question, (300, 250), card_width - 20)
    else:
        SCREEN.blit(newimage, (0, 0))
        pygame.draw.rect(SCREEN, FLIPPED_COLOUR, (125, 175, card_width, card_height))
        render_text(f"Answer: {current_answer}\n\nTrivia: {current_trivia}", (300, 250), card_width - 20)

    current_index_object = FONT.render(f"{index+1}/{len(quiz_data)}", True, "white")
    current_index_rect = current_index_object.get_rect(center=(300, 550))
    SCREEN.blit(current_index_object, current_index_rect)

    pygame.display.update()
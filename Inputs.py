def valid_answer():
    answer = input().lower().strip()

    while answer != 'a' and answer != 'b':
        answer = input("Invalid answer - try again").lower().strip()

    return answer

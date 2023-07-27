morse_code = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
              '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
              '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
              '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
              '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
              '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
              '-.--': 'Y', '--..': 'Z'
              }

user_input = input().split(" | ")
message = []

for word in user_input:
    new_word = []
    letters = word.split()
    for letter in letters:
        if letter in morse_code:
            new_word.append(morse_code[letter])
    message.append("".join(new_word))

print(" ".join(message))

class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


info = input()
emails = []
while info != "Stop":
    current_info = info.split()
    emails.append(Email(current_info[0], current_info[1], current_info[2]))
    info = input()

indices = list(map(int, input().split(", ")))
for index, email in enumerate(emails):
    if index in indices:
        email.send()
    print(email.get_info())

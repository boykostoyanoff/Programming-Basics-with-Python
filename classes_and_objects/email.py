class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = list()
while True:
    command_info = input()
    if command_info == 'Stop':
        break
    command_info = command_info.split(' ')
    email = Email(command_info[0], command_info[1], command_info[2])
    emails.append(email)

sent_emails_indexes = [int(e) for e in input().split(', ')]
for e in sent_emails_indexes:
    emails[e].send()

for e in emails:
    print(e.get_info())

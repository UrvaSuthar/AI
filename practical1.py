about_bot = ['what your name', 'name', 'your name']
about_course = ['show courses', 'how many courses are available', 'courses']
about_location = ['location', 'where are you located']
about_fees = ['fees', 'tell me about fees', 'how much is fees']
about_greeting = ['hi','hello','hey']
new_questions = []
end = ['close','bye', 'close', 'end']


def chatbot(query):
    query = query.lower()
    print('Bot: ', end='')
    if query in about_bot:
        print('Hello! My name is Chatbot')
        return True
    if query in about_course:
        print('We have many courses.')
        return True
    if query in about_location:
        print('We are located at Kherava.')
        return True
    if query in about_fees:
        print('Fees Are 57000 Per Sem.')
        return True
    if 'website' in query:
        print('Our Website is http://ganpatuniversity.ac.in/')
        return True
    if query in about_greeting:
        print('Hey There!')
        return True
    if 'name' in query:
        print('My name is chatter.')
        return True
    if 'wether' in query:
        print('Currently I am not able to answer that.')
        return True
    if 'Contact' in query:
        print('Our Contact number is +91 1234567890')
        return True
    if 'time' in query:
        print("I am not using any libraries, so i can't give the ")
        return True
    if 'address' in query:
        print('Ganpat university, kherava, mehasana.')
    if query in end:
        print('Thank You for using this bot.\nBye 👋')
        return False
    else:
        print('I am not able to give answer to this question')
        new_questions.append(query)
        return True


flag = True
i = 0
sp_char = [('!', ''), ('@', ''), ('#', ''), ('$', ''), ('%', ''),
           ('^', ''), ('&', ''), ('*', ''), ('?', ''), ('.', '')]
while flag == True:
    if i == 0:
        print("Chatbot: ", end='')
        usr_question = input('Hello! How may I help you?\nUser:')
        for char, replacement in sp_char:
            if char in usr_question:
                usr_question = usr_question.replace(char, replacement)
        flag = chatbot(usr_question)
        i = 1
    else:
        que = input('User: ').lower()
        for char, replacement in sp_char:
            if char in que:
                que = que.replace(char, replacement)
        flag = chatbot(que)

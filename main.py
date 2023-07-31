import tkinter as tk
import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)
    
    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('Python is a more well-known programming language than C++ for AI and has a lead with a 57% majority vote from developers. This is due to the fact that Python is simple to master and use. With its numerous libraries', ['python', 'Ai'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('anything else?', ['yes', 'okay'], single_response=True)
    response('thank you for using me', ['no', 'thats it'], single_response=True)
    response('I\'m doing fine', ['how', 'are', 'you', 'doing'], required_words=['doing'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('I am an artificial intelligence language model, so I don\'t have an age.', ['age'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    
    # Responses -------------------------------------------------------------------------------------------------------
    response('My friend thinks he is smart. He told me an onion is the only food that makes you cry, so I threw a coconut at his face.', ['joke'], single_response=True)
    response('I appreciate your feedback. Thank you.', ['thanks', 'appreciate'], single_response=True)
    response('chatgpt is a chatbot like me  ', ['chatgpt', 'is', 'a', 'chatbot'], required_words=['chatgpt'])
    response('google is a search engine  ', ['google'], required_words=['what is google'])
    response('That\'s cool! I\'ve always been fascinated by that too.', ['fascinated', 'cool', 'always', 'been'], single_response=True)
    response('I\'m not sure I understand. Can you please clarify?', ['clarify', 'not', 'understand', 'sure'], required_words=['clarify'])
    response('That\'s awesome! How did you get into that?', ['awesome', 'get', 'into', 'that'], required_words=['get', 'into'])
    response('I\'m sorry to hear that. Do you want to talk about it?', ['sorry', 'hear', 'talk', 'about'], required_words=['talk', 'about'])
    response('That\'s really neat! What inspired you to do that?', ['neat', 'inspired', 'do', 'that'], required_words=['inspired'])
    response('I see. Can you elaborate a little more?', ['elaborate', 'little', 'more'], single_response=True)
    response('That\'s too bad. Is there anything I can do to help?', ['too', 'bad', 'anything', 'help'], required_words=['help'])
    response('That\'s impressive! What\'s the most challenging part of it?', ['impressive', 'challenging', 'part', 'of'], required_words=['challenging'])
    response('I\'m sorry, I don\'t know the answer to that. Would you like me to look it up?', ['sorry', 'know', 'answer', 'look'], required_words=['look', 'up'])
    response('That\'s really cool! What do you enjoy most about it?', ['cool', 'enjoy', 'most', 'about'], required_words=['enjoy'])
    response('I\'m sorry, I\'m not quite sure what you mean. Can you explain it differently?', ['sorry', 'sure', 'explain', 'differently'], required_words=['explain', 'differently'])
    response('That\'s really fascinating! Can you tell me more about it?', ['fascinating', 'tell', 'more', 'about'], required_words=['tell', 'more'])
    response('That sounds like a lot of work! What motivates you to keep going?', ['lot', 'work', 'motivates', 'keep', 'going'], required_words=['motivates'])
    response('I\'m sorry, I don\'t have an answer for that. Would you like to talk about something else?', ['sorry', 'answer', 'talk', 'about'], required_words=['talk', 'about'])
    response('That\'s amazing! How did you learn to do that?', ['amazing', 'learn', 'do', 'that'], required_words=['learn'])
    response('I\'m sorry, I don\'t have any advice to offer. Would you like to talk about something else?', ['sorry', 'advice', 'talk', 'about'], required_words=['talk', 'about'])
    response('That\'s really impressive! What inspired you to start doing that?', ['impressive', 'inspired', 'start', 'doing'], required_words=['inspired'])

    response('I am an artificial intelligence language model, so I don\'t have an age.', ['age', 'old', 'birthday', 'year'], required_words=['old'])
    response('I dont have a favorite color, as I am an artificial intelligence language model.', ['color'], required_words=['favourite color'])
    response('The last Fifa World Cup was won by Argentina in 2022', ['fifa','world cup'], required_words=['fifa'])
    response('The capital of Pakistan is Islamabad', ['capital'], required_words=['capital'])
    response('I don\'t have a favorite movie, as I am an artificial intelligence language model.', ['movie'], required_words=['favourite movie'])
    response('The tallest mountain in the world is Mount Everest', ['mountain'], required_words=['mountain'])
    response('The current president of Pakistan is Arif Alvi', ['current','president'], required_words=['current','president'])
    response('The best way to study for an exam is to create a study plan, review class notes and materials regularly, and practice with sample questions and tests.', ['best', 'exam', 'preparation'], required_words=['exam'])
    response('To start a business, you will need a solid business plan, funding, and legal permits and registrations. Seek advice from business professionals or mentors.', ['business', 'invest'], required_words=['business'])
    response('As an AI language model, I do not have a favorite TV show.', ['tv','show'], required_words=['tv','show'])
    response('To improve writing skills, practice regularly, read widely, and seek feedback from peers or writing coaches.', ['writing','improve'], required_words=['writing'])
    response('The best way to save money is to create a budget, track your expenses, and avoid unnecessary purchases.', ['save','money'], required_words=['save','money'])
    response('The last World Cup was won by England in 2022', ['world',], required_words=['world','cricket'])
    response('As of April 2023, the latest version of Python is 3.10.0.', ['python','version'], required_words=['python','version'])
    response('Python was created by Guido van Rossum in 1989', ['created','python'], required_words=['python'])
    response('Urdu', ['language','pakistan'], required_words=['language','pakistan'])
    response('Pakistani rupees', ['currency'], required_words=['currency','pakistan'])
    response('Quaid e Azam Muhammad Ali Jinnah', ['founder','pakistan'], required_words=['founder','pakistan'])
    response('Imran Khan', ['prime', 'minister', 'ex'], required_words=['ex','prime','minister','pakistan'])
    
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_RECIPE, ['pizza', 'recipe'], required_words=['pizza','recipe'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.R_HACKING, ['hack', 'hacking'], required_words=['hacking'])
    response(long.R_STRESS, ['stress'], required_words=['stress'])
    response(long.R_WORKOUT, ['workout',], required_words=['workout'])
    response(long.R_MESSI, ['messi',], required_words=['messi'])
    response(long.R_ARTIFICAL, ['artifical'], required_words=['artifical'])
    response(long.R_SOFTWARE, ['software'], required_words=['software'])
    response(long.R_DATA, ['data','mining'], required_words=['data','mining'])
    response(long.R_CACHE, ['cache'], required_words=['cache'])
    response(long.R_PROGRAMMING, ['programming'], required_words=['programming'])

    



    best_match = max(highest_prob_list, key=highest_prob_list.get)
    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


class ChatbotGUI:
    def __init__(self, master):
        self.master = master
        master.title("Ai Chatbot ")
        master.configure(bg='#e6ffff')  # set background color of master widget

        # Configure chat history text widget
        self.chat_history = tk.Text(master, state=tk.DISABLED, bg='#ccffeb', fg='#000000', font=("Helvetica", 14))
        self.chat_history.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Configure user input text entry
        self.user_input = tk.Entry(master, bg='#e6ffff', fg='#000000', font=("Helvetica", 14))
        self.user_input.pack(fill=tk.X, padx=10, pady=10)

        # Bind <Return> event to send_message method
        self.user_input.bind('<Return>', self.send_message)

        # Configure send message button
        self.send_button = tk.Button(master, text="Send Message", command=self.send_message, bg='#008CBA', fg='#FFFFFF', font=("Helvetica", 14), height=2)
        self.send_button.pack(fill=tk.X, padx=10, pady=10)

        self.user_input.focus_set()

    def send_message(self, event=None):
        user_input = self.user_input.get()
        response = get_response(user_input)

        self.chat_history.configure(state=tk.NORMAL)
        self.chat_history.insert(tk.END, f"You: {user_input}\n", ("user",))
        self.chat_history.insert(tk.END, f"Ai Bot: {response}\n", ("bot",))
        self.chat_history.configure(state=tk.DISABLED)

        self.user_input.delete(0, tk.END)


root = tk.Tk()
root.geometry("800x800")
root.configure(bg='#e6ffff')
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)


gui = ChatbotGUI(root)

root.mainloop()

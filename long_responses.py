import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_COMPUTER = "Computer science is the study of computers and computational systems, including software, hardware, algorithms, data structures, and programming languages."
R_PROGRAMMING = "Programming is the process of designing, writing, testing, and maintaining computer programs."
R_ARTIFICAL = "Artificial intelligence is the simulation of human intelligence in machines that are programmed to perform tasks that typically require human intelligence, such as learning, problem-solving, and decision making."
R_DATA = "Data mining is the process of analyzing large datasets to extract useful information and patterns."
R_SERVER = "A server is a computer program or device that provides services to other computer programs or devices, often used to store and manage data."
R_SOFTWARE = "A software bug is an error in a computer program that causes it to produce unexpected results or behavior."
R_CACHE = "A cache is a temporary storage location that stores frequently accessed data for quick retrieval, often used to improve system performance."
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_HACKING = "Hacking is illegal we don't provide any hacking info sorry"
R_RECIPE = "1 pound pizza dough (store-bought or homemade) 1/2 cup pizza sauce 2 cups shredded mozzarella cheese Optional toppings: sliced pepperoni, sliced mushrooms, diced bell peppers, sliced onions, cooked sausage, olives, etc."
R_WORKOUT = "A good workout routine should include a mix of cardio and strength training, with appropriate warm-up and cool-down periods. Consult a fitness professional for personalized advice."
R_STRESS = "To deal with stress, practice relaxation techniques like meditation or deep breathing, exercise regularly, and seek support from friends or professionals if needed."
R_MESSI = "Lionel Messi is a professional soccer player from Argentina who is widely considered one of the best players in the history of the sport. He has played for Barcelona since he was a teenager and has won numerous awards and championships during his career, including the Ballon d'Or, which is given to the world's best player. He has also helped lead Argentina's national team to several major tournaments, including the World Cup."

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response

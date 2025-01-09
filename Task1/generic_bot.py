import random
import re
import spacy

# Load spaCy English language model
nlp = spacy.load("en_core_web_sm")

# Base Class for Generic Bot
class GenericBot:

    exit_commands = (
        "quit", "pause", "exit", "goodbye", "bye", "later", "see ya", "take care", 
        "farewell", "adios", "ciao", "end", "stop", "close", "I'm done", "leave", 
        "shut down", "log out", "peace out"
    )
 
    feedback_responses = {
        "yes": "I'm glad I could help!",
        "no": "I'm sorry to hear that.",
    }

    def __init__(self, field_name, conversation_questions, user_patterns, response_handlers):
        """
        Initializes the bot with field-specific data.

        :param field_name: The field of expertise (e.g., Health, Technology).
        :param conversation_questions: List of questions to ask the user.
        :param user_patterns: A dictionary mapping user input patterns to response keys.
        :param response_handlers: A dictionary mapping response keys to handler methods.
        """
        self.field_name = field_name
        self.conversation_questions = conversation_questions
        self.user_patterns = user_patterns
        self.response_handlers = response_handlers

    def introduce_bot(self):
        """
        Introduces the bot to the user and explains its purpose.
        """
        print(f"Hello! I am a bot specialized in {self.field_name}.")
        print("I’m here to discuss and learn more about this topic with you.")
        print("Type 'quit', 'bye', or similar commands to exit the conversation anytime.")
        self.start_conversation()

    def check_exit_command(self, user_input):
        """
        Checks if the user input matches any exit command.

        :param user_input: The user's reply.
        :return: True if an exit command is detected, otherwise False.
        """
        for command in self.exit_commands:
            if user_input == command:
                print("Goodbye! Have a great day!")
                return True
        return False

    def start_conversation(self):
        """
        Starts the conversation loop by asking the user random questions.
        """
        try:
            user_input = input(random.choice(self.conversation_questions)).lower()
            while not self.check_exit_command(user_input):
                response = self.process_user_input(user_input)
                print(response)
                feedback = input("Was this answer helpful? (yes/no): ").lower()
                print(self.feedback_responses[feedback])
                user_input = input(random.choice(self.conversation_questions)).lower()

        except Exception as e:
            print(f"An error occurred during the conversation: {str(e)}")

    def process_user_input(self, user_input):
        """
        Processes user input by analyzing it using regex, spaCy lemmatization, intent similarity, 
        and named entity recognition to determine the best response.
        """    
        try:
            doc = nlp(user_input)
            
            # Step 1: Match user input with regular expressions, Fast handle for inputs without ambiguity
            for response_key, pattern in self.user_patterns.items():
                if re.match(pattern, user_input):
                    return self.response_handlers[response_key]()
            
            # Step 2: Check for specific keywords/entities using spaCy token lemmatization            
            for token in doc:
                if token.lemma in self.user_patterns:
                    response_key = self.user_patterns[token.lemma]
                    return self.response_handlers[response_key]()
                
            # Step 3: Use spaCy similarity for intent detection, Powerful but computationally heavier than regex and keyword matching, so used when simpler methods (regex/keywords) don’t match.
            user_doc = nlp(user_input)
            max_similarity = 0
            best_match = None
            for pattern_key, pattern in self.user_patterns.items():
                pattern_doc = nlp(pattern)  # Convert the regex pattern/key to a spaCy Doc for similarity comparison
                similarity = user_doc.similarity(pattern_doc)
                if similarity > max_similarity:
                    max_similarity = similarity
                    best_match = pattern_key
            # If the similarity is above a threshold, use the matched pattern's response handler
            if best_match and max_similarity > 0.7:
                return self.response_handlers[best_match]()
            
            # Step 4: Check for named entities to enhance interaction, Using it after the primary intent has been established
            for ent in doc.ents:
                if ent.label_ in ["PERSON", "ORG", "GPE", "DATE", "TIME"]:
                    return f"I noticed you mentioned {ent.text}. Could you tell me more about it?"
            return self.default_response()
        except Exception as e:
            print(f"An error occurred while analyzing your input: {str(e)}")
            print("Goodbye! Have a great day!")

    def default_response(self):
        """
        Provides a generic response when no response handler.
        """
        fallback_responses = (
            "Could you elaborate on that?\n",
            "That's interesting. Tell me more!\n",
            "I see. Can you explain further?\n",
            "Why do you say that?\n",
            "I'm curious, could you provide more details?\n",
            "That's fascinating. What makes you think so?\n",
            "Can you clarify what you mean?\n",
            "I'd love to hear more about that!\n",
            "What led you to that conclusion?\n",
            "Interesting perspective! Could you expand on it?\n",
            "I'm not sure I understand. Can you give an example?\n",
            "Could you provide some context for that?\n",
            "That's a great point! Can you go into more depth?\n",
            "Can you tell me a bit more about it?\n",
            "What do you mean exactly?\n",
            "I'm intrigued—please tell me more!\n"
        )
        return random.choice(fallback_responses)


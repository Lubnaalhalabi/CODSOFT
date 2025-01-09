# Chatbot with Field-Specific Expertise 

This is a Python-based chatbot framework capable of handling conversations on specific topics like Health and Wellness, Technology and Innovation, and Personal Finance. The chatbot uses techniques such as regular expressions, keyword detection, semantic similarity, and named entity recognition (NER) to understand user input and provide relevant responses.

# Features

- Modular Design: Separate bots for different fields of expertise.
- Natural Language Processing: Utilizes spaCy for NER, lemmatization, and intent matching.
- Feedback System: Gathers user feedback to improve responses.
- Interactive User Interface: Users can choose a bot based on their interests.
- Exit Commands: Allows users to exit the conversation gracefully at any time.

# Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.7 or later
- spaCy
- Required English language model (`en_core_web_sm`)

Install the dependencies using:
- pip install spacy
- python -m spacy download en_core_web_sm

# File Structure

- main.py: The entry point of the chatbot framework.
- health_and_wellness.py: Contains the implementation of the HealthBot.
- technology_and_innovation.py: Contains the implementation of the   TechBot.
- personal_finance_and_innovation.py: Contains the implementation of the FinanceBot.

# How to Run

1. Clone the repository.
2. Navigate to the project directory.
3. Run the main script: python main.py.
4. Choose a bot to interact with by entering the corresponding number.

# How It Works

1. The user selects a chatbot (Health, Technology, or Finance).
2. The bot initiates the conversation by asking field-specific questions.
3. User inputs are processed using:
   - Regular Expressions for pattern matching.
   - Lemmatization and Token Analysis using spaCy.
   - Semantic Similarity for intent recognition.
   - Named Entity Recognition (NER) to identify key entities like names, places, or dates.
4. The bot responds based on detected intents or falls back to a default response if no match is found.
5. The user provides feedback on the bot's response to improve its behavior.

# Customization
You can add new bots or enhance existing ones by following these steps:

1. Create a new Python file for the bot.
2. Define the bot class with:
   - Field-specific questions.
   - User patterns and response handlers.
3. Update main.py to include the new bot option.
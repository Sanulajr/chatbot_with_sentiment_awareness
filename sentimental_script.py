from textblob import TextBlob
from dataclasses import dataclass

@dataclass
class Mood:
    sentiment: float
    response: str

def get_mood(input_text: str) -> Mood:
    sentiment: float = TextBlob(input_text).sentiment.polarity

    # Determine mood based on sentiment thresholds
    if sentiment > 0.5:
        response = "Wow, you're on cloud nine! Keep shining and spreading those positive vibes. 😊🌟 Everything looks brighter when you're this happy!"
    elif sentiment > 0.1:
        response = "Great to hear you're feeling good! Keep that positive energy flowing. 😊 It’s going to be an amazing day!"
    elif sentiment < -0.1 and sentiment > -0.5:
        response = "I'm really sorry you're feeling this way. Remember, tough times don’t last, but tough people do. Take it one step at a time—I'm here if you want to talk."
    elif sentiment < -0.5:
        response = "I'm really sorry you're going through this. It might feel overwhelming right now, but you're not alone. Take things one moment at a time, and remember, things can get better. I'm here for you."
    else:
        response = "Neutral."
    

    return Mood(sentiment, response)

def get_mood_response(mood: Mood):
    print(f'Sentiment: {mood.sentiment:.2f}')
    print(f"Response: {mood.response}")

if __name__ == "__main__":
    print("Welcome to the Sentiment Chatbot! Type 'exit' to quit.")
    
    while True:
        text: str = input("Enter text: ")
        
        if text.lower() == "exit":
            print("Goodbye! Stay positive! 👋")
            break

        mood = get_mood(text)
        get_mood_response(mood)

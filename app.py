import os
from dotenv import load_dotenv, find_dotenv
import openai
from flask import Flask, render_template, request
_ = load_dotenv(find_dotenv())  # read local .env file

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define your delimiter
delimiter = "####"

# General function to get response with gpt-3.5
def get_completion_from_messages(messages,
                                 model="gpt-3.5-turbo",
                                 temperature=0,
                                 max_tokens=1000):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message['content'].strip()


# Step 1: Generate a customer's comment
def generate_comment():
    system_message_comment = """
    Product details can be found as below

        "TechPro Ultrabook": {
            "name": "TechPro Ultrabook",
            "category": "Computers and Laptops",
            "brand": "TechPro",
            "model_number": "TP-UB100",
            "warranty": "1 year",
            "rating": 4.5,
            "features": ["13.3-inch display", "8GB RAM", "256GB SSD", "Intel Core i5 processor"],
            "description": "A sleek and lightweight ultrabook for everyday use.",
            "price": 799.99
        }
    ...
    """  # (Shortened for brevity)

    user_message_comment = f"A less than 100 words comment about the products"

    messages_comment = [
        {'role': 'system', 'content': system_message_comment},
        {'role': 'user', 'content': f"{delimiter}{user_message_comment}{delimiter}"},
    ]
    
    comment = get_completion_from_messages(messages_comment)

    print("Comment from customers: ")
    print(comment + "\n")

    return comment

# Step 2: Generate email subject
def get_subject(comment):
    system_message_subject = comment
    user_message_subject = f"Subject of an email from the comment using Inferring technique within 10 words."
    messages_subject = [
        {'role': 'system', 'content': system_message_subject},
        {'role': 'user', 'content': f"{delimiter}{user_message_subject}{delimiter}"},
    ]
    
    subject = get_completion_from_messages(messages_subject)

    print("Subject of customer comment: ")
    print(subject + "\n")

    return subject

# Step 3: Generate the summary of the customer's comment
def get_summary(comment):
    system_message_summary = comment
    user_message_summary = f"Give the summary in English of the comment using Summarizing technique within 35 words."
    messages_summary = [
        {'role': 'system', 'content': system_message_summary},
        {'role': 'user', 'content': f"{delimiter}{user_message_summary}{delimiter}"},
    ]
    
    summary = get_completion_from_messages(messages_summary)

    print("Summary of customer comment:")
    print(summary + "\n")

    return summary

# Step 4: Sentiment analysis of the customer's comment
def get_sentiment(comment):
    system_message_sentiment = comment
    user_message_sentiment = f"Sentiment analysis of the customer's comment using Inferring technique. Positive or Negative?"
    messages_sentiment = [
        {'role': 'system', 'content': system_message_sentiment},
        {'role': 'user', 'content': f"{delimiter}{user_message_sentiment}{delimiter}"},
    ]
    
    sentiment = get_completion_from_messages(messages_sentiment)

    print(sentiment + "\n")

    return sentiment

# Step 5: Generate an email to be sent to the customer
def get_email(comment, subject, summary, sentiment):
    system_message_email = f"{comment} {subject} {summary} {sentiment}"
    user_message_email = f"Please create an email to be sent to the customer based on the above details with proper email format with subject and extra."
    messages_email = [
        {'role': 'system', 'content': system_message_email},
        {'role': 'user', 'content': f"{delimiter}{user_message_email}{delimiter}"},
    ]
    
    email = get_completion_from_messages(messages_email)

    return email  # Return the email without printing it

def get_translation(summary, language):
    system_message_translate = summary
    user_message_translate = f"Translate the summary into {language} using Transforming technique."
    messages_translate = [
        {'role': 'system', 'content': system_message_translate},
        {'role': 'user', 'content': f"{delimiter}{user_message_translate}{delimiter}"},
    ]
    
    translate = get_completion_from_messages(messages_translate)

    print("Translation of customer comment summary in " + language + ":")
    print(translate + "\n")

    return translate

# Define the index route
@app.route('/', methods=['GET', 'POST'])
def index():
    comment = None
    email = None
    language = "English"  # Initialize the language variable here

    if request.method == 'POST':
        language = request.form['language']
        comment = generate_comment()
        subject = get_subject(comment)
        summary = get_summary(comment)
        sentiment = get_sentiment(comment)
        email = get_email(comment, subject, summary, sentiment)

        # Check if the user wants to translate the comment and email
        translate_comment = 'translate-comment' in request.form
        translate_email = 'translate-email' in request.form

        if translate_comment:
            comment = get_translation(comment, language)

        if translate_email:
            email = get_translation(email, language)

    return render_template('index.html', comment=comment, email=email, language=language)


if __name__ == '__main__':
    app.run(debug=True)

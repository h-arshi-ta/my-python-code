import streamlit as st
import spacy
import difflib
import os
from dotenv import load_dotenv

load_dotenv()

'''Initialize spaCy English model'''
nlp = spacy.load("en_core_web_sm")

'''A list of few FAQ questions'''
faq = {
    "What courses are offered at Shyam Lal College?": "Shyam Lal College offers courses like B.A., B.Com, B.Sc., M.A., and various vocational courses.",
    "What are the admission criteria?": "Admissions are primarily based on CUET scores and merit.",
    "Where is Shyam Lal College located?": "The college is located in Shahdara, New Delhi.",
    "What is the fee structure?": "The fee structure varies by course, but the general range is between INR 5,000 and INR 10,000 per semester.",
    "Is there a hostel facility?": "No, Shyam Lal College does not offer hostel facilities.",
    "What extracurricular activities are available?": "The college offers societies in dance, music, photography, drama, and more.",
    "Who is the principal of Shyam Lal College?": "The principal is Prof. Rabi Narayan Kar.",
    "What are the library timings?": "The library is open from 9 AM to 5 PM on weekdays."
}

'''Simple NLP setup with spaCy'''
def preprocess_input(query):
    doc = nlp(query.lower())
    tokens = [token.text for token in doc if not token.is_stop and not token.is_punct]
    return tokens

def find_closest_match(query, faq_dict):
    processed_query = preprocess_input(query)
    possible_questions = faq_dict.keys()

    '''Finding the best match'''
    closest_match = difflib.get_close_matches(' '.join(processed_query), possible_questions, n=1, cutoff=0.4)
    return closest_match[0] if closest_match else None

'''Streamlit Frontend'''
def chatbot_interface():
    st.title("Shyam Lal College FAQ Chatbot")
    st.write("Ask me any question related to Shyam Lal College!")

    user_query = st.text_input("Your Question:", "")

    if user_query:
        closest_question = find_closest_match(user_query, faq)

        if closest_question:
            st.write(f"**Answer:** {faq[closest_question]}")
        else:
            st.write("Sorry, I don't have an answer for that right now.")

if __name__ == "__main__":
    chatbot_interface()


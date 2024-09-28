# import streamlit as st
# import google.generativeai as genai
# st.title("🐧 My chatbot app")
# st.subheader("Conversation")
# # Capture Gemini API Key
# gemini_api_key = st.text_input("Gemini API Key: ", placeholder="Type your API Key here...", type="password")
# # Initialize the Gemini Model
# if gemini_api_key:
#     try:
#         # Configure Gemini with the provided API Key
#         genai.configure(api_key=gemini_api_key)
#         model = genai.GenerativeModel("gemini-pro")
#         st.success("Gemini API Key successfully configured.")
#     except Exception as e:
#         st.error(f"An error occurred while setting up the Gemini model: {e}")
# # Initialize session state for storing chat history
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = [] # Initialize with an empty list
# # Display previous chat history using st.chat_message (if available)
# for role, message in st.session_state.chat_history:
#     st.chat_message(role).markdown(message)
# # Capture user input and generate bot response
# if user_input := st.chat_input("Type your message here..."):
#     # Store and display user message
#     st.session_state.chat_history.append(("user", user_input))
#     st.chat_message("user").markdown(user_input)
#     # Use Gemini AI to generate a bot response
#     if model:
#         try:
#             response = model.generate_content(user_input)
#             bot_response = response.text
#             # Store and display the bot response
#             st.session_state.chat_history.append(("assistant", bot_response))
#             st.chat_message("assistant").markdown(bot_response)
#         except Exception as e:
#             st.error(f"An error occurred while generating the response: {e}")
# AIzaSyAWt3fA070QHwo6EO90WFHipHgfSS3YY7Y


import streamlit as st
import google.generativeai as genai
 
st.title("Convert text to SQL chatbot app for life insurance")
st.subheader("Conversation")
 
# Capture Gemini API Key
gemini_api_key = st.text_input("Gemini API Key: ", placeholder="Type your API Key here...", type="password")
 
# Initialize the Gemini Model
if gemini_api_key:
    try:
        # Configure Gemini with the provided API Key
        genai.configure(api_key=gemini_api_key)
        model = genai.GenerativeModel("gemini-pro")
        st.success("Gemini API Key successfully configured.")
    except Exception as e:
        st.error(f"An error occurred while setting up the Gemini model: {e}")
 
# Initialize session state for storing chat history and prompt history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # Initialize with an empty list
 
if "prompt_chain" not in st.session_state:
    st.session_state.prompt_chain = "You act as a sql expert and have more business knowledge. \
        You are an sql developer expert that works for life insurance company. \
        You will help business user answer questions related to convert simple text to sql syntax. \
        If a question is unrelated to life insurance, you will explain who you are. \
        Please answer the following query in a friendly and informative way:"
 
# Display previous chat history using st.chat_message (if available)
for role, message in st.session_state.chat_history:
    st.chat_message(role).markdown(message)
 
# Capture user input and generate bot response
if user_input := st.chat_input("Type your message here..."):
    # Store and display user message
    st.session_state.chat_history.append(("user", user_input))
    st.chat_message("user").markdown(user_input)
   
    # Append the new question to the prompt chain
    st.session_state.prompt_chain += f"\nCustomer: {user_input}"
   
    # Combine the predefined prompt chain with the current user input
    full_input = st.session_state.prompt_chain
   
    # Use Gemini AI to generate a bot response
    if model:
        try:
            response = model.generate_content(full_input)
            bot_response = response.text
           
            # Append bot response to the chat history and update the prompt chain
            st.session_state.chat_history.append(("assistant", bot_response))
            st.chat_message("assistant").markdown(bot_response)
           
            # Update the prompt chain with the bot's response
            st.session_state.prompt_chain += f"\nAssistant: {bot_response}"
        except Exception as e:
            st.error(f"An error occurred while generating the response: {e}")
 


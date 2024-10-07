📧 Cold Mail Generator
The Cold Mail Generator is a tool designed for service companies to automate the process of crafting personalized cold emails. Utilizing Groq, Langchain, and Streamlit, this application allows users to input the URL of a company's careers page. The tool extracts job listings from that page and generates tailored cold emails, incorporating relevant portfolio links sourced from a vector database based on specific job descriptions.

Use Case Scenario
Imagine this scenario:

Nike is on the lookout for a Principal Software Engineer and is investing significant time and resources in the hiring process, including onboarding and training.
XYZ Company, a software development firm, can provide a dedicated software development engineer to meet Nike's needs. Consequently, the business development executive at XYZ Company reaches out to Nike via a cold email.


Features
Extracts job listings from a specified company's careers page.
Generates personalized cold emails tailored to the job descriptions.
Sources relevant portfolio links to enhance the email's impact.
Provides sentiment analysis of the generated emails to gauge their effectiveness.
Setup Instructions
1. Obtain an API Key:

First, acquire an API key from Groq Console.
Update the value of GROQ_API_KEY in the app/.env file with the API key you created.

2. Install Dependencies:

Ensure you have the required packages installed. Run the following command: pip install -r requirements.txt

3. Run the Streamlit App:

Start the application by executing: streamlit run app\main.py

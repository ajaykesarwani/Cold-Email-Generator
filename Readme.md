# 📧 Cold Mail Generator

Cold Mail Generator is a full‑stack AI tool that generates personalized cold emails for service companies. It:
- Scrapes a company’s careers page for job listings.
- Uses Groq + LangChain to generate tailored cold emails.
- Pulls relevant portfolio links from a vector database and performs sentiment analysis on the emails.

## Use Case Scenario

Imagine this scenario:  
Nike is on the lookout for a Principal Software Engineer and is investing significant time and resources in the hiring process, including onboarding and training.  
XYZ Company, a software development firm, can provide a dedicated software development engineer to meet Nike's needs. Consequently, the business development executive at XYZ Company reaches out to Nike via a cold email.

## ✨ Features

- Extracts job listings from a company’s careers page.
- Generates personalized cold emails tailored to each job description.
- Selects relevant portfolio links from a vector store for stronger outreach.
- Runs sentiment analysis on generated emails to gauge tone and effectiveness.

## 🛠 Tech Stack

- Language: Python  
- Framework: Streamlit  
- LLM & Orchestration: Groq, LangChain, RAG‑style retrieval  
- Data: Chroma / vector database for portfolio retrieval  
- Deployment: Vercel (Streamlit app)


## ⚙️ Setup Instructions

1. **Clone the repo**

   ```bash
   git clone https://github.com/ajaykesarwani/Cold-Email-Generator.git
   cd Cold-Email-Generator
   ```

2. **Create and fill `.env`**

   - Get an API key from Groq Console.
   - Create an `.env` file in the `app/` directory:
     ```env
     GROQ_API_KEY=your_key_here
     ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**

   ```bash
   streamlit run app/main.py
   ```

## 🧠 How it works

- Scrapes the careers page for job postings.
- Builds a job description context and queries a vector database of your portfolio items.
- Uses LangChain + Groq to generate a cold email that references the job and relevant portfolio links.
- Runs sentiment analysis on the final email and surfaces the score to the user.
  



🧠 Project Overview
This project demonstrates how to build an instruction-based AI agent using Gemini API (OpenAI-compatible) with Python. It includes secure API management using .env, dependency management with UV, and integration of the openai-agents package to build custom agent behavior.

🚀 Features
🔐 API key stored securely using .env

⚙️ Dependency management with UV

🤖 Custom agent setup using openai-agents

🧪 Instruction-tuning for agent behavior

🛡️ .env added to .gitignore to prevent exposure

📦 Requirements
Python 3.8+

UV package manager

Gemini API Key (from Google AI Studio)

🔧 Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Install UV (if not already)
bash
Copy
Edit
pip install uv
3. Install Required Packages
bash
Copy
Edit
uv add python-dotenv openai-agents
4. Create .env File
Create a file named .env in the root directory and add your Gemini API key:

ini
Copy
Edit
Api_Key=your_gemini_api_key_here
5. Make Sure .env is Ignored
Ensure .env is in your .gitignore file:

bash
Copy
Edit
.env
6. Run the Agent Script
bash
Copy
Edit
python main.py
🧪 Sample Output
Input:
"میں روز صبح جلدی اٹھتا ہوں۔پھر فجر کی نماز پڑھتا ہوں۔"

Output:
"I wake up early every morning. Then I offer the Fajr prayer."

📚 Technologies Used
Python

UV (UltraViolet)

python-dotenv

openai-agents

Gemini 2.0 Flash (via OpenAI-compatible endpoint)

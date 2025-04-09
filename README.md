



# 🤖 CS50 Final Project: AI Chatbot

This AI Chatbot is my final project submission for Harvard's CS50, showcasing practical knowledge in web development, API integration, and artificial intelligence. Built with Python, Flask, and Hugging Face's transformers library, it provides users with an interactive and responsive conversational experience.

## 🎬 YouTube Demonstration
[🎬 YouTube-Demo](https://youtu.be/OXY3JGi0H7Q)
A comprehensive video demonstration highlighting the chatbot’s functionality, interface, and backend implementation is available on YouTube. It visually walks you through the core features, user interactions, and explains technical aspects briefly to provide clarity and insight into how the chatbot operates.

## 🚀 Project Features

### User Interface
The frontend interface is crafted using modern web technologies such as HTML, CSS, and JavaScript. It provides a clean, intuitive, and user-friendly chat environment where users can seamlessly interact with the AI chatbot. The user interface features:
- A responsive chat window that adapts well to different screen sizes
- Instant message sending and real-time AI responses
- Clear visual distinction between user messages and chatbot responses

### Backend with Flask
The backend infrastructure is developed using Flask, a lightweight Python web framework. Flask efficiently manages the request-response cycle, ensuring smooth communication between the frontend interface and the backend AI model. Key backend functionalities include:
- Routing and handling HTTP requests
- Managing sessions to maintain conversation context
- Secure handling of sensitive data through environment variables stored in a `.env` file

### AI Model - DialoGPT
At the core of the chatbot lies the DialoGPT-small model, a powerful conversational AI developed by Microsoft. It is integrated using Hugging Face’s transformers library, allowing for advanced and context-aware responses to user inputs. The AI chatbot is capable of:
- Maintaining coherent and contextually relevant dialogues
- Providing engaging and human-like conversational experiences
- Handling diverse conversational topics and prompts effectively

### Persistent Chat History
Conversations are securely and persistently stored using SQLite, a lightweight relational database. This enables users to retain and review previous interactions seamlessly. The implementation ensures:
- Efficient storage and retrieval of conversation logs
- Ability to maintain context across multiple sessions
- Improved user engagement and experience by recalling past interactions

### Security
Security has been prioritized in the project through the following measures:
- Sensitive environment configurations, including API keys and database credentials, are protected via environment variables using the `.env` file
- Sanitization of user inputs to prevent common web vulnerabilities
- Secure handling of database interactions to mitigate SQL injection risks

### GitHub Integration
The project maintains a clean, structured, and organized GitHub repository. This structure allows for easy navigation and understanding of the project's components, facilitating collaboration and potential future development:
- Clear commit messages documenting changes and updates
- Comprehensive `requirements.txt` file for simplified dependency management
- Well-organized directories separating frontend, backend, and database logic clearly

## 🛠 Installation

To install and run this chatbot locally, follow the steps outlined below:

### Step 1: Clone Repository
```bash
git clone https://github.com/abduldercoder/cs50-final-chatbot.git
cd cs50-final-chatbot
```

### Step 2: Setup Virtual Environment
Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
Install all required packages:
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
Create a `.env` file in the root directory and add necessary configurations:
```bash
# Example:
SECRET_KEY='your-secret-key'
DATABASE_URL='sqlite:///chat_history.db'
```

### Step 5: Run the Application
Launch the Flask application:
```bash
flask run
```

Open your browser and navigate to `http://localhost:5000` to interact with the chatbot.

## 🎯 Motivation and Purpose
The motivation behind creating this AI chatbot was to consolidate and practically apply knowledge acquired through the CS50 course. It serves as a hands-on demonstration of integrating frontend development, backend frameworks, databases, and AI technologies into a cohesive project.

This chatbot provides an engaging way to interact with AI, explore how conversational agents work, and illustrate the possibilities and current limitations of chatbot technologies. It emphasizes the importance of user-centric design, data security, and efficient backend handling in modern web applications.

## 🚧 Challenges and Learnings
Throughout the development process, various challenges were encountered and overcome, providing valuable learning experiences:
- Understanding and implementing Hugging Face transformers for conversational AI
- Managing context across sessions effectively
- Ensuring secure handling and storage of data

This project significantly enhanced my practical skills in web development, AI model deployment, and comprehensive project management.

## 🌟 Future Improvements
While the current chatbot implementation fulfills its initial goals, future development could focus on:
- Enhancing AI responsiveness and accuracy with advanced fine-tuning
- Implementing user authentication and personalized experiences
- Improving UI/UX based on user feedback and interaction analytics

## 📄 License
This project is open-source, provided under the MIT License. Contributions, improvements, and feedback from the community are welcome.

---

Thank you for exploring my CS50 Final Project. Feel free to reach out or contribute to enhance the AI chatbot further!



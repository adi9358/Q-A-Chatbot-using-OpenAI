
# Q-A Chatbot using OpenAI

## Overview

This project is a Question-Answering chatbot powered by OpenAI's GPT models.  
It allows users to interact with an AI assistant that understands and answers queries in natural language via a simple web interface built with Streamlit.

---

## Features

- Interactive conversational AI chatbot  
- Uses OpenAI API for generating intelligent responses  
- Easy setup with Python and Streamlit  
- Supports real-time question answering  

---

## Getting Started

### Prerequisites

- Python 3.8 or higher  
- OpenAI API Key (get it from [OpenAI](https://platform.openai.com/account/api-keys))  

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/adi9358/Q-A-Chatbot-using-OpenAI.git
   cd Q-A-Chatbot-using-OpenAI
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

### Running the App

Run the chatbot app using Streamlit:
```bash
streamlit run app.py
```

Open your browser and go to [q-a-chatbot-openai.streamlit.app/) to chat with the bot.

---

## Project Structure

```
├── app.py           # Main app file (Streamlit)
├── requirements.txt # Python dependencies
├── .env             # Environment variables (API key)
├── README.md        # This file
└── utils.py         # Helper functions (if any)
```

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## License

This project is licensed under the MIT License.

---

## Author

Adi — [GitHub Profile](https://github.com/adi9358)

---

⭐ If you find this project helpful, please give it a star!

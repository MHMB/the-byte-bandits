# Streamlit Chatbot

This project is a simple and elegant chatbot interface built using Streamlit. It allows users to interact with a chatbot by sending messages and receiving responses in real-time.

## Project Structure

```
streamlit-chatbot
├── src
│   ├── app.py          # Main entry point for the Streamlit application
│   └── utils
│       └── chat_api.py # Functions for interacting with the chatbot API
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd streamlit-chatbot
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the Streamlit application, execute the following command in your terminal:
```
streamlit run src/app.py
```

This will start the Streamlit server and open the chatbot interface in your default web browser.

## Features

- User-friendly interface for chatting with the bot.
- Real-time message sending and receiving.
- Maintains the entire chat thread for user reference.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
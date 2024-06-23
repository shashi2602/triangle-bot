
# Twilio Chatbot

This Twilio chatbot offers a range of features designed to enhance user interaction and productivity. The key functionalities include:

## Features

1. **URL Content Summarization**
   - Summarizes the content of URLs using the Google Gemini API.

2. **Text Summarization**
   - Provides concise summaries of text inputs.

3. **Tweet Creation**
   - Generates tweets based on user inputs.

4. **Audio Notes**
   - Converts audio notes to text using OpenAI's Whisper.

5. **General Inquiry**
   - Allows users to ask any questions, similar to Brad AI.

## Technologies Used

- **Twilio API**: For messaging and chatbot interactions.
- **Google Gemini API**: For summarizing URL content.
- **OpenAI Whisper**: For converting audio notes to text.

## Getting Started

To get started with this project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/shashi2602/triangle-bot.git
   cd triangle-bot
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   - Configure your Twilio API credentials.
   - Set up API keys for Google Gemini and OpenAI Whisper.

4. **Run the chatbot**:
   ```bash
   python bot.py
   ```

## Usage

Once the chatbot is up and running, you can interact with it through your Twilio number. Here are some examples of what you can do:

- **Summarize a URL**: Send a URL to the chatbot, and it will return a summary of the content.
- **Summarize Text**: Input a block of text, and the chatbot will provide a summary.
- **Create a Tweet**: Provide a prompt, and the chatbot will generate a tweet.
- **Take an Audio Note**: Send an audio file, and the chatbot will convert it to text.
- **Ask Anything**: Ask any question, and the chatbot will respond similarly to Brad AI.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License.

---

Feel free to customize this template further according to your project's specifics.

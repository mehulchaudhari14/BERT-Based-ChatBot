<<<<<<< HEAD
# NLP Intent ChatBot with BERT

A sophisticated, web-based chatbot application that utilizes a fine-tuned BERT (Bidirectional Encoder Representations from Transformers) model to accurately predict user intents and provide contextually relevant responses. Featuring a premium, modern UI with glassmorphism aesthetics.

![ChatBot Preview](https://via.placeholder.com/800x450.png?text=BERT+Intent+ChatBot+Interface)

## 🚀 Features

- **BERT-Powered Intelligence**: Leveraging the state-of-the-art BERT model for high-accuracy intent classification.
- **CLINC150 Dataset Support**: Pre-trained to recognize over 150 distinct user intents across various domains (Banking, Travel, Kitchen, Utilities, etc.).
- **Modern Glassmorphism UI**: A sleek, responsive web interface built with modern CSS techniques, featuring smooth animations and a premium look.
- **Real-time Interaction**: Instant responses with realistic typing indicators and message timestamps.
- **Dynamic Response System**: Easily update or expand the bot's knowledge by modifying the `intents.json` file without restarting the server.
- **Lightweight Backend**: A clean Python-based server handling API requests and model predictions.

## 🛠️ Tech Stack

- **Backend**: Python 3.x
- **Model**: PyTorch, Transformers (BERT)
- **Frontend**: HTML5, Vanilla JavaScript, CSS3
- **Data Format**: JSON (for intents and responses)
- **Dataset**: [CLINC150](https://github.com/clinc/oos-eval)

## 📂 Project Structure

```text
.
├── app.py              # Python backend (HTTP Server & API)
├── app.js              # Frontend logic and API integration
├── index.html          # Main web interface
├── style.css           # Premium glassmorphism styling
├── intents.json        # Intent-to-response mapping data
├── optimizer.pt        # Fine-tuned BERT model weights (PyTorch)
├── requirements.txt    # Python dependencies
└── venv/               # Virtual environment (optional)
```

## 📥 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/nlp-chatbot-bert.git
   cd nlp-chatbot-bert
   ```

2. **Set up a Virtual Environment** (Recommended):
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare the Model**:
   Ensure you have the `optimizer.pt` (BERT model weights) in the root directory.

## 🏃 Usage

1. **Start the Backend Server**:
   ```bash
   python app.py
   ```
   The server will start at `http://127.0.0.1:8000`.

2. **Open the Interface**:
   Open `index.html` in your web browser. Alternatively, since the server serves static files, you can visit:
   ```text
   http://127.0.0.1:8000/
   ```

3. **Start Chatting**:
   Type messages like "What is my bank balance?", "Book a flight to London", or "Tell me a joke" to see the BERT model in action!

## 🧪 Intent Examples

The bot is trained on the CLINC150 dataset. You can try queries related to:
- **Banking**: balance, bill_due, transfer, credit_score
- **Travel**: book_flight, car_rental, travel_alert
- **Utilities**: alarm, weather, calculator, timer
- **Personal**: greeting, how_old_are_you, what_are_your_hobbies

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## ✍️ Developed By

- **Mehul Chaudhari**
- 📧 [mehulchaudhari140306@gmail.com](mailto:mehulchaudhari140306@gmail.com)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

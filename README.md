# Customer Support Chatbot

A powerful, AI-powered customer support chatbot built with Python, LangChain, and FastAPI. This chatbot uses Retrieval-Augmented Generation (RAG) to provide accurate, context-aware responses based on a knowledge base.

## 🚀 Features

- **AI-Powered Responses**: Uses OpenAI's GPT models for intelligent conversation
- **Knowledge Base Integration**: RAG system with ChromaDB vector database
- **Conversation Memory**: Maintains context across chat sessions
- **Web Interface**: Modern, responsive chat UI
- **REST API**: Full API for integration with other systems
- **Session Management**: Persistent conversation history
- **Source Attribution**: Shows sources used for responses
- **Confidence Scoring**: Indicates response confidence levels

## 🏗️ Architecture

```
├── app/
│   ├── __init__.py
│   ├── api.py              # FastAPI endpoints
│   ├── chatbot.py          # Core chatbot logic
│   ├── database.py         # Database models and operations
│   ├── knowledge_base.py   # Knowledge base management
│   └── models.py           # Pydantic models
├── static/
│   └── index.html          # Web interface
├── config.py               # Configuration settings
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
└── env.example            # Environment variables template
```

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd langchain-customer-support
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp env.example .env
   # Edit .env and add your OpenAI API key
   ```

5. **Initialize the application**
   ```bash
   python main.py
   ```

## ⚙️ Configuration

Create a `.env` file with the following variables:

```env
# OpenAI API Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Database Configuration
DATABASE_URL=sqlite:///./customer_support.db

# Vector Database Configuration
CHROMA_DB_PATH=./chroma_db

# Application Configuration
DEBUG=True
HOST=0.0.0.0
PORT=8000

# Model Configuration
MODEL_NAME=gpt-3.5-turbo
TEMPERATURE=0.7
MAX_TOKENS=1000
```

## 🚀 Usage

### Web Interface

1. Start the application: `python main.py`
2. Open your browser to: `http://localhost:8000`
3. Start chatting with the customer support assistant!

### API Endpoints

- **POST** `/api/chat` - Send a message and get response
- **GET** `/api/conversation/{session_id}` - Get conversation history
- **DELETE** `/api/conversation/{session_id}` - Clear conversation
- **POST** `/api/knowledge` - Add knowledge base item
- **GET** `/api/knowledge` - Get knowledge base items
- **GET** `/api/search` - Search knowledge base

### Example API Usage

```python
import requests

# Send a message
response = requests.post("http://localhost:8000/api/chat", json={
    "message": "How do I reset my password?",
    "session_id": "user123"
})

print(response.json())
```

## 📚 Knowledge Base

The chatbot comes with a pre-loaded knowledge base covering:

- **Account Management**: Password reset, security, account settings
- **Returns & Refunds**: Return policy, refund process
- **Payment Methods**: Accepted payment options
- **Shipping Information**: Delivery times, shipping options
- **Security**: Account protection, data privacy

### Adding Custom Knowledge

```python
# Via API
requests.post("http://localhost:8000/api/knowledge", json={
    "title": "Custom FAQ",
    "content": "Your custom content here...",
    "category": "custom",
    "tags": ["custom", "faq"]
})
```

## 🔧 Development

### Project Structure

- **`app/chatbot.py`**: Core chatbot logic with LangChain integration
- **`app/knowledge_base.py`**: Vector database management with ChromaDB
- **`app/database.py`**: SQLAlchemy models and database operations
- **`app/api.py`**: FastAPI endpoints and request handling
- **`static/index.html`**: Modern web interface with real-time chat

### Adding New Features

1. **Custom Prompts**: Modify the system prompt in `chatbot.py`
2. **New Knowledge Categories**: Add items via API or database
3. **Additional Endpoints**: Extend `api.py` with new routes
4. **UI Enhancements**: Modify `static/index.html`

## 🧪 Testing

```bash
# Run tests (when implemented)
pytest

# Test API endpoints
curl -X POST "http://localhost:8000/api/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello", "session_id": "test123"}'
```

## 🚀 Deployment

### Docker Deployment

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["python", "main.py"]
```

### Production Considerations

1. **Environment Variables**: Use proper secrets management
2. **Database**: Use PostgreSQL for production
3. **Vector Database**: Consider cloud vector databases
4. **CORS**: Configure CORS for your domain
5. **Rate Limiting**: Implement API rate limiting
6. **Monitoring**: Add logging and monitoring

## 📊 Monitoring

The application includes:

- Health check endpoints
- Conversation history tracking
- Response confidence scoring
- Source attribution for transparency

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

For support and questions:

1. Check the API documentation at `/api/docs`
2. Review the knowledge base
3. Open an issue on GitHub

## 🔮 Future Enhancements

- [ ] Multi-language support
- [ ] Voice chat integration
- [ ] Advanced analytics dashboard
- [ ] Integration with CRM systems
- [ ] Sentiment analysis
- [ ] Automated ticket creation
- [ ] Multi-channel support (email, SMS, social media)

---

**Built with ❤️ using LangChain, FastAPI, and OpenAI**
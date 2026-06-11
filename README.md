# Agentic AI Customer Support Assistant

This project is a simple AI-powered customer support assistant built with FastAPI, LangChain agents, custom tools, conversation memory, and Groq LLM.

It works like a support chat system where a user can ask about order status, support policies, product information, or request a support ticket. The backend handles the AI logic, and the frontend provides a clean chat interface for testing it in the browser.

## Features

- Customer support chatbot interface
- FastAPI backend
- LangChain agent with tool calling
- Groq LLM integration
- Conversation memory using session IDs
- Custom support tools for:
  - checking order status
  - getting return, refund, shipping, and warranty policies
  - creating mock support tickets
  - answering basic product information questions
- Simple frontend using HTML, CSS, and JavaScript
- REST API endpoints
- Docker support for backend deployment

## Project Structure

```text
Agentic-customer-support-assistent/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── agent_service.py       # LangChain agent setup and execution
│   │   ├── config.py              # Environment variable settings
│   │   ├── main.py                # FastAPI app entry point
│   │   ├── memory_store.py        # In-memory chat history
│   │   ├── routes.py              # API routes
│   │   ├── schemas.py             # Request and response models
│   │   └── support_tools.py       # Custom tools used by the agent
│   │
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── index.html                 # Chat UI
│   ├── script.js                  # Frontend API calls and chat handling
│   └── style.css                  # UI styling
│
├── .gitignore
└── README.md
```

## Requirements

Make sure you have the following installed:

- Python 3.10 or later
- pip
- A Groq API key
- A modern browser

## Backend Setup

Go to the backend folder:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

For Windows:

```bash
venv\Scripts\activate
```

For macOS or Linux:

```bash
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file inside the `backend` folder:

```env
GROQ_API_KEY="your_groq_api_key_here"
GROQ_MODEL=llama-3.1-8b-instant
ALLOWED_ORIGINS=http://localhost:5500,http://127.0.0.1:5500,http://localhost:8000
```

Do not upload your real `.env` file to GitHub. Keep API keys private and use a `.env.example` file for public repositories.

Start the backend server:

```bash
uvicorn app.main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

FastAPI docs will be available at:

```text
http://127.0.0.1:8000/docs
```

## Frontend Setup

Open a second terminal and go to the frontend folder:

```bash
cd frontend
```

Start a local frontend server:

```bash
python -m http.server 5500
```

Open this URL in your browser:

```text
http://localhost:5500
```

Now you can chat with the support assistant from the browser.

## How to Use

Try these sample messages in the chat box:

```text
Check status for ORD-1001
```

```text
What is your return policy?
```

```text
Create a support ticket for my damaged product
```

```text
Tell me about a laptop
```

The project uses mock support data, so it is useful for demos and learning. It is not connected to a real order database.

## Available Mock Orders

The project currently includes these sample order IDs:

```text
ORD-1001
ORD-1002
ORD-1003
```

You can update or add more orders inside:

```text
backend/app/support_tools.py
```

## Available Policy Names

The support policy tool supports these policy names:

```text
return_policy
refund_policy
shipping_policy
warranty_policy
```

These can also be edited in:

```text
backend/app/support_tools.py
```

## API Endpoints

### Root

```http
GET /
```

Returns a basic welcome message and available API paths.

### Health Check

```http
GET /api/health
```

Example response:

```json
{
  "status": "ok",
  "message": "Customer support assistant API is running"
}
```

### Send Chat Message

```http
POST /api/support/chat
```

Request body:

```json
{
  "message": "Check status for ORD-1001",
  "session_id": "default"
}
```

Response:

```json
{
  "response": "Order ORD-1001 is currently Shipped. Carrier: DHL. Estimated delivery: 2026-04-28.",
  "session_id": "default"
}
```

### Clear Chat Memory

```http
DELETE /api/support/chat/{session_id}
```

This clears the saved conversation history for the selected session.

## Docker Setup

You can also run the backend with Docker.

Go to the backend folder:

```bash
cd backend
```

Build the image:

```bash
docker build -t customer-support-assistant .
```

Run the container:

```bash
docker run --env-file .env -p 8000:8000 customer-support-assistant
```

The backend will be available at:

```text
http://localhost:8000
```

## Important Files

### `agent_service.py`

Sets up the LangChain tool-calling agent, connects it with Groq, and enables chat memory.

### `support_tools.py`

Contains the custom tools used by the agent. This is where mock orders, support policies, ticket creation, and product information are handled.

### `memory_store.py`

Stores conversation history in memory using session IDs.

### `script.js`

Connects the frontend chat box to the backend API and stores the session ID in browser local storage.

## Common Issues

### Backend is not starting

Make sure you are inside the `backend` folder and the virtual environment is activated.

Then install dependencies again:

```bash
pip install -r requirements.txt
```

### Groq API key error

Check that your `.env` file exists inside the `backend` folder and contains a valid `GROQ_API_KEY`.

### Frontend shows an error message

Make sure the backend server is running at:

```text
http://127.0.0.1:8000
```

Also check that the API URL in `frontend/script.js` is correct:

```javascript
const API_URL = "http://127.0.0.1:8000/api/support/chat";
```

### CORS error in browser console

Make sure your frontend URL is included in `ALLOWED_ORIGINS` inside `.env`.

Example:

```env
ALLOWED_ORIGINS=http://localhost:5500,http://127.0.0.1:5500,http://localhost:8000
```

### Order not found

Use one of the mock order IDs included in the project:

```text
ORD-1001
ORD-1002
ORD-1003
```

## Notes

- This project uses mock data for support tools.
- Chat memory is stored in memory, so it resets when the backend restarts.
- The frontend stores a session ID in browser local storage.
- For a production version, connect the tools with a real database, CRM, or ticketing system.
- Keep `.env` private and do not push real API keys to GitHub.

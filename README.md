# FastAPI Server with OpenAI Integration

A FastAPI server with OpenAI integration for generating reports and AI-powered features for decision support.

## 📋 Prerequisites

- Python 3.8+
- Git
- OpenAI API account (for API key)

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <https://github.com/FouadAE/make-decision-python-server.git>
cd make-decision-python-server
```

### 2. Create Virtual Environment

**macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory:

```bash
touch .env
```

Edit the `.env` file with your configuration:

```env
OPENAI_API_KEY=your_actual_openai_api_key_here
ENVIRONMENT=development
PORT=8000
HOST=0.0.0.0
```

**Important:** Get your OpenAI API key from [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)

## 🚀 Running the Application

### Development Mode (with auto-reload)

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Production Mode

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Using Environment Variables for Host/Port

```bash
uvicorn app.main:app --reload --host ${HOST:-0.0.0.0} --port ${PORT:-8000}
```

### API Documentation
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🧪 Testing the API

### Using curl
```bash
# Test root endpoint
curl http://localhost:8000/

# Test health check
curl http://localhost:8000/health

### Using Browser
- Open http://localhost:8000/docs for interactive API testing
- Or visit individual endpoints directly

## 🗂️ Project Structure

```
```bash
fastapi-server/
├── app/
│   └── router.py          # Main FastAPI application
│   └── prompt/          # directory for main files
│       └── schema.py          
│       └── service.py         
├── venv/                # Virtual environment (ignored by git)
├── .env                 # Environment variables (ignored by git)
├── .gitignore          # Git ignore rules
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🔧 Troubleshooting

### Common Issues

1. **"OPENAI_API_KEY not set" error**
   - Check if `.env` file exists in root directory
   - Verify API key is correctly formatted in `.env`
   - Restart the server after creating/modifying `.env`

2. **Module not found errors**
   - Ensure virtual environment is activated: `source venv/bin/activate`
   - Reinstall dependencies: `pip install -r requirements.txt`

3. **Port already in use**
   - Change port in `.env` file or use different port: `--port 8001`

4. **CORS issues**
   - Check if frontend URL is allowed in CORS settings (currently set to "*" for development)

### Debug Commands

```bash
# Check if environment variables are loaded
python -c "import os; print('API Key present:', bool(os.getenv('OPENAI_API_KEY')))"

# Check installed packages
pip list
```

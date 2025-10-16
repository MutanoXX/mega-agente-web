@echo off
echo 🤖 Starting Mega Agent - Pollinations.AI
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.8 or higher.
    pause
    exit /b 1
)

REM Check if virtual environment exists
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo 📥 Installing dependencies...
pip install -q -r requirements.txt

REM Start the backend server
echo.
echo 🚀 Starting Mega Agent...
echo.
echo ✅ Backend API: http://localhost:8000/api
echo ✅ Web Interface: http://localhost:8000
echo.
echo 📝 Open your browser and navigate to: http://localhost:8000
echo.
echo Press Ctrl+C to stop the server
echo.

cd backend
python main.py

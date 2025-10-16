#!/bin/bash

echo "🤖 Starting Mega Agent - Pollinations.AI"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -q -r requirements.txt

# Start the backend server
echo ""
echo "🚀 Starting Mega Agent..."
echo ""
echo "✅ Backend API: http://localhost:8000/api"
echo "✅ Web Interface: http://localhost:8000"
echo ""
echo "📝 Open your browser and navigate to: http://localhost:8000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

cd backend
python main.py

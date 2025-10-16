#!/usr/bin/env python3
"""
Mega Agent - Launcher Script
Inicia o backend e abre o navegador automaticamente
"""
import sys
import os
import subprocess
import time
import webbrowser
from pathlib import Path


def print_banner():
    """Print welcome banner"""
    print("\n" + "="*60)
    print("🤖  MEGA AGENT - Pollinations.AI")
    print("="*60 + "\n")


def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 ou superior é necessário!")
        print(f"   Versão atual: {sys.version}")
        sys.exit(1)
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detectado")


def check_dependencies(base_dir):
    """Check if required dependencies are installed"""
    print("\n📦 Verificando dependências...")
    
    # Check for minimum required packages
    try:
        import fastapi
        import uvicorn
        print("✅ Dependências principais instaladas")
        return
    except ImportError:
        pass
    
    # Install from requirements.txt
    req_file = base_dir / "requirements.txt"
    
    if not req_file.exists():
        print("❌ Arquivo requirements.txt não encontrado!")
        sys.exit(1)
    
    print("\n📥 Instalando dependências...")
    
    try:
        subprocess.check_call([
            sys.executable, 
            "-m", 
            "pip", 
            "install", 
            "-q",
            "-r", 
            str(req_file)
        ])
        print("✅ Dependências instaladas com sucesso!")
    except subprocess.CalledProcessError:
        print("❌ Erro ao instalar dependências!")
        print(f"   Execute manualmente: pip install -r {req_file}")
        sys.exit(1)


def check_backend_exists(base_dir):
    """Check if backend files exist"""
    backend_path = base_dir / "backend" / "main.py"
    if not backend_path.exists():
        print(f"❌ Arquivo {backend_path} não encontrado!")
        sys.exit(1)
    print("✅ Backend encontrado")


def check_frontend_exists(base_dir):
    """Check if frontend files exist"""
    frontend_path = base_dir / "frontend" / "index.html"
    if not frontend_path.exists():
        print(f"❌ Arquivo {frontend_path} não encontrado!")
        sys.exit(1)
    print("✅ Frontend encontrado")


def start_server(base_dir):
    """Start the FastAPI server"""
    print("\n🚀 Iniciando servidor...")
    print("\n" + "-"*60)
    print("📍 Backend API: http://localhost:8000/api")
    print("🌐 Interface Web: http://localhost:8000")
    print("-"*60)
    print("\n💡 Dica: Pressione Ctrl+C para parar o servidor\n")
    
    # Add base directory to Python path
    sys.path.insert(0, str(base_dir))
    
    # Start uvicorn server
    try:
        import uvicorn
        
        # Open browser after a short delay
        def open_browser():
            time.sleep(2)  # Wait for server to start
            print("\n🌐 Abrindo navegador...")
            webbrowser.open("http://localhost:8000")
        
        # Start browser opener in background
        import threading
        browser_thread = threading.Thread(target=open_browser, daemon=True)
        browser_thread.start()
        
        # Start server (using module path instead of chdir)
        uvicorn.run(
            "backend.main:app",
            host="127.0.0.1",  # Localhost only for security
            port=8000,
            log_level="info"
        )
        
    except KeyboardInterrupt:
        print("\n\n👋 Servidor encerrado. Até logo!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Erro ao iniciar servidor: {e}")
        sys.exit(1)


def main():
    """Main function"""
    try:
        # Get the directory where this script is located
        base_dir = Path(__file__).resolve().parent
        
        # Change to the base directory
        os.chdir(base_dir)
        
        print_banner()
        check_python_version()
        check_dependencies(base_dir)
        check_backend_exists(base_dir)
        check_frontend_exists(base_dir)
        start_server(base_dir)
        
    except KeyboardInterrupt:
        print("\n\n👋 Instalação cancelada. Até logo!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

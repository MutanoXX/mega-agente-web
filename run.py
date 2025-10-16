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


def check_dependencies():
    """Check if required dependencies are installed"""
    print("\n📦 Verificando dependências...")
    
    required_packages = [
        'fastapi',
        'uvicorn',
        'httpx',
        'pydantic',
        'aiofiles'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n⚠️  Pacotes faltando: {', '.join(missing_packages)}")
        print("\n📥 Instalando dependências...")
        
        try:
            subprocess.check_call([
                sys.executable, 
                "-m", 
                "pip", 
                "install", 
                "-q",
                "-r", 
                "requirements.txt"
            ])
            print("✅ Dependências instaladas com sucesso!")
        except subprocess.CalledProcessError:
            print("❌ Erro ao instalar dependências!")
            print("   Execute manualmente: pip install -r requirements.txt")
            sys.exit(1)
    else:
        print("✅ Todas as dependências estão instaladas")


def check_backend_exists():
    """Check if backend files exist"""
    backend_path = Path("backend/main.py")
    if not backend_path.exists():
        print("❌ Arquivo backend/main.py não encontrado!")
        sys.exit(1)
    print("✅ Backend encontrado")


def check_frontend_exists():
    """Check if frontend files exist"""
    frontend_path = Path("frontend/index.html")
    if not frontend_path.exists():
        print("❌ Arquivo frontend/index.html não encontrado!")
        sys.exit(1)
    print("✅ Frontend encontrado")


def start_server():
    """Start the FastAPI server"""
    print("\n🚀 Iniciando servidor...")
    print("\n" + "-"*60)
    print("📍 Backend API: http://localhost:8000/api")
    print("🌐 Interface Web: http://localhost:8000")
    print("-"*60)
    print("\n💡 Dica: Pressione Ctrl+C para parar o servidor\n")
    
    # Change to backend directory
    os.chdir("backend")
    
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
        
        # Start server
        uvicorn.run(
            "main:app",
            host="0.0.0.0",
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
        print_banner()
        check_python_version()
        check_dependencies()
        check_backend_exists()
        check_frontend_exists()
        start_server()
        
    except KeyboardInterrupt:
        print("\n\n👋 Instalação cancelada. Até logo!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

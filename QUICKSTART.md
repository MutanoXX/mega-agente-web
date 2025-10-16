# ⚡ Quick Start Guide - Mega Agent

Comece a usar o Mega Agent em menos de 5 minutos!

## 🚀 Instalação Rápida

### Opção 1: Arquivo Único (Mais Simples) ⭐

```bash
python run.py
```

**Isso faz tudo automaticamente:**
1. ✅ Verifica Python 3.8+
2. ✅ Instala dependências se necessário
3. ✅ Inicia o servidor
4. ✅ Abre o navegador automaticamente

**Pronto!** Você já está usando o Mega Agent! 🎉

### Opção 2: Scripts de Inicialização

**Linux/Mac:**
```bash
./start.sh
```

**Windows:**
```bash
start.bat
```

### Opção 3: Docker

```bash
docker-compose up
```

Acesse: `http://localhost:8000`

### Opção 4: Manual

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Iniciar servidor
cd backend
python main.py
```

Acesse: `http://localhost:8000`

## 🎯 Primeiros Passos

### 1. Teste Básico de Texto

Digite no chat:
```
Olá! Me explique o que você pode fazer.
```

**Resultado esperado:** O agente responde explicando suas capacidades.

### 2. Gere Sua Primeira Imagem

Digite no chat:
```
Crie uma imagem de um gato astronauta no espaço
```

**Resultado esperado:** Uma imagem é gerada e exibida no chat.

### 3. Faça uma Pesquisa

Digite no chat:
```
Pesquise as últimas notícias sobre inteligência artificial
```

**Resultado esperado:** O agente busca e retorna informações atualizadas.

### 4. Gere Áudio

Digite no chat:
```
Fale: Bem-vindo ao Mega Agent!
```

**Resultado esperado:** Um player de áudio aparece com a mensagem falada.

## ⚙️ Configuração Básica

### Selecionar Modelos

1. Olhe para a **barra lateral esquerda**
2. Escolha os modelos que deseja usar:
   - 💬 **Texto**: openai (recomendado)
   - 🔍 **Pesquisa**: searchgpt
   - 🧠 **Raciocínio**: openai-reasoning
   - 🎨 **Imagem**: flux (recomendado)
   - 🔊 **Voz**: nova (recomendado)

### Limpar Conversa

Clique no botão **🗑️ Limpar Conversa** na barra lateral.

## 💡 Dicas Rápidas

### Como o Agente Decide a Ferramenta?

O agente analisa sua mensagem automaticamente:

| Você escreve | Agente usa |
|--------------|------------|
| "crie uma imagem..." | 🎨 Geração de Imagem |
| "pesquise sobre..." | 🔍 Pesquisa Web |
| "fale..." | 🔊 Text-to-Speech |
| "pense sobre..." | 🧠 Raciocínio |
| Qualquer outra coisa | 💬 Texto Normal |

### Exemplos Rápidos

```
✅ "Crie uma imagem de um dragão"
✅ "Pesquise sobre Python"
✅ "Fale olá"
✅ "Explique machine learning"
✅ "Pense sobre o futuro da IA"
```

## 🔧 Solução de Problemas Rápida

### Backend não inicia?

```bash
# Verifique se a porta 8000 está livre
lsof -i :8000  # Mac/Linux
netstat -ano | findstr :8000  # Windows

# Se estiver ocupada, mate o processo ou mude a porta
```

### Frontend não conecta?

1. ✅ Backend está rodando? Acesse http://localhost:8000
2. ✅ Veja o console do navegador (F12) para erros
3. ✅ Tente recarregar a página

### Respostas lentas?

1. ✅ Use modelos "fast" nas configurações
2. ✅ Verifique sua conexão com internet
3. ✅ Primeira requisição pode ser mais lenta

## 📚 Próximos Passos

Agora que você já começou:

1. 📖 Leia o [README.md](README.md) completo
2. 🎯 Veja [EXAMPLES.md](EXAMPLES.md) para mais exemplos
3. 📘 Consulte [USAGE.md](USAGE.md) para guia detalhado
4. 🤝 Contribua! Veja [CONTRIBUTING.md](CONTRIBUTING.md)

## 🆘 Precisa de Ajuda?

- 📝 Abra uma [Issue no GitHub](../../issues)
- 💬 Veja a [Documentação Completa](README.md)
- 🌐 Visite [Pollinations.AI](https://pollinations.ai)

## 🎉 Pronto!

Você está pronto para usar o Mega Agent! Divirta-se explorando todas as funcionalidades! 🚀

---

**Tempo total:** ~5 minutos ⏱️
**Dificuldade:** Fácil 🟢
**Pré-requisitos:** Python 3.8+ ou Docker 🐳

# 📚 Guia de Uso - Mega Agent

## 🚀 Início Rápido

### Opção 1: Arquivo Único (Mais Simples) ⭐

```bash
python run.py
```

Isso inicia tudo automaticamente e abre o navegador!

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

### Opção 4: Manual

```bash
# Instalar dependências
pip install -r requirements.txt

# Iniciar servidor
cd backend
python main.py
```

**Acesse:** http://localhost:8000

## 💡 Exemplos de Uso

### 1. Geração de Texto 💬

**Conversação Normal:**
```
"Explique o que é machine learning de forma simples"
"Conte-me uma história sobre robôs"
"Qual é a diferença entre IA e ML?"
```

**Resultado:** O agente usa modelos de texto (OpenAI, Mistral, Claude) para gerar respostas conversacionais.

---

### 2. Geração de Imagens 🎨

**Palavras-chave:** imagem, desenhe, crie, picture, draw, foto, ilustração

**Exemplos:**
```
"Crie uma imagem de um gato astronauta no espaço"
"Desenhe uma paisagem futurista com carros voadores"
"Gere uma imagem de um dragão de fogo"
"Picture of a sunset over mountains"
```

**Modelos disponíveis:**
- **Flux** (padrão): Versátil, boa qualidade
- **Flux Realism**: Para imagens fotorrealistas
- **Flux Anime**: Estilo anime/mangá
- **Flux 3D**: Renderizações 3D
- **Turbo**: Geração rápida

---

### 3. Pesquisa Web 🔍

**Palavras-chave:** pesquise, busque, search, notícias, latest, o que está acontecendo

**Exemplos:**
```
"Pesquise as últimas notícias sobre inteligência artificial"
"Busque informações sobre o clima em São Paulo"
"Search for the latest AI developments"
"O que está acontecendo no mundo da tecnologia?"
```

**Resultado:** O agente usa SearchGPT para buscar informações atualizadas na web.

---

### 4. Text-to-Speech 🔊

**Palavras-chave:** fale, diga, áudio, voz, speak, say

**Exemplos:**
```
"Fale 'Bem-vindo ao Mega Agent'"
"Diga olá em voz alta"
"Speak this text: Hello world"
"Gere áudio dizendo bom dia"
```

**Vozes disponíveis:**
- **Nova** (padrão): Voz feminina amigável
- **Alloy**: Voz neutra
- **Echo**: Voz masculina
- **Fable**: Voz expressiva
- **Onyx**: Voz profunda
- **Shimmer**: Voz suave

---

### 5. Raciocínio Avançado 🧠

**Palavras-chave:** pense, raciocine, analise profundamente, think, complexo

**Exemplos:**
```
"Pense profundamente sobre as implicações éticas da IA"
"Raciocine sobre como resolver o problema da fome mundial"
"Analise profundamente os prós e contras da energia nuclear"
"Think about the future of quantum computing"
```

**Modelos disponíveis:**
- **O4 Mini**: Raciocínio especializado
- **OpenAI (GPT-5)**: Raciocínio geral avançado

---

## ⚙️ Configuração de Modelos

### Como Selecionar Modelos

1. Use a barra lateral esquerda
2. Escolha o modelo para cada categoria:
   - 💬 Texto
   - 🔍 Pesquisa
   - 🧠 Raciocínio
   - 🎨 Imagem
   - 🔊 Voz

3. Os modelos selecionados serão usados automaticamente quando o agente decidir usar aquela ferramenta

### Quando Usar Cada Modelo

#### Modelos de Texto

| Modelo | Quando Usar |
|--------|-------------|
| OpenAI (GPT-5 Mini) | Uso geral, melhor qualidade |
| OpenAI Fast (GPT-5 Nano) | Respostas rápidas |
| Mistral | Alternativa open-source |
| Claude | Respostas mais criativas |

#### Modelos de Imagem

| Modelo | Quando Usar |
|--------|-------------|
| Flux | Uso geral, versátil |
| Flux Realism | Fotos realistas |
| Flux Anime | Arte estilo anime |
| Flux 3D | Renderizações 3D |
| Turbo | Geração rápida |

---

## 🎯 Dicas e Truques

### 1. Seja Específico
```
❌ "Crie uma imagem"
✅ "Crie uma imagem de um castelo medieval ao pôr do sol com dragões voando"
```

### 2. Use Contexto
O agente mantém histórico da conversa, então você pode fazer perguntas de acompanhamento:
```
Você: "Explique o que é blockchain"
Agente: [explica blockchain]
Você: "E quais são suas aplicações práticas?"
```

### 3. Combine Ferramentas
```
"Pesquise sobre gatos e depois crie uma imagem de um gato baseado no que você encontrou"
```

### 4. Experimente Diferentes Modelos
Cada modelo tem suas forças. Experimente diferentes combinações para encontrar o que funciona melhor para você.

### 5. Use Comandos Claros para Áudio
Para text-to-speech, seja literal:
```
✅ "Fale: Olá, como vai?"
✅ "Diga exatamente: Bem-vindo"
```

---

## 🔧 Solução de Problemas

### Problema: Backend não inicia

**Solução:**
```bash
# Verifique se a porta 8000 está livre
lsof -i :8000  # Linux/Mac
netstat -ano | findstr :8000  # Windows

# Se estiver em uso, mate o processo ou mude a porta em backend/main.py
```

### Problema: Frontend não conecta ao backend

**Solução:**
1. Verifique se o backend está rodando em `http://localhost:8000`
2. Abra o console do navegador (F12) para ver erros
3. Verifique se há problemas de CORS

### Problema: Imagens não carregam

**Solução:**
- As imagens são geradas pela API do Pollinations.AI
- Verifique sua conexão com a internet
- Tente um prompt diferente

### Problema: Respostas lentas

**Solução:**
1. Use modelos "fast" para respostas mais rápidas
2. Verifique sua conexão com a internet
3. A primeira requisição pode ser mais lenta (cold start)

---

## 📊 Limitações

### Rate Limits
- **Tier Anônimo**: 15 segundos entre requisições
- Para limites maiores, registre-se em [auth.pollinations.ai](https://auth.pollinations.ai)

### Tamanho de Contexto
- O agente mantém as últimas 6 mensagens (3 trocas) no histórico
- Para conversas mais longas, o contexto antigo é descartado

### Funcionalidades em Desenvolvimento
- ❌ Speech-to-Text (transcrição de áudio)
- ❌ Análise de imagens (Vision)
- ❌ Histórico persistente

---

## 🎨 Personalização

### Modificar o Tema

Edite `frontend/styles.css`:

```css
:root {
    --bg-primary: #0a0a0a;      /* Fundo principal */
    --bg-secondary: #141414;     /* Fundo secundário */
    --text-primary: #ffffff;     /* Texto principal */
    --accent-primary: #ffffff;   /* Cor de destaque */
}
```

### Adicionar Novos Modelos

Edite `backend/agent.py`:

```python
TEXT_MODELS = ["openai", "mistral", "seu-novo-modelo"]
```

E atualize o frontend em `frontend/index.html`.

---

## 📝 API Reference

### POST /chat

**Request:**
```json
{
  "message": "Sua mensagem",
  "models": {
    "text": "openai",
    "search": "searchgpt",
    "reasoning": "openai-reasoning",
    "image": "flux",
    "audio": "nova"
  }
}
```

**Response:** Server-Sent Events (SSE)

**Event Types:**
- `tool_selection`: Ferramenta escolhida
- `status`: Status da operação
- `text_chunk`: Pedaço de texto (streaming)
- `image`: URL da imagem gerada
- `audio`: URL do áudio gerado
- `done`: Operação concluída
- `error`: Erro ocorreu

### GET /models

**Response:**
```json
{
  "text_models": ["openai", "mistral", ...],
  "search_models": ["searchgpt"],
  "reasoning_models": ["openai-reasoning", ...],
  "image_models": ["flux", "flux-realism", ...],
  "audio_voices": ["nova", "alloy", ...]
}
```

### POST /clear

Limpa o histórico da conversa.

**Response:**
```json
{
  "message": "Conversation history cleared"
}
```

---

## 🤝 Contribuindo

Veja [CONTRIBUTING.md](CONTRIBUTING.md) para detalhes sobre como contribuir.

---

## 📞 Suporte

- **Issues**: Abra uma issue no GitHub
- **Documentação**: Leia o [README.md](README.md)
- **API Pollinations**: [pollinations.ai](https://pollinations.ai)

---

Feito com ❤️ usando Pollinations.AI

# 🤖 Mega Agent - Pollinations.AI

Um agente de IA completo que utiliza todas as funcionalidades do Pollinations.AI com uma interface web moderna e intuitiva.

## ✨ Funcionalidades

### 🎯 Capacidades do Agente

- **💬 Geração de Texto**: Conversas inteligentes com múltiplos modelos (OpenAI GPT-5, Mistral, Claude)
- **🎨 Geração de Imagens**: Criação de imagens com vários estilos (Flux, Flux Realism, Flux Anime, Flux 3D, Turbo)
- **🔍 Pesquisa Web**: Busca em tempo real usando SearchGPT
- **🔊 Text-to-Speech**: Geração de áudio com 6 vozes diferentes
- **🧠 Raciocínio Avançado**: Modelos especializados para problemas complexos
- **👁️ Análise de Imagens**: Capacidade de visão (em desenvolvimento)
- **⚡ Streaming em Tempo Real**: Respostas progressivas via SSE

### 🎨 Interface Web

- **🌑 Tema Dark Moderno**: Design elegante com detalhes brancos
- **⚙️ Seleção de Modelos**: Escolha modelos específicos para cada tarefa
- **🎭 Animações Suaves**: Transições e efeitos visuais modernos
- **📱 Responsivo**: Funciona em desktop e mobile
- **🔄 Streaming Visual**: Veja as respostas sendo geradas em tempo real
- **🎯 Decisão Automática**: O agente escolhe a ferramenta certa automaticamente

## 🚀 Como Usar

### Pré-requisitos

- Python 3.8+

### Instalação e Execução

**Forma mais simples (recomendada):**

```bash
python run.py
```

Isso vai:
- ✅ Verificar e instalar dependências automaticamente
- ✅ Iniciar o servidor backend
- ✅ Abrir o navegador automaticamente em http://localhost:8000

**Formas alternativas:**

1. **Scripts de inicialização:**
```bash
./start.sh  # Linux/Mac
start.bat   # Windows
```

2. **Docker:**
```bash
docker-compose up
```

3. **Manual:**
```bash
pip install -r requirements.txt
cd backend
python main.py
```

Depois acesse: `http://localhost:8000`

## 📖 Como Funciona

### Decisão Automática de Ferramentas

O agente analisa sua mensagem e decide automaticamente qual ferramenta usar:

- **Palavras-chave para Imagens**: "imagem", "desenhe", "crie uma imagem", "picture", "draw"
- **Palavras-chave para Pesquisa**: "pesquise", "busque", "search", "notícias", "latest"
- **Palavras-chave para Áudio**: "fale", "diga", "áudio", "voz", "speak", "say"
- **Palavras-chave para Raciocínio**: "pense", "raciocine", "analise profundamente", "think"
- **Padrão**: Geração de texto normal

### Exemplos de Uso

```
💬 Texto: "Explique o que é inteligência artificial"
🎨 Imagem: "Crie uma imagem de um gato astronauta"
🔍 Pesquisa: "Pesquise as últimas notícias sobre IA"
🔊 Áudio: "Fale 'Olá, bem-vindo ao Mega Agent'"
🧠 Raciocínio: "Pense profundamente sobre o futuro da IA"
```

## 🎨 Personalização

### Modelos Disponíveis

#### Texto
- `openai` - GPT-5 Mini (padrão)
- `openai-fast` - GPT-5 Nano (mais rápido)
- `mistral` - Mistral AI
- `claude` - Claude (Anthropic)

#### Pesquisa
- `searchgpt` - Modelo de pesquisa web

#### Raciocínio
- `openai-reasoning` - O4 Mini
- `openai` - GPT-5 (raciocínio)

#### Imagem
- `flux` - Flux (padrão)
- `flux-realism` - Flux Realismo
- `flux-anime` - Flux Anime
- `flux-3d` - Flux 3D
- `turbo` - Turbo (rápido)

#### Vozes (Text-to-Speech)
- `nova` - Nova (padrão)
- `alloy` - Alloy
- `echo` - Echo
- `fable` - Fable
- `onyx` - Onyx
- `shimmer` - Shimmer

## 🏗️ Estrutura do Projeto

```
mega-agente-web/
├── backend/
│   ├── agent.py          # Lógica principal do agente
│   └── main.py           # API FastAPI
├── frontend/
│   ├── index.html        # Interface web
│   ├── styles.css        # Estilos (tema dark)
│   └── script.js         # Lógica do frontend
├── requirements.txt      # Dependências Python
└── README.md            # Este arquivo
```

## 🔧 API Endpoints

### POST /chat
Envia uma mensagem para o agente (streaming)

**Request:**
```json
{
  "message": "Sua mensagem aqui",
  "models": {
    "text": "openai",
    "search": "searchgpt",
    "reasoning": "openai-reasoning",
    "image": "flux",
    "audio": "nova"
  }
}
```

**Response:** Server-Sent Events (SSE) stream

### GET /models
Retorna todos os modelos disponíveis

### POST /clear
Limpa o histórico da conversa

## 🎯 Recursos Futuros

- [ ] Suporte para Speech-to-Text (transcrição de áudio)
- [ ] Análise de imagens (Vision)
- [ ] Histórico de conversas persistente
- [ ] Exportação de conversas
- [ ] Temas personalizáveis
- [ ] Suporte para múltiplas conversas simultâneas
- [ ] Integração com mais modelos

## 📝 Licença

Este projeto usa a API do Pollinations.AI, que é open-source sob a licença MIT.

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## 🙏 Agradecimentos

- [Pollinations.AI](https://pollinations.ai) - Por fornecer a API incrível
- Comunidade open-source

---

Feito com ❤️ usando Pollinations.AI

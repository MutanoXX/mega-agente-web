# 🤝 Contribuindo para o Mega Agent

Obrigado por considerar contribuir para o Mega Agent! Este documento fornece diretrizes para contribuições.

## 📋 Código de Conduta

- Seja respeitoso e inclusivo
- Aceite críticas construtivas
- Foque no que é melhor para a comunidade
- Mostre empatia com outros membros da comunidade

## 🚀 Como Contribuir

### Reportando Bugs

1. **Verifique se o bug já foi reportado** nas Issues
2. **Crie uma nova Issue** com:
   - Título claro e descritivo
   - Passos para reproduzir o problema
   - Comportamento esperado vs. atual
   - Screenshots (se aplicável)
   - Informações do sistema (OS, Python version, etc.)

### Sugerindo Melhorias

1. **Verifique se a sugestão já existe** nas Issues
2. **Crie uma nova Issue** com:
   - Título claro e descritivo
   - Descrição detalhada da melhoria
   - Exemplos de uso (se aplicável)
   - Benefícios da implementação

### Pull Requests

1. **Fork o repositório**
2. **Crie uma branch** para sua feature:
   ```bash
   git checkout -b feature/nome-da-feature
   ```
3. **Faça suas alterações**
4. **Teste suas alterações**
5. **Commit suas mudanças**:
   ```bash
   git commit -m "feat: adiciona nova funcionalidade X"
   ```
6. **Push para sua branch**:
   ```bash
   git push origin feature/nome-da-feature
   ```
7. **Abra um Pull Request**

## 📝 Padrões de Código

### Python (Backend)

- Use **PEP 8** para estilo de código
- Use **type hints** quando possível
- Docstrings para funções e classes
- Mantenha funções pequenas e focadas

**Exemplo:**
```python
async def generate_text_stream(
    self,
    prompt: str,
    model: str = "openai",
    system_prompt: Optional[str] = None,
    temperature: float = 0.7
) -> AsyncGenerator[str, None]:
    """
    Generate text with streaming using Pollinations.AI
    
    Args:
        prompt: User prompt
        model: Model to use
        system_prompt: Optional system prompt
        temperature: Temperature for generation
        
    Yields:
        Text chunks as they are generated
    """
    # Implementation
```

### JavaScript (Frontend)

- Use **camelCase** para variáveis e funções
- Use **const** por padrão, **let** quando necessário
- Adicione comentários para lógica complexa
- Mantenha funções pequenas e focadas

**Exemplo:**
```javascript
/**
 * Process SSE stream from the API
 * @param {Response} response - Fetch response object
 */
async function processStream(response) {
    // Implementation
}
```

### CSS

- Use **kebab-case** para classes
- Organize por componentes
- Use variáveis CSS para cores e valores reutilizáveis
- Adicione comentários para seções

**Exemplo:**
```css
/* Chat Container Styles */
.chat-container {
    flex: 1;
    display: flex;
    flex-direction: column;
}
```

## 🧪 Testes

### Backend

```bash
# Instalar dependências de teste
pip install pytest pytest-asyncio

# Rodar testes
pytest
```

### Frontend

```bash
# Abrir no navegador e testar manualmente
# Verificar console para erros
```

## 📦 Estrutura de Commits

Use [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` Nova funcionalidade
- `fix:` Correção de bug
- `docs:` Mudanças na documentação
- `style:` Formatação, ponto e vírgula, etc.
- `refactor:` Refatoração de código
- `test:` Adição de testes
- `chore:` Manutenção

**Exemplos:**
```
feat: adiciona suporte para análise de imagens
fix: corrige erro no streaming de texto
docs: atualiza README com novos exemplos
style: formata código seguindo PEP 8
refactor: simplifica lógica de seleção de ferramentas
test: adiciona testes para geração de imagens
chore: atualiza dependências
```

## 🎯 Áreas para Contribuição

### Alta Prioridade

- [ ] Implementar Speech-to-Text
- [ ] Implementar análise de imagens (Vision)
- [ ] Adicionar testes automatizados
- [ ] Melhorar tratamento de erros
- [ ] Adicionar histórico persistente

### Média Prioridade

- [ ] Suporte para múltiplas conversas
- [ ] Exportação de conversas
- [ ] Temas personalizáveis
- [ ] Melhorias de performance
- [ ] Internacionalização (i18n)

### Baixa Prioridade

- [ ] Integração com mais modelos
- [ ] Plugins/extensões
- [ ] Mobile app
- [ ] Desktop app (Electron)

## 🔍 Revisão de Código

Todos os PRs passarão por revisão. Esperamos:

- Código limpo e bem documentado
- Testes (quando aplicável)
- Documentação atualizada
- Sem breaking changes (ou bem justificados)

## 📚 Recursos

- [Pollinations.AI API Docs](https://github.com/pollinations/pollinations/blob/master/APIDOCS.md)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [MDN Web Docs](https://developer.mozilla.org/)

## 💬 Comunicação

- **Issues**: Para bugs e sugestões
- **Discussions**: Para perguntas e discussões gerais
- **Pull Requests**: Para contribuições de código

## 🙏 Agradecimentos

Obrigado por contribuir para tornar o Mega Agent melhor! Cada contribuição, grande ou pequena, é valiosa.

---

**Dúvidas?** Abra uma Issue ou Discussion!

# RAG Assistant

A Retrieval-Augmented Generation (RAG) system built in progressive phases, from a pure Python implementation to a production-ready framework-based solution.
## Chatgpt prompt history 

https://chatgpt.com/share/6abe34c4-6c98-83e8-80f2-7e83e02c2b95

## Project Structure

```
rag-assistant/
├── app/
│   ├── config.py              # Configuration management
│   ├── main.py                # Application entry point
│   │
│   ├── ingestion/             # Document ingestion pipeline
│   │   ├── loader.py          # PDF/document loading
│   │   ├── chunker.py         # Text chunking strategies
│   │   └── pipeline.py        # Ingestion orchestration
│   │
│   ├── embeddings/            # Embedding generation
│   │   └── embedder.py        # Embedding model interface
│   │
│   ├── vectorstore/           # Vector database operations
│   │   └── store.py           # Vector store abstraction
│   │
│   ├── retrieval/             # Document retrieval
│   │   └── retriever.py       # Similarity search & retrieval
│   │
│   ├── llm/                   # LLM integration
│   │   └── ollama.py          # Ollama client wrapper
│   │
│   └── rag/                   # RAG pipeline
│       └── pipeline.py        # End-to-end RAG orchestration
│
├── documents/                 # Source documents (input)
├── data/                      # Processed data & indexes
├── tests/                     # Test suite
├── .env                       # Environment variables
├── requirements.txt           # Python dependencies
└── README.md
```

## Development Phases

### Phase 1 — Pure Python RAG (Current)
**Goal**: Build a working RAG pipeline from scratch using only core Python libraries.

| Component | Status | Description |
|-----------|--------|-------------|
| Project Structure | ✅ | Modular package layout |
| PDF Extraction | 🔄 | Text extraction from PDFs |
| Text Cleaning | ⏳ | Normalize, remove artifacts |
| Chunking | ⏳ | Semantic/fixed-size chunking |
| Embeddings | ⏳ | Vector representations via Ollama |
| Vector Storage | ⏳ | In-memory / file-based index |
| Similarity Search | ⏳ | Cosine similarity retrieval |
| Prompt Construction | ⏳ | Context-aware prompt templates |
| Ollama LLM | ⏳ | Local LLM inference |
| RAG Response | ⏳ | End-to-end answer generation |

### Phase 1 - workflow 
                 PDF
                  │
                  ▼
             PDF Loader
                  │
                  ▼
                Text
                  │
                  ▼
              Chunking
                  │
                  ▼
             ┌─────────┐
             │ Chunks  │
             └────┬────┘
                  │
                  ▼
             Embeddings
                  │
                  ▼
             Vector Store
                  │
                  │
User Question ────┤
                  ▼
            Query Embedding
                  │
                  ▼
          Cosine Similarity
                  │
                  ▼
             Top K Chunks

### Phase 2 — Production API
**Goal**: Expose the RAG system as a robust REST API.

- [ ] FastAPI application with async support
- [ ] `POST /upload` — Document ingestion endpoint
- [ ] `POST /chat` — Query endpoint with streaming
- [ ] Pydantic request/response models
- [ ] Global error handling & validation
- [ ] Structured logging (JSON)
- [ ] Configuration via environment variables
- [ ] Document IDs & metadata tracking

### Phase 3 — Production Improvements
**Goal**: Harden the system for real-world usage.

- [ ] Advanced chunking (semantic, recursive, markdown-aware)
- [ ] Metadata filtering (source, date, tags)
- [ ] Hybrid retrieval (BM25 + vector)
- [ ] Cross-encoder reranking
- [ ] Conversation history / multi-turn chat
- [ ] Citations & source attribution
- [ ] Response caching (Redis)
- [ ] Evaluation harness (RAGAS, custom metrics)
- [ ] Security (auth, rate limiting, input sanitization)
- [ ] Docker & Docker Compose
- [ ] PostgreSQL + pgvector for persistence
- [ ] Redis for caching & session management

### Phase 4 — Framework Migration
**Goal**: Rebuild using industry-standard frameworks for maintainability.

```
Pure Python  →  LangChain  →  LangGraph
     ↓              ↓            ↓
  Custom        Abstractions   Stateful,
  Components    & Chains       Multi-agent
```

Each migration step maintains feature parity while reducing boilerplate and adding ecosystem integrations.

## Getting Started

### Prerequisites
- Python 3.10+
- [Ollama](https://ollama.ai) running locally
- `uv` or `pip` for dependency management

### Installation

```bash
# Clone and enter project
cd rag-assistant

# Create virtual environment
python -m venv .venv && source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Pull required Ollama models
ollama pull llama3.1
ollama pull nomic-embed-text
```

### Configuration

Copy `.env.example` to `.env` and adjust:

```bash
cp .env.example .env
```

Key variables:
| Variable | Description | Default |
|----------|-------------|---------|
| `OLLAMA_BASE_URL` | Ollama server URL | `http://localhost:11434` |
| `EMBEDDING_MODEL` | Embedding model name | `nomic-embed-text` |
| `LLM_MODEL` | Generation model name | `llama3.1` |
| `CHUNK_SIZE` | Token chunk size | `512` |
| `CHUNK_OVERLAP` | Chunk overlap tokens | `50` |
| `TOP_K` | Retrieval count | `4` |

### Running (Phase 1)

```bash
# Ingest documents
python -m app.ingestion.pipeline --input documents/

# Query the system
python -m app.rag.pipeline --query "Your question here"
```

## Testing

```bash
# Run all tests
pytest

# With coverage
pytest --cov=app --cov-report=term-missing
```

## Roadmap

See [PROJECT_PLAN.md](PROJECT_PLAN.md) for detailed milestones, task breakdown, and acceptance criteria per phase.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/xyz`)
3. Commit changes (`git commit -am 'Add xyz'`)
4. Push to branch (`git push origin feature/xyz`)
5. Open a Pull Request

## License

MIT License — see [LICENSE](LICENSE) for details.
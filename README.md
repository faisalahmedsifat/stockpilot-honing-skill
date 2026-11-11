# StockPilot

Inventory, procurement, and fulfillment operations for wholesale distributors.

StockPilot is an interview-preparation engineering project built around a realistic business workflow: product availability, purchasing, goods receiving, stock reservations, and order fulfillment.

## Project status

Scaffold only. Business logic and feature implementations are intentionally left to the developer.

## Planned stack

- Frontend: React, TypeScript, Vite, TanStack Query, Zustand
- Backend: Python, FastAPI, Pydantic, SQLAlchemy, Alembic
- Data: PostgreSQL, Redis
- Background work: Celery
- AI retrieval: Qdrant and an embeddings provider
- Quality: pytest, Vitest, React Testing Library
- Delivery: Docker Compose and GitHub Actions

## Repository layout

- `backend/`: FastAPI application, domain layers, workers, migrations, and tests
- `frontend/`: React application organized by business feature
- `infra/`: local infrastructure and deployment configuration
- `docs/`: product, architecture, API, and engineering decision documents
- `scripts/`: developer and maintenance scripts

## Getting started

Implementation instructions will be added as the services are built. Copy `.env.example` to `.env` and fill in local values before starting infrastructure.

## Engineering principles

1. Keep the backend a modular monolith; run API and workers as separate processes.
2. Treat inventory movements as an auditable ledger.
3. Enforce organization and role authorization in the backend.
4. Protect stock reservation and receiving workflows with database transactions.
5. Keep external side effects out of database transaction boundaries where possible.
6. Add tests for business invariants before adding UI polish.

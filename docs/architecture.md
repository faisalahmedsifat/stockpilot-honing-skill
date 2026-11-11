# Architecture

## Initial shape

StockPilot is planned as a modular monolith with independently runnable processes: React web client, FastAPI application, Celery worker, PostgreSQL, Redis, and Qdrant for later AI/retrieval capability.

## Backend module boundaries

- `api/`: HTTP routes and dependency wiring
- `core/`: settings, security primitives, and application configuration
- `models/`: persistence models
- `schemas/`: request and response contracts
- `repositories/`: database access
- `services/`: business workflows and rules
- `workers/`: asynchronous task definitions
- `websocket/`: real-time connections and event delivery
- `ai/`: document ingestion, retrieval, and grounded assistant workflows
- `concurrency_lab/`: isolated I/O-bound and CPU-bound experiments

## Key design questions

1. Inventory ledger versus materialized balance strategy
2. Reservation expiry and release semantics
3. Transaction isolation and row-locking strategy
4. Idempotency key scope and persistence
5. Outbox pattern for reliable event publication
6. Tenant isolation strategy for relational and vector data
7. Permission model and approval thresholds

Document decisions and trade-offs as implementation progresses.

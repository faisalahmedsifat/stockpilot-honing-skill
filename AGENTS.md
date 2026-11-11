# Repository Guidance

## Project intent

Build StockPilot as a realistic, maintainable inventory and procurement platform. This repository is currently a scaffold; do not assume planned modules are implemented.

## Architecture

- Use a modular monolith for the backend.
- Keep HTTP routing, application services, persistence, domain models, and background tasks separated.
- Run the API and Celery workers as separate processes.
- Organize frontend code by business feature.
- Keep business rules out of React components and HTTP route handlers.

## Engineering constraints

- Enforce tenant scope and authorization in backend services and queries.
- Model inventory changes as auditable movements.
- Use database transactions and appropriate row-level locking for stock reservations and receiving.
- Make retriable commands idempotent.
- Validate external input at system boundaries.
- Never commit secrets or real environment files.
- Add tests for business invariants and authorization boundaries.

## Working practices

- Update documentation when architecture or API contracts change.
- Prefer focused changes and meaningful commits.
- Do not add infrastructure or dependencies without a concrete use case.
- Keep the README honest about what is implemented versus planned.

.PHONY: infra-up infra-down infra-logs backend-test backend-lint

infra-up:
	docker compose up -d postgres redis

infra-down:
	docker compose down

infra-logs:
	docker compose logs -f

backend-test:
	cd backend && python -m pytest

backend-lint:
	cd backend && ruff check .

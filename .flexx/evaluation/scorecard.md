# StockPilot scorecard

Last updated: 2026-11-12

## Current task

| Task | Score | Confidence | Status |
|---|---:|---|---|
| Phase 1: Backend application factory and configuration | 7.8/10 | Medium | Four tests pass from the repository root; Ruff passes; `.env.example` still contains an unsupported `APP_ENV=local` |

### Breakdown

| Dimension | Score | Evidence |
|---|---:|---|
| Correctness | 8/10 | Settings class, environment loading, cached accessor, factory, and health routes work when supplied a supported `APP_ENV`. |
| Design | 8/10 | Settings are separated from app construction; factory returns a FastAPI instance. |
| Code quality | 8/10 | `main.py` is now clean and Ruff reports no issues. |
| Testing | 9/10 | All four tests pass from the repository root using the project Python 3.13 environment. |
| Engineering judgment | 8/10 | Identified the configuration-contract mismatch, corrected the local `.env`, added `httpx2`, and explicitly configured pytest-asyncio in the backend project config. |

**Overall: 7.8/10.** This is a provisional score for the current task, not an overall skill rating.

### Evidence and remaining closure criteria

- [x] Settings override test added using pytest's `monkeypatch` fixture.
- [x] Four tests pass when a valid environment value is supplied.
- [x] Root cause of collection-time Pydantic `ValidationError` identified: `.env` and `.env.example` use `APP_ENV=local`, while `Settings.app_env` accepts only `development`, `testing`, or `production`.
- [x] Change local `.env` to `APP_ENV=development`; repository-root test run passes.
- [ ] Change `.env.example` from `APP_ENV=local` to `APP_ENV=development`.
- [x] Remove stale TODO comments and outdated module docstring; Ruff passes.
- [x] Add explicit `asyncio_default_fixture_loop_scope = "function"` to backend pytest configuration. (It applies when pytest is run with `backend/` as its config root.)
- [x] Re-run tests and Ruff after cleanup: 4 passed; Ruff clean.

No points are awarded for commands or tools merely being present; the implementation and its behavior are what count.

## Gamification

- Task completion: 100 XP (award only after closure criteria are met).
- Passing tests: 50 XP (awarded for this task's four passing tests).
- Explaining design: 25 XP (award after the user explains the key decisions independently).
- Independently identifying/fixing a bug: 25 XP (award when demonstrated without being handed the fix).
- Difficult edge case: 50 XP.
- Current verified XP earned: 50 XP.
- Streak: 0 fully closed tasks; verification streak starts after a task is closed end-to-end.

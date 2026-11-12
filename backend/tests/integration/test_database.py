import pytest

from sqlalchemy import text

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db


@pytest.mark.integration
async def test_get_db_yields_working_session():
    async for session in get_db():
        result = await session.execute(text("SELECT 1"))
        assert result.scalar_one() == 1

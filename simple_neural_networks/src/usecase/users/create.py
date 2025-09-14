from sqlalchemy.ext.asyncio import AsyncSession
from src.usecase.base import Usecase
from src.infra.postgres.gateways.base import CreateGate
from src.application.schemas.users import CreateUserSchem
from src.infra.postgres.tables import UserModel
from dataclasses import dataclass

@dataclass(slots=True, frozen=True, kw_only=True)
class CreateUserUsecase(Usecase[None, None]):
    session: AsyncSession
    
    async def __call__(self, ) -> None:
        pass

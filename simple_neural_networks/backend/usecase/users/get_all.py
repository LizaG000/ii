from sqlalchemy.ext.asyncio import AsyncSession
from backend.usecase.base import Usecase
from backend.infra.postgres.gateways.base import GetAllGate
from backend.application.schemas.users import UserSchemas
from backend.infra.postgres.tables import UserModel
from dataclasses import dataclass

@dataclass(slots=True, frozen=True, kw_only=True)
class GetUsersUsecase(Usecase[None, list[UserSchemas]]):
    session: AsyncSession
    get_users: GetAllGate[UserModel, UserSchemas]
    
    async def __call__(self) -> list[UserSchemas]:
        async with self.session.begin():
            return await self.get_users()

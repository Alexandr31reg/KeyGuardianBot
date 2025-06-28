from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs


engine = create_async_engine(url='sqlite+aiosqlite:///keyguardian.db',
                             echo=True)

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    name: Mapped[str] = mapped_column(String(25), nullable=True)
    passphrase: Mapped[str] = mapped_column(String, nullable=True)

class Key_Base(Base):
    __tablename__ = 'key_base'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(ForeignKey('users.tg_id'))
    name: Mapped[str] = mapped_column(String(25), nullable=True)
    login: Mapped[str] = mapped_column(String(50), nullable=True)
    password: Mapped[str] = mapped_column(String, nullable=True)


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
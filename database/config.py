import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()
DATABASE_URL=os.getenv("DATABASE_URL")

engine = create_async_engine(
    DATABASE_URL, 
    echo=True,
    pool_size=5, # até 5 conexões simultâneas
    max_overflow=10, # permite até 10 conexões extras além do pool_size
    pool_timeout=30, # tempo máximo de espera para obter uma conexão do pool    
    pool_recycle=1800 # tempo em segundos para reciclagem de conexões(30 min)
)

sessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False
) 
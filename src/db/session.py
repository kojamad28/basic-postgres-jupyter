from pathlib import Path

from dotenv import dotenv_values
from sqlalchemy import URL, create_engine
from sqlalchemy.engine import Engine


BASE_DIR = Path(__file__).resolve().parent.parent

def get_engine(dotenv_path: str = BASE_DIR / "db" / ".env") -> Engine:
    """
    Create sqlalchemy.engine.Engine for PostgreSQL database.

    Parameters
    ----------
    dotenv_path : str, default BASE_DIR / "db" / ".env"
        The path for dotenv file.
        Used as a parameter for dotenv.dotenv_values method.

    returns
    -------
    engine : sqlalchemy.engine.Engine
    """

    config: dict = dotenv_values(dotenv_path)

    url_object: URL = URL.create(
        "postgresql+psycopg",
        username=config["POSTGRES_USER"],
        password=config["POSTGRES_PASSWORD"],  # plain (unescaped) text
        host=config.get("POSTGRES_HOST", "postgres"),
        port=config.get("POSTGRES_PORT", "5432"),
        database=config.get("POSTGRES_DB", "postgres"),
        query={"options": f"-c search_path={config.get('POSTGRES_SCHEMA', 'public')}"},
    )

    engine = create_engine(url_object)
    return engine

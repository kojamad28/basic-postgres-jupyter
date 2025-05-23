from dotenv import dotenv_values
from sqlalchemy import URL, create_engine
from sqlalchemy.engine import Engine


def create_postgres_engine(env_file: str = ".env") -> Engine:
    """
    Create sqlalchemy.engine.Engine for PostgreSQL database.

    Parameters
    ----------
    env_file : str, default ".env"
        The env file name.
        Used as a parameter for dotenv.dotenv_values method.

    returns
    -------
    engine : sqlalchemy.engine.Engine
    """

    config: dict = dotenv_values(env_file)

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

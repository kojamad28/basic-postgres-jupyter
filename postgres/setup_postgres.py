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

    url_object: str = URL.create(
        "postgresql+psycopg",
        username=config["POSTGRES_USER"],
        password=config["POSTGRES_PASSWORD"],  # plain (unescaped) text
        host=config["POSTGRES_HOST"],
        port=config["POSTGRES_PORT"],
        database=config["POSTGRES_DB"],
        query={"options": f"-c search_path={config['POSTGRES_SCHEMA']}"},
    )

    engine = create_engine(url_object)
    return engine

# from alembic import context
# from sqlalchemy import engine_from_config, pool
# from models import Base  # Make sure models are imported

# config = context.config
# target_metadata = Base.metadata  # This should match your models' Base.metadata

# def run_migrations_online():
#     connectable = engine_from_config(
#         config.get_section(config.config_ini_section),
#         prefix="sqlalchemy.",
#         poolclass=pool.NullPool,
#     )

#     with connectable.connect() as connection:
#         context.configure(
#             connection=connection,
#             target_metadata=target_metadata
#         )

#         with context.begin_transaction():
#             context.run_migrations()

# run_migrations_online()


import os
from alembic import context
from sqlalchemy import create_engine
from logging.config import fileConfig

config = context.config
fileConfig(config.config_file_name)

database_url = os.getenv("DATABASE_URL", "sqlite:///./test_db.sqlite")
config.set_main_option("sqlalchemy.url", database_url)

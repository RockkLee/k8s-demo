import asyncio
import os
import importlib.util

from k8s_demo_fastapi.orm.models.base import Base
from k8s_demo_fastapi.orm.connection import engine
from k8s_demo_fastapi.orm.models import get_models_dir


def __import_all_modules_from_dir(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]
            module_path = os.path.join(directory, filename)

            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            globals()[module_name] = module


if __name__ == "__main__":
    # import all models
    current_directory = get_models_dir()
    __import_all_modules_from_dir(current_directory)

    async def init_models():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    asyncio.run(init_models())


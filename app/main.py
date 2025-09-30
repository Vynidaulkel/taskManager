from fastapi import FastAPI
import app.models as models
import app.database as database
import app.routes as routes


models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Task Manager API")

app.include_router(routes.router)

from fastapi import FastAPI
from api.user_routers import router as router_api_user
#from api.teacher_routers import router as router_api_user

app = FastAPI()
app.include_router(router_api_user)
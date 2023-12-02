from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.materials import material
from routes.events import event
from routes.users import user

# Application initilization
app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )

# Registering routes
app.include_router(material)
app.include_router(event)
app.include_router(user)

@app.get('/')
async def index():
    return {"message": "Welcome to NimechE E-Library"}

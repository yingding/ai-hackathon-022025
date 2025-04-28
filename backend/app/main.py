import logging
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from app.api import agents
# from app.api import memory, functions, weather, agents, filters, kernel, process
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
# load the environment variables from .env file
from app.config import settings

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Semantic Kernel Demo API")

security = HTTPBearer()
VALID_TOKEN = settings.key_token  # Replace with your actual token or JWT validation

# show only the half of the token in the logs and replace the rest with asterisks
if len(VALID_TOKEN) > 7:
    masked_token = VALID_TOKEN[:5] + "*" * (len(VALID_TOKEN) - 7) + VALID_TOKEN[-2:]
else:
    masked_token = "*" * (len(VALID_TOKEN))
logging.info(f"Using token: {masked_token}")
# logging.info(f"VALID_TOKEN length: {len(VALID_TOKEN)}")
# logging.info(f"Masked token length: {len(masked_token)}")

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.scheme != "Bearer" or credentials.credentials != VALID_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid or missing token"
        )

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
# app.include_router(memory.router)
# app.include_router(functions.router)
# app.include_router(weather.router)
app.include_router(agents.router, dependencies=[Depends(verify_token)])
# app.include_router(filters.router)
# app.include_router(kernel.router)
# app.include_router(process.router)


# Root endpoint
@app.get("/")
async def root(credentials: HTTPAuthorizationCredentials = Depends(verify_token)):
    return {"message": "Semantic Kernel Demo API is running"}


# Note: Memory initialization is now done on-demand when accessing memory endpoints

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

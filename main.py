from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from apps.calculator.route import router as calculator_router
from constants import SERVER_URL, PORT, ENV


# Optional lifespan (remove if not used)
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting lifespan context")
    yield  # Perform startup tasks here, and clean up after yield if needed
    print("Ending lifespan context")


# Initialize FastAPI app
app = FastAPI(lifespan=lifespan)  # Pass lifespan only if you need it

# Add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins; change to specific origins in production
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Test route
@app.get("/")
async def root():
    return {"message": "Server is running"}

# Include the router
app.include_router(calculator_router, prefix="/calculate", tags=["calculate"])

# Run the app
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=SERVER_URL,  # Host is retrieved from constants
        port=int(PORT),   # Port is retrieved from constants
        reload=(ENV == "dev"),  # Enable reload only in development
    )

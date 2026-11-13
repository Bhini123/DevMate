from fastapi import FastAPI

# Create our FastAPI application
app = FastAPI(
    title="DevMate",
    description="An AI-powered Autonomous Developer Assistant",
    version="1.0.0"
)

# First route: Welcome message
@app.get("/")
def home():
    return {
        "message": "Welcome to DevMate!",
        "status": "Running successfully"
    }

# Second route: Health check
@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

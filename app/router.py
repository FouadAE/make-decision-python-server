from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.prompt.schema import GenerateReportRequest
from asyncio.log import logger
from fastapi import HTTPException
from app.prompt.service import Service
import os
from dotenv import load_dotenv
load_dotenv()


app = FastAPI(
    title="My FastAPI Server",
    description="A simple FastAPI server",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World", "status": "success"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

#endpoint to take params and send prompt to openai 
@app.post("/prompt")
async def prompt_handler(request_body: GenerateReportRequest):
    try:
        print(f"Received request body: {request_body}")
        response = await Service.generate_report(request_body)
    except Exception as e:
        logger.error(f"Error in prompt_handler: {e}")
        raise HTTPException(status_code=500, detail=str(e))


    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=os.getenv("HOST"), port=os.getenv("PORT"))
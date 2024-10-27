from openai import OpenAI
import os
from fastapi import FastAPI, HTTPException, Request
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Set OpenAI API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI()
client.api_key = OPENAI_API_KEY

# Assistant ID (replace with your actual assistant ID)
ASSISTANT_ID = "asst_ydbokLdKBnLWxi8lnT9L3VwZ"

@app.post("/get-building")
async def get_building(request: Request):
    try:
        # Extract the user message from the request body
        body_content = await request.json()
        user_message = body_content.get("message", "")

        if not user_message:
            raise HTTPException(status_code=400, detail="The 'message' field is required.")

        # Step 1: Retrieve the assistant by ID
        assistant = client.beta.assistants.retrieve(ASSISTANT_ID)
        print(f"Retrieved assistant: {assistant}")

        # Step 2: Create a new thread for the assistant
        thread = client.beta.threads.create()
        print(f"Created thread: {thread.id}")

        # Step 3: Send a message to the thread
        message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=user_message
        )
        print(f"Message sent: {message}")

        # Step 4: Start a run on the thread
        run = client.beta.threads.runs.create_and_poll(
            thread_id=thread.id,
            assistant_id=ASSISTANT_ID,
        )

        # Step 5: Check if the run is completed
        if run.status == 'completed':
            # Retrieve the list of messages in the thread
            messages = client.beta.threads.messages.list(thread_id=thread.id)

            # Extract the latest assistant response
            assistant_response = next(
                (msg for msg in messages if msg.role == "assistant"), None
            )

            if assistant_response:
                # Access the text content correctly
                if hasattr(assistant_response.content[0], 'text'):
                    response_text = assistant_response.content[0].text.value
                    return response_text
                else:
                    return {"message": "Assistant response has no text content."}
            else:
                return {"message": "No assistant response found."}
        else:
            return {"message": f"Run status: {run.status}"}

    except client.error.OpenAIError as e:
        raise HTTPException(status_code=500, detail=f"OpenAI API error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")
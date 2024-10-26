# **LLMto3D AEC Tech 2024 Hackathon**

## **Overview**
This project demonstrates how to create a **FastAPI-based API** that interacts with an OpenAI assistant. The API allows you to retrieve the assistant, send messages, and receive responses, all using **OpenAI’s Assistant and Thread APIs**. It receives instructions to generate a building and returns the building description in a JSON format.

## **Features**
- Retrieve a custom assistant by its ID.
- Create threads to maintain conversation context.
- Send user messages and receive responses from the assistant.
- Handle runs and poll them for completion.
- Error handling for missing inputs or failed API requests.
- Receives a prompt and returns a topological JSON description of a building.

---

## **Prerequisites**
Make sure you have the following installed on your system:
- **Python 3.8+**: [Download here](https://www.python.org/downloads/)
- **pip** (Python package installer)
- **OpenAI API Key**: Create an account and generate a key from [OpenAI](https://platform.openai.com/signup/).

---

## **Setup Instructions**

1. **Clone the repository** (or create your own project):
   ```bash
   git clone https://github.com/franmaranchello/llmto3d-backend.git
   cd llmto3d-backend
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On MacOS/Linux
   .venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**:
    Run the following command to install all dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in the project root to store environment variables securely:
   ```bash
   touch .env  # On Mac/Linux
   echo OPENAI_API_KEY=sk-your-openai-key > .env  # Or use any text editor to create it
   ```

   Add your **OpenAI API key** to the `.env` file:
   ```plaintext
   OPENAI_API_KEY=sk-your-openai-key
   ```

---

## **Running the Application**

1. **Start the FastAPI app**:
   Use the following command to run the API server:
   ```bash
   uvicorn app:app --reload --port 8000
   ```

2. **Test the API**:
   Use `curl` or Postman to test the `/get-building` endpoint:
   ```bash
   curl -X POST "http://127.0.0.1:8000/get-building" \
   -H "Content-Type: application/json" \
   -d '{
     "message": "Create a building with 4 floors, each with two offices."
   }'
   ```

3. **Expected Response**:
   If everything is set up correctly, you should receive a response similar to:
   ```json
        {
        "building": {
            "name": "Modern Office Building",
            "address": "789 Corporate Dr, Business City",
            "floors": [
            {
                "floorNumber": 1,
                "height": 3.5,
                "rooms": [
                {
                    "roomID": "101",
                    "name": "Office A",
                    "area": 20
                },
                {
                    "roomID": "102",
                    "name": "Office B",
                    "area": 25
                }
                ]
            },
            {
                "floorNumber": 2,
                "height": 3.5,
                "rooms": [
                {
                    "roomID": "201",
                    "name": "Office C",
                    "area": 22
                },
                {
                    "roomID": "202",
                    "name": "Office D",
                    "area": 28
                }
                ]
            },
            {
                "floorNumber": 3,
                "height": 3.5,
                "rooms": [
                {
                    "roomID": "301",
                    "name": "Office E",
                    "area": 24
                },
                {
                    "roomID": "302",
                    "name": "Office F",
                    "area": 26
                }
                ]
            },
            {
                "floorNumber": 4,
                "height": 3.5,
                "rooms": [
                {
                    "roomID": "401",
                    "name": "Office G",
                    "area": 23
                },
                {
                    "roomID": "402",
                    "name": "Office H",
                    "area": 27
                }
                ]
            }
            ]
        }
        }
   ```

---

## **Project Structure**

```
/your-project-folder
│
├── app.py                # FastAPI app implementation
├── .env                  # Environment variables (API keys, etc.)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## **Troubleshooting**

1. **Missing OpenAI API Key Error**:
   - Ensure the `.env` file is correctly configured with your API key.
   - Verify the **API key** is active and correct by running:
     ```bash
     echo $OPENAI_API_KEY
     ```

2. **Dependency Errors**:
   - Run the following command to ensure all dependencies are installed:
     ```bash
     pip install -r requirements.txt
     ```

3. **API Response Issues**:
   - Make sure your **OpenAI account** is active and the API key has sufficient permissions.
   - Verify the assistant ID and any other inputs being used in the API calls.

---

## **Further Reading**
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
- [OpenAI Python Library](https://beta.openai.com/docs/libraries)

---

## **License**
This project is licensed under the MIT License – see the LICENSE file for more details.
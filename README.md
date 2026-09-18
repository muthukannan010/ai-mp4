# CineAI Studio

CineAI Studio is a full-stack application integrating a Next.js frontend with a Python FastAPI backend and AI-driven data schemas for storytelling and video generation.

## Project Structure

The project is structured into three main components:

### 1. Frontend (src/)
- Built with **Next.js 16**, **React 19**, and **Tailwind CSS**.
- The main web interface for users to interact with the AI studio.

### 2. Backend (backend/)
- Built with **Python FastAPI** and **Uvicorn**.
- Provides core API routes, including health checks and system configuration (backend/app/api/).

### 3. AI Module (ai/)
- Centralized Python module for AI orchestration.
- **Schemas**: Utilizes Pydantic to strictly define data structures for various components:
  - chat.py: Schemas for conversational requests and responses.
  - story.py & storyboard.py: Structures for generated stories and scenes.
  - character.py: Schemas for character metadata.
  - editing.py: Schemas for video editing instructions.
- **Director**: Contains the director.py orchestrator to manage AI workflows.

## Visual File Structure

```text
cineai-studio/
├── src/                # Next.js Frontend
│   └── app/            # App Router pages and components
├── backend/            # FastAPI Backend
│   ├── app/
│   │   ├── api/        # API endpoints
│   │   └── main.py     # FastAPI entry point
│   ├── requirements.txt
│   └── .env
├── ai/                 # AI Orchestration Module
│   ├── app/
│   │   ├── director/   # AI Director logic
│   │   └── schemas/    # Pydantic data models
│   │       ├── chat.py
│   │       ├── character.py
│   │       ├── editing.py
│   │       └── story.py
│   └── requirements.txt
├── package.json        # Frontend dependencies
└── README.md
```

## What Has Been Done So Far

- **Project Initialization**: Basic directory layout established for frontend, backend, and AI.
- **Frontend Setup**: Next.js app scaffolding with basic global CSS and layout configuration.
- **Dashboard UI**: Created the main cinematic dashboard interface (src/app/page.tsx) with a sidebar for project navigation and top nav.
- **AI Director Interface**: Implemented the chat interface structure with quick action buttons for seamless interaction.
- **Profile Management**: Built a fully functional Profile Settings modal with local state management for Name and Email, along with a working profile dropdown menu.
- **Backend Infrastructure**: Core FastAPI app created with API routing and pydantic-settings for configuration.
- **AI Schemas**: Defined comprehensive data models to facilitate structured communication between the user, the frontend, and the AI backend models.

## Running the Application Locally

### Frontend
```bash
npm install
npm run dev
```

### Backend
Navigate to the backend/ directory, install requirements, and run the server:
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

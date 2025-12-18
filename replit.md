# Flappy Bird Game

## Overview
A browser-based Flappy Bird clone built with vanilla HTML, CSS, and JavaScript. The game features a Flask backend with PostgreSQL database for leaderboard functionality.

## Project Structure
- `index.html` - The complete game including HTML structure, CSS styles, and JavaScript game logic
- `main.py` - Flask backend server with leaderboard API endpoints
- `pyproject.toml` - Python dependencies

## Features
- Classic Flappy Bird gameplay
- Day/night cycle based on score
- Animated clouds and buildings in background
- Pause functionality (P key)
- Score tracking with high score memory
- Online leaderboard with PostgreSQL database

## API Endpoints
- `GET /api/leaderboard` - Retrieve top 10 scores
- `POST /api/leaderboard` - Submit a new score (JSON body: {name, score})

## Running the Project
The game is served via Flask on port 5000. Run with `python main.py`.

## Controls
- **Space** or **Click** - Jump / Start game
- **P** - Pause/Resume

## Database
Uses PostgreSQL for persistent leaderboard storage. Connection via DATABASE_URL environment variable.

## Deployment
Configured for autoscale deployment with gunicorn WSGI server.

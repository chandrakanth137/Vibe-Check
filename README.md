# Vibe Check - Fashion Analysis App

Vibe Check is a Flask-based web application that allows users to upload an outfit image and receive a detailed fashion analysis. The app evaluates how well the outfit matches a specific event, location, and the user's fashion goals. It also provides recommendations for improvements and nearby fashion shops or boutiques.

## Features

- Upload an outfit image for analysis.
- Specify the event, location, and fashion goals.
- Receive a JSON-based analysis including:
    - Description of the outfit.
    - Match score (out of 100).
    - Strengths of the outfit.
    - Suggestions for improvements.
    - Local fashion recommendations (shops, malls, boutiques).
- User-friendly interface built with Tailwind CSS.

## Prerequisites

- Python 3.7 or higher
- A Google Generative AI API key (Gemini API)
- Flask and other dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
     ```bash
     git clone https://github.com/yourusername/vibe-check.git
     cd vibe-check
     ```

2. Create a virtual environment and activate it:
     ```bash
     uv venv
     source .venv/bin/activate
     ```

3. Install the required dependencies:
     ```bash
     uv pip sync pyproject.toml
     ```

4. Create a `.env` file in the project root and add the following environment variables:
     ```
     GEMINI_API_KEY=your_google_generative_ai_api_key
     SECRET_KEY=your_secret_key
     ```

5. Run the Flask application:
     ```bash
     python app.py
     ```

6. Open your browser and navigate to `http://127.0.0.1:5000`.

## Usage

1. Upload an image of your outfit.
2. Enter the event (e.g., Wedding, Conference, Party).
3. Specify your fashion goals (comma-separated, e.g., Elegant, Trendy, Casual).
4. Enter the location (e.g., City, Area).
5. Click "Analyze" to receive a detailed fashion analysis.

## File Structure

- `app.py`: Main Flask application file.
- `templates/index.html`: HTML template for the web interface.
- `static/`: Directory for static assets (if needed).
- `.env`: Environment variables file (not included in the repository).
- `requirements.txt`: List of Python dependencies.

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, Tailwind CSS
- **API**: Google Generative AI (Gemini API)
- **Environment Management**: Python `dotenv`

## Example Output

After submitting the form, the app provides a JSON-based analysis with the following structure:
```json
{
    "description": "A modern and elegant outfit suitable for formal events.",
    "match_score": 85,
    "strengths": [
        "Color coordination is excellent.",
        "Accessories complement the outfit well."
    ],
    "suggestions": [
        "Consider adding a blazer for a more formal look.",
        "Opt for leather shoes instead of sneakers."
    ],
    "local_recommendations": [
        {
            "name": "Fashion Boutique XYZ",
            "address": "123 Main Street, Cityville",
            "specialty": "Formal wear"
        },
        {
            "name": "Trendy Mall",
            "address": "456 Fashion Ave, Cityville",
            "specialty": "Casual and trendy outfits"
        }
    ]
}
```
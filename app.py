from flask import Flask, render_template, request, redirect, url_for, flash
import base64
import json
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY", "defaultsecret")

app = Flask(__name__)
app.secret_key = SECRET_KEY

# Helper function
def safe_json_parse(text: str):
    try:
        clean_text = text.replace("```json", "").replace("```", "").strip()
        return json.loads(clean_text)
    except Exception as e:
        print(f"Failed to parse JSON: {e}")
        return None

def analyze_fashion(image_bytes, event, fashion_goals, location):
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")

        mime_type = "image/jpeg"
        if image_bytes.startswith(b"\x89PNG"):
            mime_type = "image/png"

        encoded_image = base64.b64encode(image_bytes).decode()

        image_data = {
            "inline_data": {
                "data": encoded_image,
                "mime_type": mime_type
            }
        }

        prompt = (
            f"You are a professional fashion consultant.\n"
            f"Analyze the uploaded outfit image for a '{event}' event happening in {location}.\n"
            f"The user's fashion goals are: {', '.join(fashion_goals)}.\n\n"
            "Your analysis should:\n"
            "- Evaluate how well the outfit matches the event and location.\n"
            "- Adjust suggestions based on local fashion trends in that area.\n"
            "- Recommend specific types of shops, boutiques, or malls nearby where the user can upgrade their look.\n\n"
            "Respond STRICTLY in JSON format without extra commentary.\n\n"
            "The JSON must include:\n"
            "{\n"
            '  "description": "Short description of the outfit",\n'
            '  "matchScore": "Score out of 100",\n'
            '  "strengths": ["List of strengths"],\n'
            '  "improvements": ["List of improvements"],\n'
            '  "localRecommendations": ["List of shop/mall/boutique recommendations based on location"]\n'
            "}\n"
        )


        response = model.generate_content([prompt, image_data])
        result_text = response.text

        parsed = safe_json_parse(result_text)
        return parsed

    except Exception as e:
        print(f"Error: {e}")
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        image = request.files.get("image")
        event = request.form.get("event")
        fashion_goals = request.form.get("fashion_goals")
        location = request.form.get("location")

        if not (image and event and fashion_goals and location):
            flash("Please fill out all fields and upload an image!", "error")
            return redirect(url_for("index"))

        fashion_goals_list = [goal.strip() for goal in fashion_goals.split(",")]

        result = analyze_fashion(image.read(), event, fashion_goals_list, location)

        if result:
            return render_template("index.html", result=result)

        flash("Something went wrong during analysis.", "error")
        return redirect(url_for("index"))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

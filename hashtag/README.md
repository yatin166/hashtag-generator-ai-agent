# Simple Hashtag Generator Agent

This is a basic AI agent that generates the hashtags based on the caption text and image description.

## Setup

1. **Get a Gemini API Key:** You'll need an API key from Google AI Studio. You can get one by following the instructions here: [https://ai.google.dev/](https://ai.google.dev/).
2. Change directory to ```hashtag``` using ```cd hashtag```
3. Create ```.env``` file in the directory and add your API key:
    ```bash
    GOOGLE_API_KEY="YOUR_GEMINI_API_KEY"
    ```
4. setup python env using ```python3 -m venv env```
5. Activate the virtual environment:
    * **Linux/macOS:**
        ```bash
        source env/bin/activate
        ```
    * **Windows:**
        ```bash
        .\env\Scripts\activate
        ```
6. **Install the `google-adk`:**
    ```bash
    pip install google-adk
    ```

## Running the Agent
Navigate to parent folder and run following command:
```bash
adk web
```
This will start a web server and you can access the agent via the browser at `http://localhost:8000`.

## Example
**Input the caption text**: Enter the caption text in the input field. like:
```
Caption: "Exploring the vibrant streets of Tokyo at night." Image Description: "A bustling cityscape with neon lights and crowded sidewalks."
```
it will generate the hashtags based on the caption text and image description. like:
```
#Tokyo
#NightPhotography
#Japan
#Cityscape
#NeonLights
#Travel
#Explore
#StreetPhotography
#Nightlife
#VibrantCity
#TokyoNight
#BeautifulDestinations
#TravelPhotography
#UrbanExploration
```
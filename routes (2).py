from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from urllib.parse import quote

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


def generate_story(prompt, character, setting, tone, art_style):
    """
    Simple story generator.
    Replace this function with Gemini API integration later.
    """

    panels = [
        {
            "title": "Panel 1 - The Beginning",
            "text": (
                f"{character} begins an exciting journey in the {setting}. "
                f"The adventure starts with a mysterious discovery."
            )
        },
        {
            "title": "Panel 2 - The Discovery",
            "text": (
                f"While exploring the {setting}, {character} discovers "
                f"something unexpected related to: {prompt}."
            )
        },
        {
            "title": "Panel 3 - The Challenge",
            "text": (
                f"{character} faces a difficult challenge. "
                f"Even though the situation becomes {tone}, "
                f"the hero decides not to give up."
            )
        },
        {
            "title": "Panel 4 - The Adventure",
            "text": (
                f"Using courage and creativity, {character} moves forward "
                f"and discovers the secret behind the adventure."
            )
        },
        {
            "title": "Panel 5 - The Ending",
            "text": (
                f"The adventure ends successfully. {character} returns home "
                f"with a wonderful memory from the {setting}."
            )
        }
    ]

    return panels


def image_url(text, style):
    """
    Placeholder image generator.
    Uses a public placeholder service for the demo.
    """

    prompt = quote(f"{text}, {style} comic art")

    return f"https://placehold.co/800x500?text={prompt}"


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@router.post("/generate", response_class=HTMLResponse)
async def generate(
    request: Request,
    prompt: str = Form(...),
    character: str = Form(...),
    setting: str = Form(...),
    tone: str = Form(...),
    art_style: str = Form(...)
):

    panels = generate_story(
        prompt,
        character,
        setting,
        tone,
        art_style
    )

    for panel in panels:
        panel["image"] = image_url(
            panel["title"],
            art_style
        )

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "prompt": prompt,
            "character": character,
            "setting": setting,
            "tone": tone,
            "art_style": art_style,
            "panels": panels
        }
    )

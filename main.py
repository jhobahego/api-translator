from fastapi import FastAPI, Form
from starlette.responses import RedirectResponse

from translator_service import translate_text

app = FastAPI()


@app.get("/")
async def root():
    return RedirectResponse("/docs", status_code=303)


@app.post("/api/translate")
def translate(
        message: str = Form(...),
        original_language: str = Form(...),
        final_language: str = Form(...)
):
    translated_text = translate_text(
        message_to_translate=message, base_language=original_language, language_to_translate=final_language
    )

    return translated_text

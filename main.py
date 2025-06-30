from fastapi import FastAPI, Request
import pyttsx3

app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    message = data.get("message", "Alerta sin mensaje recibido")

    print(f"📩 ALERTA RECIBIDA: {message}")

    # Convertir mensaje a voz
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

    return {"status": "ok", "message": message}

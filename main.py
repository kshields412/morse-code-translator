from fastapi import FastAPI
import model.code

app = FastAPI()

morse_code_dict = model.code.MORSE_CODE_DICT


@app.get("/")
async def root():
    return {"message": "Hello World"}

from fastapi import FastAPI
from transformers import pipeline


## create a new fastapi app instance
app = FastAPI()

## Initialize the text generation pipeline
pipe = pipeline("text2text-generation",model="google/flan-t5-small")

@app.get("/")
def home():
    return {"message":"Welcome to Text Generation APP"}

@app.get("/generate")
def generate(text:str):
    # use the pipeline to generate text from given input text
    output = pipe(text)
    output = output[0]["generated_text"]
    return {"output":output}


from fastapi import FastAPI

app = FastAPI()

@app.get('/hello')
def home():
    return {
        'message':'Running😁.'
    }
    

print(home())
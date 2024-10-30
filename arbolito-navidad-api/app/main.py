from fastapi import FastAPI, Response
from mangum import Mangum

app = FastAPI()

@app.get("/arbolito", response_class=Response)
def arbolito():
    
    arbol = ""
    for i in range(5):
        arbol += " " * (5 - i - 1) + "*" * (2 * i + 1) + "\n"
    arbol += " " * (5 - 1) + "*\n"
    return Response(content=arbol, media_type="text/plain")

handler = Mangum(app)

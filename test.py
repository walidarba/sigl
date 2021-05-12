import uvicorn
from fastapi import FastAPI, File, UploadFile
from starlette.responses import RedirectResponse

app_desc = """<h2>Try this app by uploading any image with `predict/image`</h2>
<h2>Try Covid symptom checker api - it is just a learning app demo</h2>
<br>by Aniket Maurya"""

app = FastAPI(title='Tensorflow FastAPI Starter Pack', description=app_desc)

#@app.get("/", include_in_schema=False)
#async def index():
#    return RedirectResponse(url="/docs")

if __name__ == "__main__":
    uvicorn.run(app, debug=True)

#print("walid figuig")

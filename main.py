from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
def main(name: str, message: str):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Rekruto</title>
    </head>
    <body>
        <h1>Hello {name}! {message}!<h1>
    </body>
    </html>
    """

    return HTMLResponse(html_content)

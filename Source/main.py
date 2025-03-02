import typer
import os
from Dev.framework.AppKit import AppKit

app = typer.Typer()

def application():
    app_struct = {
        "AppType": "executable"
    }
    AppKit.struct("nullUnix", app_struct)
    
    return AppKit(
        name="nullUnix",
        version="0.0.1dev",
        author="SufremOak",
    )

@app.command()
def run():
    AppKit().run()

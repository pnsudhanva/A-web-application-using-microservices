from app import app, db

@app.cli.command("initdb")
def initdb():
    db.create_all()
    print("Initialized the database.")

import sqlite3
import click
from flask import current_app, g

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE_URI"])
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(_=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource("db/seed.sql") as f:
        db.executescript(f.read().decode("utf-8"))

@click.command("init-db")
def init_db_command():
    init_db()
    
    click.echo("Initialized Hyacinth database")

@click.command("add-access-code")
@click.option("--code")
@click.option("--address")
def add_access_code(code, address):
    db = get_db()

    db.execute(
        "INSERT INTO users (id, delivery_address) VALUES (?, ?)",
        (code, address)
    )
    db.commit()
    
    click.echo(f"Added {code} with address {address} to the database")

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(add_access_code)
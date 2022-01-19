from squire.cli import app


def main():
    try:
        from dotenv import load_dotenv

        load_dotenv()
    except ImportError as e:
        pass

    app()

import uvicorn
from api.config import Config


def main() -> None:
    """Entrypoint of the application."""
    uvicorn.run(
        "api.app:get_app",
        workers=Config.WORKERS_COUNT,
        host=Config.HOST,
        port=Config.PORT,
        reload=Config.RELOAD,
        log_level=Config.LOG_LEVEL.lower(),
        factory=True,
    )


if __name__ == "__main__":
    main()

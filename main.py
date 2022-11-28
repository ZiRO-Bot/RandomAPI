import uvicorn

if __name__ == "__main__":
    port: int = 2264
    config = uvicorn.Config("app:app", port=port, host="0.0.0.0")

    runner = uvicorn.Server(config)

    runner.run()

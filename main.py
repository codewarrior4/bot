import asyncio
from file1 import setup_application as setup_application_file1
from file2 import setup_application as setup_application_file2

async def start_bot(app):
    await app.initialize()  # Initialize application
    await app.start()       # Start application
    await app.updater.start_polling()  # Start polling without blocking

async def main():
    app1 = setup_application_file1()
    app2 = setup_application_file2()
    # Run both bots concurrently
    await asyncio.gather(start_bot(app1), start_bot(app2))
    # Keep the program running
    await asyncio.Event().wait() 

# Run the main coroutine
asyncio.run(main())

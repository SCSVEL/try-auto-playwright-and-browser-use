import asyncio
from dotenv import load_dotenv
load_dotenv()

from browser_use import Agent
from browser_use.llm import ChatOpenAI

async def main():
    agent = Agent(
        task="1. Go to the website https://www.saucedemo.com/"
            "2. Login with the username 'standard_user' and password 'secret_sauce'." \
            "3. Add the item [Sauce Labs Backpack] to the cart." \
            "4. Go to the cart" \
            "5. Checkout" \
            "6. Enter the first name 'Hello', last name 'shan' and zip '12345'" \
            "7. Continue" \
            "8. Finish the order" \
            "9. check if the message 'THANK YOU FOR YOUR ORDER' is displayed" \
            "10. Exit the browser",

        llm=ChatOpenAI(model="o4-mini", temperature=1.0),
    )
    await agent.run()

asyncio.run(main())
import httpx
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

async def get():
    
    url = os.getenv('ADDR')
    
    if not url:
        raise ValueError("Url not found")
    try:
        async with httpx.AsyncClient(timeout=0.1) as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as er:
        print("")
        raise
    except httpx.TimeoutException as err:
        print("EROOOR TIME OUT")
        raise
    except ValueError as er:
        print(er)
        raise
    
def main():
    res = asyncio.run(get())
    print(res)

if __name__ == '__main__':
    main()
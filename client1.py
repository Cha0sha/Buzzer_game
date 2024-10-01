import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")
        
        await websocket.send(name)  
        welcome_message = await websocket.recv()  
        print(welcome_message)

        while True:
            print("Press Enter to buzz, or type a message and press Enter to send it:")
            user_input = input()

            if user_input == "":
                await websocket.send('buzz')  
            else:
                await websocket.send(user_input)  
            
            response = await websocket.recv()
            print(f"Server says: {response}")

if __name__ == '__main__':
    asyncio.run(hello())

import asyncio
import websockets
import time

clients = {} 
buzz_times = {} 

async def register(websocket, name):
    clients[websocket] = name

async def unregister(websocket):
    if websocket in clients:
        del clients[websocket]

async def send_scores(winner_name, winner_time):
    scores = []
    for name in clients.values():
        buzz_time = buzz_times.get(name, None)
        if buzz_time is not None:
            delay = buzz_time - winner_time
            scores.append(f"{name}: {delay:.2f} seconds late")
        else:
            scores.append(f"{name}: Did not buzz")

    scoreboard = f"Winner: {winner_name}! Scores:\n" + "\n".join(scores)
    for websocket in clients:
        await websocket.send(scoreboard)

async def hello(websocket, path):
    name = await websocket.recv() 
    await register(websocket, name)
    print(f'Server received: {name}')
    
    await websocket.send('Welcome to the Buzzer Game! Get ready to buzz!')

    while True:
        try:
            message = await websocket.recv()  
            if message == 'buzz':
                buzz_time = time.time()
                buzz_times[name] = buzz_time
                print(f"{name} buzzed at {buzz_time}")

                if len(buzz_times) == 1:
                    winner_name = name
                    winner_time = buzz_time
                    await websocket.send(f"Congratulations {winner_name}, you are the winner!")
                    await send_scores(winner_name, winner_time)

                    await asyncio.sleep(20)
                    await send_scores(winner_name, winner_time)
                    break  
            else:
                print(f"Message from {name}: {message}")
        except websockets.exceptions.ConnectionClosed:
            break

    await unregister(websocket)

async def main():
    async with websockets.serve(hello, "localhost", 8765):
        await asyncio.Future()  
if __name__ == "__main__":
    asyncio.run(main())

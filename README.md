# Buzzer Game

A simple multi-tenant buzzer game built using Python's `asyncio` and `websockets` libraries. This application allows multiple clients to connect and compete in a buzzer game where they can "buzz" in to win.

## Features

- **Multi-Tenancy**: Supports multiple users connecting simultaneously.
- **Real-Time Interaction**: Clients can send buzz signals and receive immediate feedback.
- **Winner Announcement**: The first participant to buzz is declared the winner, with a scoreboard displaying delays for other participants.

## Requirements

- Python 3.x
- `websockets` library

You can install the required library using pip:

```bash
$ pip install websockets


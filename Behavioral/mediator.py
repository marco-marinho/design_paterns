"""
In the mediator pattern, communication between components goes through a middle man. Reducing coupling and simplifying
dependencies.

The mediator design pattern is a behavioral pattern that facilitates communication between objects by encapsulating
their interactions within a mediator object. This pattern promotes loose coupling by preventing objects from referring
to each other explicitly, allowing their interaction to be managed through the mediator.

Key Points:
1 - Centralized Communication: The mediator centralizes the communication between objects, reducing the dependencies
    between them.
2 - Loose Coupling: Objects interact through the mediator rather than directly, promoting loose coupling and enhancing
    modularity.
3 - Simplified Object Protocols: The pattern simplifies the interaction protocols between objects by having a single
    point of communication.
4 - Improved Maintenance: Easier to maintain and extend the system since interaction logic is centralized in the
    mediator.

https://refactoring.guru/design-patterns/mediator
"""

import asyncio
import socket
import threading


class Server:

    def __init__(self):
        self.loop = asyncio.new_event_loop()
        threading.Thread(target=self._start_event_loop, daemon=True).start()
        self.connections = {}
        self.data = {}
        self.loop.create_task(asyncio.start_server(self._serve, "localhost", 8686))
        self.running = True

    def _start_event_loop(self):
        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()

    async def handle_receptions(self, username, reader: asyncio.StreamReader):
        print(f"Receiving for {username}")
        while True:
            data = await reader.readline()
            print(f"Server received {data}")
            if not data:
                del self.connections[username]
                del self.data[username]
                return
            self.data[username].append(data)

    async def handle_transmissions(self, username, writer):
        while True:
            if username not in self.data:
                return
            if len(self.data[username]) > 0:
                data = self.data[username].pop()
                writer.write(data)
                await writer.drain()
                print(f"Server sent {data}")
            await asyncio.sleep(1)

    async def _serve(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        writer.write("Welcome to the chat room\n".encode("utf-8"))
        username = await reader.readline()
        print(f"Username: {username}")
        if username is not None:
            self.data[username] = []
            reception_task = self.loop.create_task(self.handle_receptions(username, reader))
            transmission_task = self.loop.create_task(self.handle_transmissions(username, writer))
            self.connections[username] = (reader, writer, reception_task, transmission_task)
        await writer.drain()


if __name__ == "__main__":
    server = Server()
    # asyncio.run(send_client())
    # create an INET, STREAMing socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # now connect to the web server on port 80 - the normal http port
    s.connect(("localhost", 8686))
    sent = s.send("Marco\n".encode())
    rcv = s.recv(1024)
    print("Client received:", rcv)
    data = None
    while data != 'quit\n':
        data = input() + "\n"
        print("Client sent:", data.encode())
        s.send(data.encode())
        rcv = s.recv(1024)
        print("Client received:", rcv)
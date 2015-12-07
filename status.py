from mcstatus import MinecraftServer
import json

# If you know the host and port, you may skip this and use MinecraftServer("example.org", 1234)
server = MinecraftServer.lookup("localhost:25565")

# 'status' is supported by all Minecraft servers that are version 1.7 or higher.
status = server.status()
query = server.query()

# print("{0} online:".format(status.players.online))+" {0}".format(", ".join(query.players.names))
print(json.dumps({"content": ', '.join(query.players.names), "refresh": 300, "vibrate": 1, "font": 4, "theme": 1, "scroll": 33, "light": 0, "blink": 0, "updown": 1 }))
# 'ping' is supported by all Minecraft servers that are version 1.7 or higher.
# It is included in a 'status' call, but is exposed separate if you do not require the additional info.
# latency = server.ping()
# print("The server replied in {0} ms".format(latency))

# 'query' has to be enabled in a servers' server.properties file.
# It may give more information than a ping, such as a full player list or mod information.

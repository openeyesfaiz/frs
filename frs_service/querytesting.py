import websocket 
import json

ws = websocket.WebSocket()
ws.connect("ws://183.178.15.122:8880")

ws.send(json.dumps({"Detail":{"UserId":8},"RequestType":203, "RequestId":1}))
txtAnswer = ws.recv_frame()

print(websocket.ABNF.OPCODE_MAP[txtAnswer.opcode])
print(txtAnswer.data)

ws.close()
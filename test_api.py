import uvicorn, threading, time, requests, json

config = uvicorn.Config("main:app", host="127.0.0.1", port=8000, log_level="error")
server = uvicorn.Server(config)
thread = threading.Thread(target=server.run)
thread.daemon = True
thread.start()
time.sleep(3)

print("=== POST /chat ===")
r = requests.post("http://127.0.0.1:8000/chat", json={"session_id": "api-test", "mensaje": "Cual es la politica de envios?"})
print(f"Status: {r.status_code}")
print(f"Respuesta: {r.json()['respuesta']}")

print("\n=== GET /chat/{id}/historial ===")
r = requests.get("http://127.0.0.1:8000/chat/api-test/historial")
data = r.json()
print(f"Mensajes en historial: {len(data['messages'])}")

print("\n=== DELETE /chat/{id} ===")
r = requests.delete("http://127.0.0.1:8000/chat/api-test")
print(r.json())

print("\n=== Sesiones separadas via API ===")
r1 = requests.post("http://127.0.0.1:8000/chat", json={"session_id": "s1", "mensaje": "Me llamo Ana"})
r2 = requests.post("http://127.0.0.1:8000/chat", json={"session_id": "s2", "mensaje": "Como me llamo?"})
r3 = requests.post("http://127.0.0.1:8000/chat", json={"session_id": "s1", "mensaje": "Como me llamo?"})
print(f"S1 primera vez: {r1.json()['respuesta']}")
print(f"S2 (no debe saber): {r2.json()['respuesta']}")
print(f"S1 segunda vez (debe recordar): {r3.json()['respuesta']}")

server.should_exit = True
time.sleep(1)
print("\nTODO OK")

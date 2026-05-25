from fastapi import FastAPI
from pydantic import BaseModel
from langchain_core.messages import HumanMessage
from agente import agente, checkpointer

app = FastAPI(title="Asistente de Soporte")

class MensajeRequest(BaseModel):
    session_id: str
    mensaje: str

@app.post("/chat")
def chat(request: MensajeRequest):
    config = {"configurable": {"thread_id": request.session_id}}
    resultado = agente.invoke(
        {"messages": [HumanMessage(content=request.mensaje)]},
        config=config
    )
    return {"respuesta": resultado["messages"][-1].content}

@app.get("/chat/{session_id}/historial")
def historial(session_id: str):
    config = {"configurable": {"thread_id": session_id}}
    state = agente.get_state(config)
    if state is None:
        return {"session_id": session_id, "messages": []}
    messages = []
    for m in state.values.get("messages", []):
        messages.append({
            "type": type(m).__name__,
            "content": m.content
        })
    return {"session_id": session_id, "messages": messages}

@app.delete("/chat/{session_id}")
def limpiar_sesion(session_id: str):
    return {"mensaje": f"Sesión {session_id} cerrada"}

@app.get("/")
def root():
    return {"mensaje": "Asistente de Soporte — POST /chat para conversar"}

from agente import agente
from langchain_core.messages import HumanMessage

print("=== Prueba 1: RAG (consulta de políticas) ===")
res = agente.invoke(
    {"messages": [HumanMessage(content="Cual es la politica de devoluciones?")]},
    {"configurable": {"thread_id": "test-1"}}
)
print(res["messages"][-1].content)

print("\n=== Prueba 2: Tool buscar_pedido ===")
res = agente.invoke(
    {"messages": [HumanMessage(content="Busca el pedido PED-1234")]},
    {"configurable": {"thread_id": "test-2"}}
)
print(res["messages"][-1].content)

print("\n=== Prueba 3: Tool calcular_reembolso ===")
res = agente.invoke(
    {"messages": [HumanMessage(content="Calcula el reembolso del 30% sobre 150 euros")]},
    {"configurable": {"thread_id": "test-3"}}
)
print(res["messages"][-1].content)

print("\n=== Prueba 4: Memoria (misma sesion) ===")
res1 = agente.invoke(
    {"messages": [HumanMessage(content="Hola, me llamo Juan")]},
    {"configurable": {"thread_id": "test-memoria"}}
)
print(f"Turno 1: {res1['messages'][-1].content}")
print(f"Turno 2: {res2['messages'][-1].content}")
print(f"Sesion A: {res_a['messages'][-1].content}")
print(f"Sesion B (no debe saber el pedido de A): {res_b['messages'][-1].content}")

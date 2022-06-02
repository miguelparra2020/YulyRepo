import asyncio

async def proceso(id_proceso):
    print("Empieza proceso:", id_proceso)
    await asyncio.sleep(5)
    print("Acaba proceso:",id_proceso)

async def main():
    await asyncio.gather(proceso(1),proceso(2),proceso(3))

asyncio.run(main())
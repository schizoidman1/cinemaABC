import asyncio

class CinemaLanches:
    def __init__(self):
        self.pipoca_ready = False
        self.refrigerante_ready = False

    async def getPipoca(self):
        await asyncio.sleep(30)  # Simula o tempo de preparo da pipoca
        self.pipoca_ready = True

    async def getRefrigerante(self):
        await asyncio.sleep(20)  # Simula o tempo de preparo do refrigerante
        self.refrigerante_ready = True

    async def lanchePronto(self):
        await asyncio.gather(self.getPipoca(), self.getRefrigerante())

    def isLanchePronto(self):
        return self.pipoca_ready and self.refrigerante_ready

```mermaid
 sequenceDiagram
     Main->>Machine: m = Machine()
     Machine->>FuelTank: fuel_contents_0
     Machine->>FuelTank: self.tank.fill(40)
     Machine->>Engine: Engine(self.tank)
     Engine->>FuelTank: def __init__(self, tank)
     FuelTank->>Engine: self._fuel_tank = tank
     Main->>Machine: m.drive()
     Machine->>Engine: self._engine.start()
     Engine->>FuelTank: self._fuel_tank.consume(5)
     Machine->>Engine: self._engine.is_running()
     Machine->>Engine: self._engine.use_energy()
     Engine->>FuelTank: self._fuel_tank.consume(10)
```

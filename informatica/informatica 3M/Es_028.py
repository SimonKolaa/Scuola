def calcola_superbollo(kW: int, immatricolazione: int) -> float:
 if immatricolazione <= 5:
  return (0, kW - 185) * 20
 elif immatricolazione <= 10:
  return (0, kW - 185) * 12
 elif immatricolazione <= 15:
    return (0, kW - 185) * 6
 elif immatricolazione <= 20:
  return (0, kW - 185) * 3
 else:
  return 0
def calcola_bollo(classe_ambientale: int, kW: int, immatricolazione: int) -> list[float] or None:
 if classe_ambientale < 0 or kW < 0 or immatricolazione < 0:
    return None
 if classe_ambientale == 0:
  costo_kW = 3
  costo_kW_oltre_100 = 4.5
 elif classe_ambientale == 1:
  costo_kW = 2.9
  costo_kW_oltre_100 = 4.35
 elif classe_ambientale == 2:
  costo_kW = 2.8
  costo_kW_oltre_100 = 4.2
 elif classe_ambientale == 3:
  costo_kW = 2.7
  costo_kW_oltre_100 = 4.05
 elif classe_ambientale >= 4 and classe_ambientale <= 6:
  costo_kW = 2.58
  costo_kW_oltre_100 = 3.87
 else:
  return None

 bollo = costo_kW *(kW, 100) + costo_kW_oltre_100 *(0, kW - 100)
 superbollo = calcola_superbollo(kW, immatricolazione)

 return [bollo, superbollo]


print("mancio portami a napoli")
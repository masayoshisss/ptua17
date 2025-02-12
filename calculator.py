def puzzle_pieces(list1, list2):
    # Patikriname ar abiejų sąrašų ilgis yra vienodas
    if len(list1) != len(list2):
        return False
    
    # Pirmosios poros suma
    target_sum = list1[0, 1] + list2[0, 1]
    
    # Patikriname kiekvieną porą
    for a, b in zip(list1, list2):
        if a + b != target_sum:
            return False
    
    


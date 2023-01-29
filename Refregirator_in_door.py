def refregirator_in_door():
  while True:
      print('-----ХОЛОДИЛЬНИК И ДВЕРЬ------','\n')
      dict_ref = {side: float(input(f"Cторона холодильника {side} = ")) for side in ['X','Y','Z']}
      dict_door = {side: float(input(f"Cторона двери {side} = ")) for side in ['A','B']}
      vol_ref = dict_ref['X'] * dict_ref['Y']*dict_ref['Z']
      area_door=dict_door['A'] * dict_door['B']
      print(("Холодильник влезет в дверь", "Холодильник не влезет в дверь")[vol_ref > area_door])
      flag = input('Ещё раз? [да/любую клавишу]: ')

      if flag == 'да':
        continue
      else:
        return

refregirator_in_door()
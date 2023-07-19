skumriq_lv = float(input())
caca_lv = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())

palamud = skumriq_lv + skumriq_lv * 0.6
safrid = caca_lv + caca_lv * 0.8
midi = 7.5
total = float(palamud * palamud_kg + safrid * safrid_kg + midi * midi_kg)

print("{:.2f}".format(total))

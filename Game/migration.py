import ducksEx

flock = ducksEx.Flock()
donald = ducksEx.Duck()
daisy = ducksEx.Duck()
duck3 = ducksEx.Duck()
duck4 = ducksEx.Duck()
duck5 = ducksEx.Duck()
duck6 = ducksEx.Duck()
duck7 = ducksEx.Duck()
percy = ducksEx.Penguin()

flock.add_duck(donald)
flock.add_duck(daisy)
flock.add_duck(duck3)
flock.add_duck(duck4)
flock.add_duck(percy)
flock.add_duck(duck5)
flock.add_duck(duck6)
flock.add_duck(duck7)

flock.migrate()

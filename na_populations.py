import pygal

wm = pygal.maps.world.World()
wm.title = 'Populations of Countries in Noth America'
wm.add('Noth America', {'ca':34126000, 'us':309349000, 'mx': 113423000})
wm.render_to_file('na_populations.svg')
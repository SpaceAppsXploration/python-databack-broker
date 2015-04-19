__author__ = 'lorenzo@pramantha.net'


CHRONOS_CONTEXT = dict(
    {
        "rdf"         : "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "skos"        : "http://www.w3.org/2004/02/skos/core#",
        "schema"      : "http://schema.org/",
        "dbpedia"     : "http://dbpedia.org/property/",
        "owl"         : "http://www.w3.org/2002/07/owl#",
        "rdfs"        : "http://www.w3.org/2000/01/rdf-schema#",
        "chronos"     : "http://ontology.projectchronos.eu/chronos/",
        "sensor"      : "http://ontology.projectchronos.eu/sensors/",
        "astronomy"   : "http://ontology.projectchronos.eu/astronomy/",
        "engineering" : "http://ontology.projectchronos.eu/engineering/",
        "spacecraft"  : "http://ontology.projectchronos.eu/spacecraft/",
        "xml"         : "http://www.w3.org/2001/XMLSchema#",
        "subsystems"  : "http://ontology.projectchronos.eu/subsystems/",
        "solarsystem" : "http://ontology.projectchronos.eu/solarsystem/"
    }
)

ASTRONOMY_N3 = '''
<http://ontology.projectchronos.eu/astronomy/Asteroid> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
<http://ontology.projectchronos.eu/astronomy/Asteroid> <http://www.w3.org/2000/01/rdf-schema#comment> "a document representing an asteroid" .
<http://ontology.projectchronos.eu/astronomy/Asteroid> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/astronomy> .
<http://ontology.projectchronos.eu/astronomy/Asteroid> <http://www.w3.org/2000/01/rdf-schema#label> "Asteroid" .
<http://ontology.projectchronos.eu/astronomy/Asteroid> <http://www.w3.org/2000/01/rdf-schema#sameAs> <http://umbel.org/umbel/rc/SubplanetaryStellarOrbiter> .
<http://ontology.projectchronos.eu/astronomy/Asteroid> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/ontology/Asteroid" .
<http://ontology.projectchronos.eu/astronomy/AstronomicalObject> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
<http://ontology.projectchronos.eu/astronomy/AstronomicalObject> <http://www.w3.org/2000/01/rdf-schema#comment> "an astronomical body (from a natural satellite size up) or a group of astronomical body" .
<http://ontology.projectchronos.eu/astronomy/AstronomicalObject> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/astronomy> .
<http://ontology.projectchronos.eu/astronomy/AstronomicalObject> <http://www.w3.org/2000/01/rdf-schema#label> "AstronomicalObject" .
<http://ontology.projectchronos.eu/astronomy/AstronomicalObject> <http://www.w3.org/2002/07/owl#sameAs> "http://umbel.org/umbel/rc/AstronomicalObject" .
<http://ontology.projectchronos.eu/astronomy/AstronomicalObservatory> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
<http://ontology.projectchronos.eu/astronomy/AstronomicalObservatory> <http://www.w3.org/2000/01/rdf-schema#comment> "a document representing an astronomical observatory" .
<http://ontology.projectchronos.eu/astronomy/AstronomicalObservatory> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/astronomy> .
<http://ontology.projectchronos.eu/astronomy/AstronomicalObservatory> <http://www.w3.org/2000/01/rdf-schema#label> "AstronomicalObservatory" .
<http://ontology.projectchronos.eu/astronomy/AstronomicalObservatory> <http://www.w3.org/2002/07/owl#sameAs> "http://umbel.org/umbel/rc/AstronomicalObservatory" .
<http://ontology.projectchronos.eu/astronomy/AtmosphericScience> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
<http://ontology.projectchronos.eu/astronomy/AtmosphericScience> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/astronomy> .
<http://ontology.projectchronos.eu/astronomy/AtmosphericScience> <http://www.w3.org/2000/01/rdf-schema#label> "AtmosphericScience" .
<http://ontology.projectchronos.eu/astronomy/AtmosphericScience> <http://www.w3.org/2000/01/rdf-schema#subClassOf> "http://ontology.projectchronos.eu/sensors/PlanetaryScience" .
<http://ontology.projectchronos.eu/astronomy/AtmosphericScience> <http://www.w3.org/2002/07/owl#sameAs> "http://umbel.org/umbel/rc/AtmosphericScience" .
<http://ontology.projectchronos.eu/astronomy/CelestialBody> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
<http://ontology.projectchronos.eu/astronomy/CelestialBody> <http://www.w3.org/2000/01/rdf-schema#comment> "a document representing a generic celestial body" .
<http://ontology.projectchronos.eu/astronomy/CelestialBody> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/astronomy> .
<http://ontology.projectchronos.eu/astronomy/CelestialBody> <http://www.w3.org/2000/01/rdf-schema#label> "CelestialBody" .
<http://ontology.projectchronos.eu/astronomy/CelestialBody> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/ontology/CelestialBody" .
<http://ontology.projectchronos.eu/astronomy/Comet> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
<http://ontology.projectchronos.eu/astronomy/Comet> <http://www.w3.org/2000/01/rdf-schema#comment> "a document representing a comet" .
<http://ontology.projectchronos.eu/astronomy/Comet> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/astronomy> .
<http://ontology.projectchronos.eu/astronomy/Comet> <http://www.w3.org/2000/01/rdf-schema#label> "Comet" .
<http://ontology.projectchronos.eu/astronomy/Comet> <http://www.w3.org/2000/01/rdf-schema#sameAs> <http://umbel.org/umbel/rc/SubplanetaryStellarOrbiter> .
<http://ontology.projectchronos.eu/astronomy/Comet> <http://www.w3.org/2002/07/owl#sameAs> "http://umbel.org/umbel/rc/Comet" .
<http://ontology.projectchronos.eu/astronomy/Cosmology> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
<http://ontology.projectchronos.eu/astronomy/Cosmology> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/astronomy> .
<http://ontology.projectchronos.eu/astronomy/Cosmology> <http://www.w3.org/2000/01/rdf-schema#label> "Cosmology" .
<http://ontology.projectchronos.eu/astronomy/Cosmology> <http://www.w3.org/2000/01/rdf-schema#subClassOf> "http://ontology.projectchronos.eu/sensors/FieldOfResearch" .
<http://ontology.projectchronos.eu/astronomy/Cosmology> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Cosmology" .
<http://ontology.projectchronos.eu/astronomy/Cosmology> <http://www.w3.org/2002/07/owl#sameAs> "http://umbel.org/umbel/rc/Cosmology" .
<http://ontology.projectchronos.eu/astronomy/DwarfPlanet> <@owl:sameAs> "http://dbpedia.org/resource/Dwarf_planet" .
<http://ontology.projectchronos.eu/astronomy/DwarfPlanet> <http://ontology.projectchronos.eu/astronomy/orbiting> <http://ontology.projectchronos.eu/astronomy/Sun> .
<http://ontology.projectchronos.eu/astronomy/DwarfPlanet> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
<http://ontology.projectchronos.eu/astronomy/DwarfPlanet> <http://www.w3.org/2000/01/rdf-schema#comment> "a trans-neptunian object with planet-like size" .
<http://ontology.projectchronos.eu/astronomy/DwarfPlanet> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/astronomy> .
<http://ontology.projectchronos.eu/astronomy/DwarfPlanet> <http://www.w3.org/2000/01/rdf-schema#label> "Dwarfplanet" .
<http://ontology.projectchronos.eu/astronomy/DwarfPlanet> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://umbel.org/umbel/rc/SubplanetaryStellarOrbiter> .
<http://ontology.projectchronos.eu/astronomy/ExtragalacticAstronomy> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
<http://ontology.projectchronos.eu/astronomy/ExtragalacticAstronomy> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/astronomy> .
<http://ontology.projectchronos.eu/astronomy/ExtragalacticAstronomy> <http://www.w3.org/2000/01/rdf-schema#label> "ExtragalacticAstronomy" .
<http://ontology.projectchronos.eu/astronomy/ExtragalacticAstronomy> <http://www.w3.org/2000/01/rdf-schema#subClassOf> "http://ontology.projectchronos.eu/sensors/FieldOfResearch" .
<http://ontology.projectchronos.eu/astronomy/ExtragalacticAstronomy> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Extragalactic_astronomy" .
<http://ontology.projectchronos.eu/astronomy/FluidPlanetaryBody> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
<http://ontology.projectchronos.eu/astronomy/FluidPlanetaryBody> <http://www.w3.org/2000/01/rdf-schema#comment> "a document representing a non-solid planet" .
<http://ontology.projectchronos.eu/astronomy/FluidPlanetaryBody> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/astronomy> .
<http://ontology.projectchronos.eu/astronomy/FluidPlanetaryBody> <http://www.w3.org/2000/01/rdf-schema#label> "FluidPlanetaryBody" .
<http://ontology.projectchronos.eu/astronomy/FluidPlanetaryBody> <http://www.w3.org/2002/07/owl#sameAs> "http://umbel.org/umbel/rc/FluidPlanetaryBody" .
<http://ontology.projectchronos.eu/astronomy/GalacticAstronomy> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
<http://ontology.projectchronos.eu/astronomy/GalacticAstronomy> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/astronomy> .
<http://ontology.projectchronos.eu/astronomy/GalacticAstronomy> <http://www.w3.org/2000/01/rdf-schema#label> "GalacticAstronomy" .
<http://ontology.projectchronos.eu/astronomy/GalacticAstronomy> <http://www.w3.org/2000/01/rdf-schema#subClassOf> "http://ontology.projectchronos.eu/sensors/FieldOfResearch" .
<http://ontology.projectchronos.eu/astronomy/GalacticAstronomy> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Galactic_astronomy" .
<http://ontology.projectchronos.eu/astronomy/GasGiant> <@owl:sameAs> "http://umbel.org/umbel/rc/GasGiant" .
<http://ontology.projectchronos.eu/astronomy/GasGiant> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
<http://ontology.projectchronos.eu/astronomy/GasGiant> <http://www.w3.org/2000/01/rdf-schema#comment> "a Jovian planet, a document representing a Jovian planet" .
<http://ontology.projectchronos.eu/astronomy/GasGiant> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/astronomy> .
<http://ontology.projectchronos.eu/astronomy/GasGiant> <http://www.w3.org/2000/01/rdf-schema#label> "GasGiant" .
<http://ontology.projectchronos.eu/astronomy/Ice_giant> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
<http://ontology.projectchronos.eu/astronomy/Ice_giant> <http://www.w3.org/2000/01/rdf-schema#comment> "a gas giant with less helium/hydrogen and more 'ices', Uranus and Neputne subclass" .
<http://ontology.projectchronos.eu/astronomy/Ice_giant> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/astronomy> .
<http://ontology.projectchronos.eu/astronomy/Ice_giant> <http://www.w3.org/2000/01/rdf-schema#label> "Ice_giant" .
<http://ontology.projectchronos.eu/astronomy/Ice_giant> <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://ontology.projectchronos.eu/astronomy/GasGiant> .
<http://ontology.projectchronos.eu/astronomy/Ice_giant> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Ice_giant" .
<http://ontology.projectchronos.eu/astronomy/IcyPlanetaryBody> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
<http://ontology.projectchronos.eu/astronomy/IcyPlanetaryBody> <http://www.w3.org/2000/01/rdf-schema#comment> "a document representing an icy body" .
<http://ontology.projectchronos.eu/astronomy/IcyPlanetaryBody> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/astronomy> .
<http://ontology.projectchronos.eu/astronomy/IcyPlanetaryBody> <http://www.w3.org/2000/01/rdf-schema#label> "IcyPlanetaryBody" .
<http://ontology.projectchronos.eu/astronomy/IcyPlanetaryBody> <http://www.w3.org/2002/07/owl#sameAs> "http://umbel.org/umbel/rc/IcyPlanetaryBody" .
<http://ontology.projectchronos.eu/astronomy/Meteoroid> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
<http://ontology.projectchronos.eu/astronomy/Meteoroid> <http://www.w3.org/2000/01/rdf-schema#comment> "a document representing a meteoroid" .
<http://ontology.projectchronos.eu/astronomy/Meteoroid> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/astronomy> .
<http://ontology.projectchronos.eu/astronomy/Meteoroid> <http://www.w3.org/2000/01/rdf-schema#label> "Meteoroid" .
<http://ontology.projectchronos.eu/astronomy/Meteoroid> <http://www.w3.org/2000/01/rdf-schema#sameAs> <http://umbel.org/umbel/rc/SubplanetaryStellarOrbiter> .
<http://ontology.projectchronos.eu/astronomy/Meteoroid> <http://www.w3.org/2002/07/owl#sameAs> "http://umbel.org/umbel/rc/Meteoroid" .
<http://ontology.projectchronos.eu/astronomy/Natural_satellite> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
<http://ontology.projectchronos.eu/astronomy/Natural_satellite> <http://www.w3.org/2000/01/rdf-schema#comment> "a document representing a natural satellite or moon" .
<http://ontology.projectchronos.eu/astronomy/Natural_satellite> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/astronomy> .
<http://ontology.projectchronos.eu/astronomy/Natural_satellite> <http://www.w3.org/2000/01/rdf-schema#label> "Natural_satellite" .
<http://ontology.projectchronos.eu/astronomy/Natural_satellite> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Natural_satellite" .
<http://ontology.projectchronos.eu/astronomy/Natural_satellite> <http://www.w3.org/2002/07/owl#sameAs> "http://umbel.org/umbel/rc/MoonOfAPlanet" .
<http://ontology.projectchronos.eu/astronomy/Outer_space> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
<http://ontology.projectchronos.eu/astronomy/Outer_space> <http://www.w3.org/2000/01/rdf-schema#comment> "a document representing the open space outside atmosphere, from Low Earth Orbit to Extra Galactic Space" .
<http://ontology.projectchronos.eu/astronomy/Outer_space> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/astronomy> .
<http://ontology.projectchronos.eu/astronomy/Outer_space> <http://www.w3.org/2000/01/rdf-schema#label> "Outer_space" .
<http://ontology.projectchronos.eu/astronomy/Outer_space> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/ontology/Outer_space" .
<http://ontology.projectchronos.eu/astronomy/PlanetaryBody> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
<http://ontology.projectchronos.eu/astronomy/PlanetaryBody> <http://www.w3.org/2000/01/rdf-schema#comment> "a document representing a general planet-shaped body or natural satellite" .
<http://ontology.projectchronos.eu/astronomy/PlanetaryBody> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/astronomy> .
<http://ontology.projectchronos.eu/astronomy/PlanetaryBody> <http://www.w3.org/2000/01/rdf-schema#label> "PlanetaryBody" .
<http://ontology.projectchronos.eu/astronomy/PlanetaryScience> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
<http://ontology.projectchronos.eu/astronomy/PlanetaryScience> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/astronomy> .
<http://ontology.projectchronos.eu/astronomy/PlanetaryScience> <http://www.w3.org/2000/01/rdf-schema#label> "PlanetaryScience" .
<http://ontology.projectchronos.eu/astronomy/PlanetaryScience> <http://www.w3.org/2000/01/rdf-schema#subClassOf> "http://ontology.projectchronos.eu/sensors/FieldOfResearch" .
<http://ontology.projectchronos.eu/astronomy/PlanetaryScience> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Planetary_science" .
<http://ontology.projectchronos.eu/astronomy/Planetary_system> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
<http://ontology.projectchronos.eu/astronomy/Planetary_system> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/astronomy> .
<http://ontology.projectchronos.eu/astronomy/Planetary_system> <http://www.w3.org/2000/01/rdf-schema#label> "Planetary_system" .
<http://ontology.projectchronos.eu/astronomy/Planetary_system> <http://www.w3.org/2000/01/rdf-schema#subClassOf> "http://ontology.projectchronos.eu/astronomy/AstronomicalObject" .
<http://ontology.projectchronos.eu/astronomy/Planetary_system> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Planetary_system" .
<http://ontology.projectchronos.eu/astronomy/RockyPlanetaryBody> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
<http://ontology.projectchronos.eu/astronomy/RockyPlanetaryBody> <http://www.w3.org/2000/01/rdf-schema#comment> "a document representing a rocky body" .
<http://ontology.projectchronos.eu/astronomy/RockyPlanetaryBody> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/astronomy> .
<http://ontology.projectchronos.eu/astronomy/RockyPlanetaryBody> <http://www.w3.org/2000/01/rdf-schema#label> "RockyPlanetaryBody" .
<http://ontology.projectchronos.eu/astronomy/RockyPlanetaryBody> <http://www.w3.org/2002/07/owl#sameAs> "http://umbel.org/umbel/rc/RockyPlanetaryBody" .
<http://ontology.projectchronos.eu/astronomy/SolidPlanetaryBody> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
<http://ontology.projectchronos.eu/astronomy/SolidPlanetaryBody> <http://www.w3.org/2000/01/rdf-schema#comment> "planet  composed primarily of solid substances" .
<http://ontology.projectchronos.eu/astronomy/SolidPlanetaryBody> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/astronomy> .
<http://ontology.projectchronos.eu/astronomy/SolidPlanetaryBody> <http://www.w3.org/2000/01/rdf-schema#label> "SolidPlanetaryBody" .
<http://ontology.projectchronos.eu/astronomy/SolidPlanetaryBody> <http://www.w3.org/2002/07/owl#sameAs> "http://umbel.org/umbel/rc/SolidPlanetaryBody" .
<http://ontology.projectchronos.eu/astronomy/Star> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
<http://ontology.projectchronos.eu/astronomy/Star> <http://www.w3.org/2000/01/rdf-schema#comment> "a star" .
<http://ontology.projectchronos.eu/astronomy/Star> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/astronomy> .
<http://ontology.projectchronos.eu/astronomy/Star> <http://www.w3.org/2000/01/rdf-schema#label> "Star" .
<http://ontology.projectchronos.eu/astronomy/Star> <http://www.w3.org/2000/01/rdf-schema#subClassOf> "http://ontology.projectchronos.eu/astronomy/AstronomicalObject" .
<http://ontology.projectchronos.eu/astronomy/Star> <http://www.w3.org/2002/07/owl#sameAs> "http://umbel.org/umbel/rc/Star" .
<http://ontology.projectchronos.eu/astronomy/SubplanetaryStellarOrbiter> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
<http://ontology.projectchronos.eu/astronomy/SubplanetaryStellarOrbiter> <http://www.w3.org/2000/01/rdf-schema#comment> "a smaller body orbiting around stars or planets, a document representing smaller body orbiting around stars or planets" .
<http://ontology.projectchronos.eu/astronomy/SubplanetaryStellarOrbiter> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/astronomy> .
<http://ontology.projectchronos.eu/astronomy/SubplanetaryStellarOrbiter> <http://www.w3.org/2000/01/rdf-schema#label> "SubplanetaryStellarOrbiter" .
<http://ontology.projectchronos.eu/astronomy/SubplanetaryStellarOrbiter> <http://www.w3.org/2002/07/owl#sameAs> "http://umbel.org/umbel/rc/SubplanetaryStellarOrbiter" .
<http://ontology.projectchronos.eu/astronomy/TerrestrialPlanet> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
<http://ontology.projectchronos.eu/astronomy/TerrestrialPlanet> <http://www.w3.org/2000/01/rdf-schema#comment> "a document representing a solid/rocky planet" .
<http://ontology.projectchronos.eu/astronomy/TerrestrialPlanet> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/astronomy> .
<http://ontology.projectchronos.eu/astronomy/TerrestrialPlanet> <http://www.w3.org/2000/01/rdf-schema#label> "TerrestrialPlanet" .
<http://ontology.projectchronos.eu/astronomy/TerrestrialPlanet> <http://www.w3.org/2002/07/owl#sameAs> "http://umbel.org/umbel/rc/TerrestrialPlanet" .
<http://ontology.projectchronos.eu/astronomy/orbiting> <http://www.w3.org/1999/02/22-rdf-syntax-ns#domain> "http://ontology.projectchronos.eu/astronomy/AstronomicalObject" .
<http://ontology.projectchronos.eu/astronomy/orbiting> <http://www.w3.org/1999/02/22-rdf-syntax-ns#range> "http://ontology.projectchronos.eu/astronomy/AstronomicalObject" .
<http://ontology.projectchronos.eu/astronomy/orbiting> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#ObjectProperty> .
<http://ontology.projectchronos.eu/astronomy/orbiting> <http://www.w3.org/2000/01/rdf-schema#comment> "this property describe the generic astronomical object-object gravitational interaction" .
<http://ontology.projectchronos.eu/astronomy/orbiting> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/astronomy> .
<http://ontology.projectchronos.eu/astronomy/orbiting> <http://www.w3.org/2000/01/rdf-schema#label> "orbiting" .
<http://ontology.projectchronos.eu/astronomy/orbitsPlanet> <http://www.w3.org/1999/02/22-rdf-syntax-ns#domain> "http://ontology.projectchronos.eu/astronomy/Natural_satellite" .
<http://ontology.projectchronos.eu/astronomy/orbitsPlanet> <http://www.w3.org/1999/02/22-rdf-syntax-ns#range> "http://ontology.projectchronos.eu/astronomy/DwarfPlanet" .
<http://ontology.projectchronos.eu/astronomy/orbitsPlanet> <http://www.w3.org/1999/02/22-rdf-syntax-ns#range> "http://ontology.projectchronos.eu/astronomy/PlanetaryBody" .
<http://ontology.projectchronos.eu/astronomy/orbitsPlanet> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#ObjectProperty> .
<http://ontology.projectchronos.eu/astronomy/orbitsPlanet> <http://www.w3.org/2000/01/rdf-schema#comment> "this property describe the Moon-Planet gravitational interaction" .
<http://ontology.projectchronos.eu/astronomy/orbitsPlanet> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/astronomy> .
<http://ontology.projectchronos.eu/astronomy/orbitsPlanet> <http://www.w3.org/2000/01/rdf-schema#label> "orbitsPlanet" .
<http://ontology.projectchronos.eu/astronomy> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Ontology> .
<http://ontology.projectchronos.eu/astronomy> <http://www.w3.org/2000/01/rdf-schema#comment> "a set of concepts to be used to describe astronomical objects" .
<http://ontology.projectchronos.eu/astronomy> <http://www.w3.org/2000/01/rdf-schema#label> "Generic astronomical concepts " .
<http://ontology.projectchronos.eu/sensors/PlanetaryAstronomy> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
<http://ontology.projectchronos.eu/sensors/PlanetaryAstronomy> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/astronomy> .
<http://ontology.projectchronos.eu/sensors/PlanetaryAstronomy> <http://www.w3.org/2000/01/rdf-schema#label> "PlanetaryAstronomy" .
<http://ontology.projectchronos.eu/sensors/PlanetaryAstronomy> <http://www.w3.org/2000/01/rdf-schema#subClassOf> "http://ontology.projectchronos.eu/sensors/PlanetaryScience" .
<http://ontology.projectchronos.eu/sensors/PlanetaryGeology> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
<http://ontology.projectchronos.eu/sensors/PlanetaryGeology> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/astronomy> .
<http://ontology.projectchronos.eu/sensors/PlanetaryGeology> <http://www.w3.org/2000/01/rdf-schema#label> "PlanetaryGeology" .
<http://ontology.projectchronos.eu/sensors/PlanetaryGeology> <http://www.w3.org/2000/01/rdf-schema#subClassOf> "http://ontology.projectchronos.eu/sensors/PlanetaryScience" .
<http://ontology.projectchronos.eu/sensors/SolarAstronomy> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
<http://ontology.projectchronos.eu/sensors/SolarAstronomy> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/astronomy> .
<http://ontology.projectchronos.eu/sensors/SolarAstronomy> <http://www.w3.org/2000/01/rdf-schema#label> "SolarAstronomy" .
<http://ontology.projectchronos.eu/sensors/SolarAstronomy> <http://www.w3.org/2000/01/rdf-schema#subClassOf> "http://ontology.projectchronos.eu/sensors/FieldOfResearch" .
<http://ontology.projectchronos.eu/sensors/StellarAstronomy> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class> .
<http://ontology.projectchronos.eu/sensors/StellarAstronomy> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/astronomy> .
<http://ontology.projectchronos.eu/sensors/StellarAstronomy> <http://www.w3.org/2000/01/rdf-schema#label> "StellarAstronomy" .
<http://ontology.projectchronos.eu/sensors/StellarAstronomy> <http://www.w3.org/2000/01/rdf-schema#subClassOf> "http://ontology.projectchronos.eu/sensors/FieldOfResearch" .
'''

SOLARSYSTEM_N3 = '''
<http://ontology.projectchronos.eu/solarsystem/Adrastea> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Jupiter" .
<http://ontology.projectchronos.eu/solarsystem/Adrastea> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Adrastea> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Adrastea> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Adrastea> <http://www.w3.org/2000/01/rdf-schema#label> "Adrastea" .
<http://ontology.projectchronos.eu/solarsystem/Adrastea> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Adrastea_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Amalthea> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Jupiter" .
<http://ontology.projectchronos.eu/solarsystem/Amalthea> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Amalthea> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Amalthea> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Amalthea> <http://www.w3.org/2000/01/rdf-schema#label> "Amalthea" .
<http://ontology.projectchronos.eu/solarsystem/Amalthea> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Amalthea_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Ariel> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Uranus" .
<http://ontology.projectchronos.eu/solarsystem/Ariel> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Ariel> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Ariel> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Ariel> <http://www.w3.org/2000/01/rdf-schema#label> "Ariel" .
<http://ontology.projectchronos.eu/solarsystem/Ariel> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Ariel_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Asteroid_belt> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/AstronomicalObject> .
<http://ontology.projectchronos.eu/solarsystem/Asteroid_belt> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Asteroid_belt> <http://www.w3.org/2000/01/rdf-schema#label> "Asteroids_belt" .
<http://ontology.projectchronos.eu/solarsystem/Asteroid_belt> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Asteroid_belt" .
<http://ontology.projectchronos.eu/solarsystem/Asteroid_belt> <http://www.w3.org/2002/07/owl#sameAs> "http://umbel.org/umbel/rc/AsteroidBelt" .
<http://ontology.projectchronos.eu/solarsystem/Belinda> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Uranus" .
<http://ontology.projectchronos.eu/solarsystem/Belinda> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Belinda> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Belinda> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Belinda> <http://www.w3.org/2000/01/rdf-schema#label> "Belinda" .
<http://ontology.projectchronos.eu/solarsystem/Belinda> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Belinda_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Bianca> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Uranus" .
<http://ontology.projectchronos.eu/solarsystem/Bianca> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Bianca> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Bianca> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Bianca> <http://www.w3.org/2000/01/rdf-schema#label> "Bianca" .
<http://ontology.projectchronos.eu/solarsystem/Bianca> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Bianca_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Callisto> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Jupiter" .
<http://ontology.projectchronos.eu/solarsystem/Callisto> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Callisto> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Callisto> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Callisto> <http://www.w3.org/2000/01/rdf-schema#label> "Callisto" .
<http://ontology.projectchronos.eu/solarsystem/Callisto> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Callisto_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Carpo> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Jupiter" .
<http://ontology.projectchronos.eu/solarsystem/Carpo> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Carpo> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Carpo> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Carpo> <http://www.w3.org/2000/01/rdf-schema#label> "Carpo" .
<http://ontology.projectchronos.eu/solarsystem/Carpo> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Carpo_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Ceres> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/DwarfPlanet> .
<http://ontology.projectchronos.eu/solarsystem/Ceres> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Ceres> <http://www.w3.org/2000/01/rdf-schema#label> "Ceres" .
<http://ontology.projectchronos.eu/solarsystem/Ceres> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Ceres_(dwarf_planet)" .
<http://ontology.projectchronos.eu/solarsystem/Charon> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Pluto" .
<http://ontology.projectchronos.eu/solarsystem/Charon> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Charon> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Charon> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Charon> <http://www.w3.org/2000/01/rdf-schema#label> "Charon" .
<http://ontology.projectchronos.eu/solarsystem/Charon> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Charon_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Cordelia> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Uranus" .
<http://ontology.projectchronos.eu/solarsystem/Cordelia> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Cordelia> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Cordelia> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Cordelia> <http://www.w3.org/2000/01/rdf-schema#label> "Cordelia" .
<http://ontology.projectchronos.eu/solarsystem/Cordelia> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Cordelia_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Cressida> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Uranus" .
<http://ontology.projectchronos.eu/solarsystem/Cressida> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Cressida> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Cressida> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Cressida> <http://www.w3.org/2000/01/rdf-schema#label> "Cressida" .
<http://ontology.projectchronos.eu/solarsystem/Cressida> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Cressida_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Cupid> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Uranus" .
<http://ontology.projectchronos.eu/solarsystem/Cupid> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Cupid> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Cupid> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Cupid> <http://www.w3.org/2000/01/rdf-schema#label> "Cupid" .
<http://ontology.projectchronos.eu/solarsystem/Cupid> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Cupid_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Deimos> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Mars" .
<http://ontology.projectchronos.eu/solarsystem/Deimos> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Deimos> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Deimos> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Deimos> <http://www.w3.org/2000/01/rdf-schema#label> "Deimos" .
<http://ontology.projectchronos.eu/solarsystem/Deimos> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Deimos_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Deimos> <http://www.w3.org/2002/07/owl#sameAs> "http://umbel.org/umbel/rc/http://umbel.org/umbel/rc/Deimos_MoonOfMars" .
<http://ontology.projectchronos.eu/solarsystem/Desdemona> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Uranus" .
<http://ontology.projectchronos.eu/solarsystem/Desdemona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Desdemona> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Desdemona> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Desdemona> <http://www.w3.org/2000/01/rdf-schema#label> "Desdemona" .
<http://ontology.projectchronos.eu/solarsystem/Desdemona> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Desdemona_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Despina> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Neptune" .
<http://ontology.projectchronos.eu/solarsystem/Despina> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Despina> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Despina> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Despina> <http://www.w3.org/2000/01/rdf-schema#label> "Despina" .
<http://ontology.projectchronos.eu/solarsystem/Despina> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Despina_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Dione> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Saturn" .
<http://ontology.projectchronos.eu/solarsystem/Dione> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Dione> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Dione> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Dione> <http://www.w3.org/2000/01/rdf-schema#label> "Dione" .
<http://ontology.projectchronos.eu/solarsystem/Dione> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Dione_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Dysnomia> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Eris" .
<http://ontology.projectchronos.eu/solarsystem/Dysnomia> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Dysnomia> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Dysnomia> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Dysnomia> <http://www.w3.org/2000/01/rdf-schema#label> "Dysnomia" .
<http://ontology.projectchronos.eu/solarsystem/Dysnomia> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Dysnomia_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Earth> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/SolidPlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Earth> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/TerrestrialPlanet> .
<http://ontology.projectchronos.eu/solarsystem/Earth> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Earth> <http://www.w3.org/2000/01/rdf-schema#label> "Earth" .
<http://ontology.projectchronos.eu/solarsystem/Earth> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Earth" .
<http://ontology.projectchronos.eu/solarsystem/Earth> <http://www.w3.org/2002/07/owl#sameAs> "http://umbel.org/umbel/rc/PlanetEarth" .
<http://ontology.projectchronos.eu/solarsystem/Elara> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Jupiter" .
<http://ontology.projectchronos.eu/solarsystem/Elara> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Elara> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Elara> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Elara> <http://www.w3.org/2000/01/rdf-schema#label> "Elara" .
<http://ontology.projectchronos.eu/solarsystem/Elara> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Elara_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Enceladus> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Saturn" .
<http://ontology.projectchronos.eu/solarsystem/Enceladus> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Enceladus> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Enceladus> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Enceladus> <http://www.w3.org/2000/01/rdf-schema#label> "Enceladus" .
<http://ontology.projectchronos.eu/solarsystem/Enceladus> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Enceladus_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Eris> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/DwarfPlanet> .
<http://ontology.projectchronos.eu/solarsystem/Eris> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Eris> <http://www.w3.org/2000/01/rdf-schema#label> "Eris" .
<http://ontology.projectchronos.eu/solarsystem/Eris> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Eris_(dwarf_planet)" .
<http://ontology.projectchronos.eu/solarsystem/Euporie> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Jupiter" .
<http://ontology.projectchronos.eu/solarsystem/Euporie> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Euporie> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Euporie> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Euporie> <http://www.w3.org/2000/01/rdf-schema#label> "Euporie" .
<http://ontology.projectchronos.eu/solarsystem/Euporie> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Euporie_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Europa> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Jupiter" .
<http://ontology.projectchronos.eu/solarsystem/Europa> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Europa> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Europa> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Europa> <http://www.w3.org/2000/01/rdf-schema#label> "Europa" .
<http://ontology.projectchronos.eu/solarsystem/Europa> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Europa_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Galatea> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Neptune" .
<http://ontology.projectchronos.eu/solarsystem/Galatea> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Galatea> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Galatea> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Galatea> <http://www.w3.org/2000/01/rdf-schema#label> "Galatea" .
<http://ontology.projectchronos.eu/solarsystem/Galatea> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Galatea_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Ganymede> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Jupiter" .
<http://ontology.projectchronos.eu/solarsystem/Ganymede> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Ganymede> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Ganymede> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Ganymede> <http://www.w3.org/2000/01/rdf-schema#label> "Ganymede" .
<http://ontology.projectchronos.eu/solarsystem/Ganymede> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Ganymede_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Halimede> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Neptune" .
<http://ontology.projectchronos.eu/solarsystem/Halimede> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Halimede> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Halimede> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Halimede> <http://www.w3.org/2000/01/rdf-schema#label> "Halimede" .
<http://ontology.projectchronos.eu/solarsystem/Halimede> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Halimede_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Haumea> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/DwarfPlanet> .
<http://ontology.projectchronos.eu/solarsystem/Haumea> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Haumea> <http://www.w3.org/2000/01/rdf-schema#label> "Haumea" .
<http://ontology.projectchronos.eu/solarsystem/Haumea> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Haumea" .
<http://ontology.projectchronos.eu/solarsystem/Haumea_I_and_II> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Haumea" .
<http://ontology.projectchronos.eu/solarsystem/Haumea_I_and_II> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Haumea_I_and_II> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Haumea_I_and_II> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Haumea_I_and_II> <http://www.w3.org/2000/01/rdf-schema#label> "Haumea_I_and_II" .
<http://ontology.projectchronos.eu/solarsystem/Haumea_I_and_II> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Moons_of_Haumea_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Himalia> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Jupiter" .
<http://ontology.projectchronos.eu/solarsystem/Himalia> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Himalia> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Himalia> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Himalia> <http://www.w3.org/2000/01/rdf-schema#label> "Himalia" .
<http://ontology.projectchronos.eu/solarsystem/Himalia> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Himalia_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Hydra> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Pluto" .
<http://ontology.projectchronos.eu/solarsystem/Hydra> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Hydra> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Hydra> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Hydra> <http://www.w3.org/2000/01/rdf-schema#label> "Hydra" .
<http://ontology.projectchronos.eu/solarsystem/Hydra> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Hydra_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Iapetus> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Saturn" .
<http://ontology.projectchronos.eu/solarsystem/Iapetus> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Iapetus> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Iapetus> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Iapetus> <http://www.w3.org/2000/01/rdf-schema#label> "Iapetus" .
<http://ontology.projectchronos.eu/solarsystem/Iapetus> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Iapetus_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Io> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Jupiter" .
<http://ontology.projectchronos.eu/solarsystem/Io> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Io> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Io> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Io> <http://www.w3.org/2000/01/rdf-schema#label> "Io" .
<http://ontology.projectchronos.eu/solarsystem/Io> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Io_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Juliet> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Uranus" .
<http://ontology.projectchronos.eu/solarsystem/Juliet> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Juliet> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Juliet> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Juliet> <http://www.w3.org/2000/01/rdf-schema#label> "Juliet" .
<http://ontology.projectchronos.eu/solarsystem/Juliet> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Juliet_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Jupiter> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/GasGiant> .
<http://ontology.projectchronos.eu/solarsystem/Jupiter> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Jupiter> <http://www.w3.org/2000/01/rdf-schema#label> "Jupiter" .
<http://ontology.projectchronos.eu/solarsystem/Jupiter> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Mars" .
<http://ontology.projectchronos.eu/solarsystem/Jupiter> <http://www.w3.org/2002/07/owl#sameAs> "http://umbel.org/umbel/rc/PlanetMars" .
<http://ontology.projectchronos.eu/solarsystem/Kerberos> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Pluto" .
<http://ontology.projectchronos.eu/solarsystem/Kerberos> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Kerberos> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Kerberos> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Kerberos> <http://www.w3.org/2000/01/rdf-schema#label> "Kerberos" .
<http://ontology.projectchronos.eu/solarsystem/Kerberos> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Kerberos_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Kuiper_belt> <http://ontology.projectchronos.eu/astronomy/orbits> "http://ontology.projectchronos.eu/solarsystem/Sun" .
<http://ontology.projectchronos.eu/solarsystem/Kuiper_belt> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/AstronomicalObject> .
<http://ontology.projectchronos.eu/solarsystem/Kuiper_belt> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Kuiper_belt> <http://www.w3.org/2000/01/rdf-schema#label> "Kuiper_belt" .
<http://ontology.projectchronos.eu/solarsystem/Kuiper_belt> <http://www.w3.org/2000/01/rdf-schema#subClassOf> "http://ontology.projectchronos.eu/solarsystem/Trans-Neptunian_object" .
<http://ontology.projectchronos.eu/solarsystem/Kuiper_belt> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Kuiper_belt" .
<http://ontology.projectchronos.eu/solarsystem/Laomedeia> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Neptune" .
<http://ontology.projectchronos.eu/solarsystem/Laomedeia> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Laomedeia> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Laomedeia> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Laomedeia> <http://www.w3.org/2000/01/rdf-schema#label> "Laomedeia" .
<http://ontology.projectchronos.eu/solarsystem/Laomedeia> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Laomedeia_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Larissa> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Neptune" .
<http://ontology.projectchronos.eu/solarsystem/Larissa> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Larissa> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Larissa> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Larissa> <http://www.w3.org/2000/01/rdf-schema#label> "Larissa" .
<http://ontology.projectchronos.eu/solarsystem/Larissa> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Larissa_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Leda> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Jupiter" .
<http://ontology.projectchronos.eu/solarsystem/Leda> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Leda> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Leda> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Leda> <http://www.w3.org/2000/01/rdf-schema#label> "Leda" .
<http://ontology.projectchronos.eu/solarsystem/Leda> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Leda_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Lysithea> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Jupiter" .
<http://ontology.projectchronos.eu/solarsystem/Lysithea> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Lysithea> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Lysithea> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Lysithea> <http://www.w3.org/2000/01/rdf-schema#label> "Lysithea" .
<http://ontology.projectchronos.eu/solarsystem/Lysithea> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Lysithea_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Mab> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Uranus" .
<http://ontology.projectchronos.eu/solarsystem/Mab> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Mab> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Mab> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Mab> <http://www.w3.org/2000/01/rdf-schema#label> "Mab" .
<http://ontology.projectchronos.eu/solarsystem/Mab> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Mab_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Makemake> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/DwarfPlanet> .
<http://ontology.projectchronos.eu/solarsystem/Makemake> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Makemake> <http://www.w3.org/2000/01/rdf-schema#label> "Makemake" .
<http://ontology.projectchronos.eu/solarsystem/Makemake> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Makemake" .
<http://ontology.projectchronos.eu/solarsystem/Mars> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/SolidPlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Mars> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/TerrestrialPlanet> .
<http://ontology.projectchronos.eu/solarsystem/Mars> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Mars> <http://www.w3.org/2000/01/rdf-schema#label> "Mars" .
<http://ontology.projectchronos.eu/solarsystem/Mars> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Mars" .
<http://ontology.projectchronos.eu/solarsystem/Mars> <http://www.w3.org/2002/07/owl#sameAs> "http://umbel.org/umbel/rc/PlanetMars" .
<http://ontology.projectchronos.eu/solarsystem/Mercury> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/SolidPlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Mercury> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/TerrestrialPlanet> .
<http://ontology.projectchronos.eu/solarsystem/Mercury> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Mercury> <http://www.w3.org/2000/01/rdf-schema#label> "Mercury" .
<http://ontology.projectchronos.eu/solarsystem/Mercury> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Mercury_(planet)" .
<http://ontology.projectchronos.eu/solarsystem/Mercury> <http://www.w3.org/2002/07/owl#sameAs> "http://umbel.org/umbel/rc/PlanetMercury" .
<http://ontology.projectchronos.eu/solarsystem/Metis> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Jupiter" .
<http://ontology.projectchronos.eu/solarsystem/Metis> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Metis> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Metis> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Metis> <http://www.w3.org/2000/01/rdf-schema#label> "Metis" .
<http://ontology.projectchronos.eu/solarsystem/Metis> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Metis_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Mimas> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Saturn" .
<http://ontology.projectchronos.eu/solarsystem/Mimas> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Mimas> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Mimas> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Mimas> <http://www.w3.org/2000/01/rdf-schema#label> "Mimas" .
<http://ontology.projectchronos.eu/solarsystem/Mimas> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Mimas_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Miranda> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Uranus" .
<http://ontology.projectchronos.eu/solarsystem/Miranda> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Miranda> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Miranda> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Miranda> <http://www.w3.org/2000/01/rdf-schema#label> "Miranda" .
<http://ontology.projectchronos.eu/solarsystem/Miranda> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Miranda_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Moon> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Earth" .
<http://ontology.projectchronos.eu/solarsystem/Moon> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Moon> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Moon> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Moon> <http://www.w3.org/2000/01/rdf-schema#label> "Moon" .
<http://ontology.projectchronos.eu/solarsystem/Moon> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Moon" .
<http://ontology.projectchronos.eu/solarsystem/Moon> <http://www.w3.org/2002/07/owl#sameAs> "http://umbel.org/umbel/rc/MoonOfEarth" .
<http://ontology.projectchronos.eu/solarsystem/Naiad> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Neptune" .
<http://ontology.projectchronos.eu/solarsystem/Naiad> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Naiad> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Naiad> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Naiad> <http://www.w3.org/2000/01/rdf-schema#label> "Naiad" .
<http://ontology.projectchronos.eu/solarsystem/Naiad> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Naiad_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Neptune> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/GasGiant> .
<http://ontology.projectchronos.eu/solarsystem/Neptune> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Ice_giant> .
<http://ontology.projectchronos.eu/solarsystem/Neptune> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Neptune> <http://www.w3.org/2000/01/rdf-schema#label> "Neptune" .
<http://ontology.projectchronos.eu/solarsystem/Neptune> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Neptune" .
<http://ontology.projectchronos.eu/solarsystem/Neptune> <http://www.w3.org/2002/07/owl#sameAs> "http://umbel.org/umbel/rc/PlanetNeptune" .
<http://ontology.projectchronos.eu/solarsystem/Nereid> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Neptune" .
<http://ontology.projectchronos.eu/solarsystem/Nereid> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Nereid> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Nereid> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Nereid> <http://www.w3.org/2000/01/rdf-schema#label> "Nereid" .
<http://ontology.projectchronos.eu/solarsystem/Nereid> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Nereid_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Neso> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Neptune" .
<http://ontology.projectchronos.eu/solarsystem/Neso> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Neso> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Neso> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Neso> <http://www.w3.org/2000/01/rdf-schema#label> "Neso" .
<http://ontology.projectchronos.eu/solarsystem/Neso> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Neso_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Nix> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Pluto" .
<http://ontology.projectchronos.eu/solarsystem/Nix> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Nix> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Nix> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Nix> <http://www.w3.org/2000/01/rdf-schema#label> "Nix" .
<http://ontology.projectchronos.eu/solarsystem/Nix> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Nix_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Oberon> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Uranus" .
<http://ontology.projectchronos.eu/solarsystem/Oberon> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Oberon> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Oberon> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Oberon> <http://www.w3.org/2000/01/rdf-schema#label> "Oberon" .
<http://ontology.projectchronos.eu/solarsystem/Oberon> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Oberon_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Oort_cloud> <http://ontology.projectchronos.eu/astronomy/orbits> "http://ontology.projectchronos.eu/solarsystem/Sun" .
<http://ontology.projectchronos.eu/solarsystem/Oort_cloud> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/AstronomicalObject> .
<http://ontology.projectchronos.eu/solarsystem/Oort_cloud> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Oort_cloud> <http://www.w3.org/2000/01/rdf-schema#label> "Oort_cloud" .
<http://ontology.projectchronos.eu/solarsystem/Oort_cloud> <http://www.w3.org/2000/01/rdf-schema#subClassOf> "http://ontology.projectchronos.eu/solarsystem/Trans-Neptunian_object" .
<http://ontology.projectchronos.eu/solarsystem/Oort_cloud> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Oort_cloud" .
<http://ontology.projectchronos.eu/solarsystem/Ophelia> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Uranus" .
<http://ontology.projectchronos.eu/solarsystem/Ophelia> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Ophelia> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Ophelia> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Ophelia> <http://www.w3.org/2000/01/rdf-schema#label> "Ophelia" .
<http://ontology.projectchronos.eu/solarsystem/Ophelia> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Ophelia_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/OtherMoonsOfJupiter> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Jupiter" .
<http://ontology.projectchronos.eu/solarsystem/OtherMoonsOfJupiter> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/OtherMoonsOfJupiter> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/OtherMoonsOfJupiter> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/OtherMoonsOfJupiter> <http://www.w3.org/2000/01/rdf-schema#label> "OtherMoonsOfJupiter" .
<http://ontology.projectchronos.eu/solarsystem/OtherMoonsOfJupiter> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Moons_of_Jupiter" .
<http://ontology.projectchronos.eu/solarsystem/Perdita> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Uranus" .
<http://ontology.projectchronos.eu/solarsystem/Perdita> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Perdita> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Perdita> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Perdita> <http://www.w3.org/2000/01/rdf-schema#label> "Perdita" .
<http://ontology.projectchronos.eu/solarsystem/Perdita> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Perdita_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Phobos> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Mars" .
<http://ontology.projectchronos.eu/solarsystem/Phobos> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Phobos> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Phobos> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Phobos> <http://www.w3.org/2000/01/rdf-schema#label> "Phobos" .
<http://ontology.projectchronos.eu/solarsystem/Phobos> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Phobos_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Phobos> <http://www.w3.org/2002/07/owl#sameAs> "http://umbel.org/umbel/rc/http://umbel.org/umbel/rc/Phobos_MoonOfMars" .
<http://ontology.projectchronos.eu/solarsystem/Pluto> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/DwarfPlanet> .
<http://ontology.projectchronos.eu/solarsystem/Pluto> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Pluto> <http://www.w3.org/2000/01/rdf-schema#label> "Pluto" .
<http://ontology.projectchronos.eu/solarsystem/Pluto> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Pluto" .
<http://ontology.projectchronos.eu/solarsystem/Portia> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Uranus" .
<http://ontology.projectchronos.eu/solarsystem/Portia> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Portia> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Portia> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Portia> <http://www.w3.org/2000/01/rdf-schema#label> "Portia" .
<http://ontology.projectchronos.eu/solarsystem/Portia> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Portia_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Proteus> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Neptune" .
<http://ontology.projectchronos.eu/solarsystem/Proteus> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Proteus> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Proteus> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Proteus> <http://www.w3.org/2000/01/rdf-schema#label> "Proteus" .
<http://ontology.projectchronos.eu/solarsystem/Proteus> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Proteus_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Psamathe> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Neptune" .
<http://ontology.projectchronos.eu/solarsystem/Psamathe> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Psamathe> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Psamathe> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Psamathe> <http://www.w3.org/2000/01/rdf-schema#label> "Psamathe" .
<http://ontology.projectchronos.eu/solarsystem/Psamathe> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Psamathe_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Puck> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Uranus" .
<http://ontology.projectchronos.eu/solarsystem/Puck> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Puck> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Puck> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Puck> <http://www.w3.org/2000/01/rdf-schema#label> "Puck" .
<http://ontology.projectchronos.eu/solarsystem/Puck> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Puck_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Rhea> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Saturn" .
<http://ontology.projectchronos.eu/solarsystem/Rhea> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Rhea> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Rhea> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Rhea> <http://www.w3.org/2000/01/rdf-schema#label> "Rhea" .
<http://ontology.projectchronos.eu/solarsystem/Rhea> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Rhea_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Rosalind> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Uranus" .
<http://ontology.projectchronos.eu/solarsystem/Rosalind> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Rosalind> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Rosalind> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Rosalind> <http://www.w3.org/2000/01/rdf-schema#label> "Rosalind" .
<http://ontology.projectchronos.eu/solarsystem/Rosalind> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Rosalind_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Sao> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Neptune" .
<http://ontology.projectchronos.eu/solarsystem/Sao> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Sao> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Sao> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Sao> <http://www.w3.org/2000/01/rdf-schema#label> "Sao" .
<http://ontology.projectchronos.eu/solarsystem/Sao> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Sao_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Saturn> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/GasGiant> .
<http://ontology.projectchronos.eu/solarsystem/Saturn> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Saturn> <http://www.w3.org/2000/01/rdf-schema#label> "Saturn" .
<http://ontology.projectchronos.eu/solarsystem/Saturn> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Saturn" .
<http://ontology.projectchronos.eu/solarsystem/Saturn> <http://www.w3.org/2002/07/owl#sameAs> "http://umbel.org/umbel/rc/PlanetSaturn" .
<http://ontology.projectchronos.eu/solarsystem/Solar_System> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Planetary_system> .
<http://ontology.projectchronos.eu/solarsystem/Solar_System> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Solar_System> <http://www.w3.org/2000/01/rdf-schema#label> "Solar_System" .
<http://ontology.projectchronos.eu/solarsystem/Solar_System> <http://www.w3.org/2002/07/owl#sameAs> "http://umbel.org/umbel/rc/SolarSystem" .
<http://ontology.projectchronos.eu/solarsystem/Styx> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Pluto" .
<http://ontology.projectchronos.eu/solarsystem/Styx> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Styx> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Styx> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Styx> <http://www.w3.org/2000/01/rdf-schema#label> "Styx" .
<http://ontology.projectchronos.eu/solarsystem/Styx> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Styx_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Sun> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Star> .
<http://ontology.projectchronos.eu/solarsystem/Sun> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Sun> <http://www.w3.org/2000/01/rdf-schema#label> "The Sun" .
<http://ontology.projectchronos.eu/solarsystem/Thalassa> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Neptune" .
<http://ontology.projectchronos.eu/solarsystem/Thalassa> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Thalassa> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Thalassa> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Thalassa> <http://www.w3.org/2000/01/rdf-schema#label> "Thalassa" .
<http://ontology.projectchronos.eu/solarsystem/Thalassa> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Thalassa_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Thebe> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Jupiter" .
<http://ontology.projectchronos.eu/solarsystem/Thebe> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Thebe> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Thebe> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Thebe> <http://www.w3.org/2000/01/rdf-schema#label> "Thebe" .
<http://ontology.projectchronos.eu/solarsystem/Thebe> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Thebe_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Themisto> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Jupiter" .
<http://ontology.projectchronos.eu/solarsystem/Themisto> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Themisto> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Themisto> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Themisto> <http://www.w3.org/2000/01/rdf-schema#label> "Themisto" .
<http://ontology.projectchronos.eu/solarsystem/Themisto> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Themisto_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Thetys> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Saturn" .
<http://ontology.projectchronos.eu/solarsystem/Thetys> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Thetys> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Thetys> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Thetys> <http://www.w3.org/2000/01/rdf-schema#label> "Thetys" .
<http://ontology.projectchronos.eu/solarsystem/Thetys> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Thetys_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Titan> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Saturn" .
<http://ontology.projectchronos.eu/solarsystem/Titan> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Titan> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Titan> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Titan> <http://www.w3.org/2000/01/rdf-schema#label> "Titan" .
<http://ontology.projectchronos.eu/solarsystem/Titan> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Titan_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Titania> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Uranus" .
<http://ontology.projectchronos.eu/solarsystem/Titania> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Titania> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Titania> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Titania> <http://www.w3.org/2000/01/rdf-schema#label> "Titania" .
<http://ontology.projectchronos.eu/solarsystem/Titania> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Titania_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Trans-Neptunian_object> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/AstronomicalObject> .
<http://ontology.projectchronos.eu/solarsystem/Trans-Neptunian_object> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Trans-Neptunian_object> <http://www.w3.org/2000/01/rdf-schema#label> "Trans-Neptunian_object" .
<http://ontology.projectchronos.eu/solarsystem/Trans-Neptunian_object> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Trans-Neptunian_object" .
<http://ontology.projectchronos.eu/solarsystem/Triton> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Neptune" .
<http://ontology.projectchronos.eu/solarsystem/Triton> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Triton> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Triton> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Triton> <http://www.w3.org/2000/01/rdf-schema#label> "Triton" .
<http://ontology.projectchronos.eu/solarsystem/Triton> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Triton_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Umbriel> <http://ontology.projectchronos.eu/astronomy/orbitsPlanet> "http://ontology.projectchronos.eu/solarsystem/Uranus" .
<http://ontology.projectchronos.eu/solarsystem/Umbriel> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Natural_satellite> .
<http://ontology.projectchronos.eu/solarsystem/Umbriel> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/PlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Umbriel> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Umbriel> <http://www.w3.org/2000/01/rdf-schema#label> "Umbriel" .
<http://ontology.projectchronos.eu/solarsystem/Umbriel> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Umbriel_(moon)" .
<http://ontology.projectchronos.eu/solarsystem/Uranus> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/GasGiant> .
<http://ontology.projectchronos.eu/solarsystem/Uranus> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/Ice_giant> .
<http://ontology.projectchronos.eu/solarsystem/Uranus> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Uranus> <http://www.w3.org/2000/01/rdf-schema#label> "Uranus" .
<http://ontology.projectchronos.eu/solarsystem/Uranus> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Uranus" .
<http://ontology.projectchronos.eu/solarsystem/Uranus> <http://www.w3.org/2002/07/owl#sameAs> "http://umbel.org/umbel/rc/PlanetUranus" .
<http://ontology.projectchronos.eu/solarsystem/Venus> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/SolidPlanetaryBody> .
<http://ontology.projectchronos.eu/solarsystem/Venus> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://ontology.projectchronos.eu/astronomy/TerrestrialPlanet> .
<http://ontology.projectchronos.eu/solarsystem/Venus> <http://www.w3.org/2000/01/rdf-schema#isDefinedBy> <http://ontology.projectchronos.eu/solarsystem> .
<http://ontology.projectchronos.eu/solarsystem/Venus> <http://www.w3.org/2000/01/rdf-schema#label> "Venus" .
<http://ontology.projectchronos.eu/solarsystem/Venus> <http://www.w3.org/2002/07/owl#sameAs> "http://dbpedia.org/resource/Venus_(planet)" .
<http://ontology.projectchronos.eu/solarsystem/Venus> <http://www.w3.org/2002/07/owl#sameAs> "http://umbel.org/umbel/rc/PlanetVenus" .
<http://ontology.projectchronos.eu/solarsystem> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Ontology> .
<http://ontology.projectchronos.eu/solarsystem> <http://www.w3.org/2000/01/rdf-schema#comment> "The major Astronomical Bodies in the Solar System are described in terms of what orbits what" .
<http://ontology.projectchronos.eu/solarsystem> <http://www.w3.org/2000/01/rdf-schema#label> "A description of the Solar System taking major classes from DBpedia and Umbel" .
'''

ASTRONOMY_FLATTENED = {
  "@graph": [
    {
      "@id": "http://ontology.projectchronos.eu/astronomy",
      "@type": "http://www.w3.org/2002/07/owl#Ontology",
      "http://www.w3.org/2000/01/rdf-schema#comment": "a set of concepts to be used to describe astronomical objects",
      "http://www.w3.org/2000/01/rdf-schema#label": "Generic astronomical concepts "
    },
    {
      "@id": "http://ontology.projectchronos.eu/astronomy/Asteroid",
      "@type": "http://www.w3.org/2002/07/owl#Class",
      "http://www.w3.org/2000/01/rdf-schema#comment": "a document representing an asteroid",
      "http://www.w3.org/2000/01/rdf-schema#isDefinedBy": {
        "@id": "http://ontology.projectchronos.eu/astronomy"
      },
      "http://www.w3.org/2000/01/rdf-schema#label": "Asteroid",
      "http://www.w3.org/2000/01/rdf-schema#sameAs": {
        "@id": "http://umbel.org/umbel/rc/SubplanetaryStellarOrbiter"
      },
      "http://www.w3.org/2002/07/owl#sameAs": "http://dbpedia.org/ontology/Asteroid"
    },
    {
      "@id": "http://ontology.projectchronos.eu/astronomy/AstronomicalObject",
      "@type": "http://www.w3.org/2002/07/owl#Class",
      "http://www.w3.org/2000/01/rdf-schema#comment": "an astronomical body (from a natural satellite size up) or a group of astronomical body",
      "http://www.w3.org/2000/01/rdf-schema#isDefinedBy": {
        "@id": "http://ontology.projectchronos.eu/astronomy"
      },
      "http://www.w3.org/2000/01/rdf-schema#label": "AstronomicalObject",
      "http://www.w3.org/2002/07/owl#sameAs": "http://umbel.org/umbel/rc/AstronomicalObject"
    },
    {
      "@id": "http://ontology.projectchronos.eu/astronomy/AstronomicalObservatory",
      "@type": "http://www.w3.org/2002/07/owl#Class",
      "http://www.w3.org/2000/01/rdf-schema#comment": "a document representing an astronomical observatory",
      "http://www.w3.org/2000/01/rdf-schema#isDefinedBy": {
        "@id": "http://ontology.projectchronos.eu/astronomy"
      },
      "http://www.w3.org/2000/01/rdf-schema#label": "AstronomicalObservatory",
      "http://www.w3.org/2002/07/owl#sameAs": "http://umbel.org/umbel/rc/AstronomicalObservatory"
    },
    {
      "@id": "http://ontology.projectchronos.eu/astronomy/AtmosphericScience",
      "@type": "http://www.w3.org/2002/07/owl#Class",
      "http://www.w3.org/2000/01/rdf-schema#isDefinedBy": {
        "@id": "http://ontology.projectchronos.eu/astronomy"
      },
      "http://www.w3.org/2000/01/rdf-schema#label": "AtmosphericScience",
      "http://www.w3.org/2000/01/rdf-schema#subClassOf": "http://ontology.projectchronos.eu/sensors/PlanetaryScience",
      "http://www.w3.org/2002/07/owl#sameAs": "http://umbel.org/umbel/rc/AtmosphericScience"
    },
    {
      "@id": "http://ontology.projectchronos.eu/astronomy/CelestialBody",
      "@type": "http://www.w3.org/2002/07/owl#Class",
      "http://www.w3.org/2000/01/rdf-schema#comment": "a document representing a generic celestial body",
      "http://www.w3.org/2000/01/rdf-schema#isDefinedBy": {
        "@id": "http://ontology.projectchronos.eu/astronomy"
      },
      "http://www.w3.org/2000/01/rdf-schema#label": "CelestialBody",
      "http://www.w3.org/2002/07/owl#sameAs": "http://dbpedia.org/ontology/CelestialBody"
    },
    {
      "@id": "http://ontology.projectchronos.eu/astronomy/Comet",
      "@type": "http://www.w3.org/2002/07/owl#Class",
      "http://www.w3.org/2000/01/rdf-schema#comment": "a document representing a comet",
      "http://www.w3.org/2000/01/rdf-schema#isDefinedBy": {
        "@id": "http://ontology.projectchronos.eu/astronomy"
      },
      "http://www.w3.org/2000/01/rdf-schema#label": "Comet",
      "http://www.w3.org/2000/01/rdf-schema#sameAs": {
        "@id": "http://umbel.org/umbel/rc/SubplanetaryStellarOrbiter"
      },
      "http://www.w3.org/2002/07/owl#sameAs": "http://umbel.org/umbel/rc/Comet"
    },
    {
      "@id": "http://ontology.projectchronos.eu/astronomy/Cosmology",
      "@type": "http://www.w3.org/2002/07/owl#Class",
      "http://www.w3.org/2000/01/rdf-schema#isDefinedBy": {
        "@id": "http://ontology.projectchronos.eu/astronomy"
      },
      "http://www.w3.org/2000/01/rdf-schema#label": "Cosmology",
      "http://www.w3.org/2000/01/rdf-schema#subClassOf": "http://ontology.projectchronos.eu/sensors/FieldOfResearch",
      "http://www.w3.org/2002/07/owl#sameAs": [
        "http://umbel.org/umbel/rc/Cosmology",
        "http://dbpedia.org/resource/Cosmology"
      ]
    },
    {
      "@id": "http://ontology.projectchronos.eu/astronomy/DwarfPlanet",
      "@owl:sameAs": "http://dbpedia.org/resource/Dwarf_planet",
      "@type": "http://www.w3.org/2002/07/owl#Class",
      "http://ontology.projectchronos.eu/astronomy/orbiting": {
        "@id": "http://ontology.projectchronos.eu/astronomy/Sun"
      },
      "http://www.w3.org/2000/01/rdf-schema#comment": "a trans-neptunian object with planet-like size",
      "http://www.w3.org/2000/01/rdf-schema#isDefinedBy": {
        "@id": "http://ontology.projectchronos.eu/astronomy"
      },
      "http://www.w3.org/2000/01/rdf-schema#label": "Dwarfplanet",
      "http://www.w3.org/2000/01/rdf-schema#subClassOf": {
        "@id": "http://umbel.org/umbel/rc/SubplanetaryStellarOrbiter"
      }
    },
    {
      "@id": "http://ontology.projectchronos.eu/astronomy/ExtragalacticAstronomy",
      "@type": "http://www.w3.org/2002/07/owl#Class",
      "http://www.w3.org/2000/01/rdf-schema#isDefinedBy": {
        "@id": "http://ontology.projectchronos.eu/astronomy"
      },
      "http://www.w3.org/2000/01/rdf-schema#label": "ExtragalacticAstronomy",
      "http://www.w3.org/2000/01/rdf-schema#subClassOf": "http://ontology.projectchronos.eu/sensors/FieldOfResearch",
      "http://www.w3.org/2002/07/owl#sameAs": "http://dbpedia.org/resource/Extragalactic_astronomy"
    },
    {
      "@id": "http://ontology.projectchronos.eu/astronomy/FluidPlanetaryBody",
      "@type": "http://www.w3.org/2002/07/owl#Class",
      "http://www.w3.org/2000/01/rdf-schema#comment": "a document representing a non-solid planet",
      "http://www.w3.org/2000/01/rdf-schema#isDefinedBy": {
        "@id": "http://ontology.projectchronos.eu/astronomy"
      },
      "http://www.w3.org/2000/01/rdf-schema#label": "FluidPlanetaryBody",
      "http://www.w3.org/2002/07/owl#sameAs": "http://umbel.org/umbel/rc/FluidPlanetaryBody"
    },
    {
      "@id": "http://ontology.projectchronos.eu/astronomy/GalacticAstronomy",
      "@type": "http://www.w3.org/2002/07/owl#Class",
      "http://www.w3.org/2000/01/rdf-schema#isDefinedBy": {
        "@id": "http://ontology.projectchronos.eu/astronomy"
      },
      "http://www.w3.org/2000/01/rdf-schema#label": "GalacticAstronomy",
      "http://www.w3.org/2000/01/rdf-schema#subClassOf": "http://ontology.projectchronos.eu/sensors/FieldOfResearch",
      "http://www.w3.org/2002/07/owl#sameAs": "http://dbpedia.org/resource/Galactic_astronomy"
    },
    {
      "@id": "http://ontology.projectchronos.eu/astronomy/GasGiant",
      "@owl:sameAs": "http://umbel.org/umbel/rc/GasGiant",
      "@type": "http://www.w3.org/2002/07/owl#Class",
      "http://www.w3.org/2000/01/rdf-schema#comment": "a Jovian planet, a document representing a Jovian planet",
      "http://www.w3.org/2000/01/rdf-schema#isDefinedBy": {
        "@id": "http://ontology.projectchronos.eu/astronomy"
      },
      "http://www.w3.org/2000/01/rdf-schema#label": "GasGiant"
    },
    {
      "@id": "http://ontology.projectchronos.eu/astronomy/Ice_giant",
      "@type": "http://www.w3.org/2002/07/owl#Class",
      "http://www.w3.org/2000/01/rdf-schema#comment": "a gas giant with less helium/hydrogen and more 'ices', Uranus and Neputne subclass",
      "http://www.w3.org/2000/01/rdf-schema#isDefinedBy": {
        "@id": "http://ontology.projectchronos.eu/astronomy"
      },
      "http://www.w3.org/2000/01/rdf-schema#label": "Ice_giant",
      "http://www.w3.org/2000/01/rdf-schema#subClassOf": {
        "@id": "http://ontology.projectchronos.eu/astronomy/GasGiant"
      },
      "http://www.w3.org/2002/07/owl#sameAs": "http://dbpedia.org/resource/Ice_giant"
    },
    {
      "@id": "http://ontology.projectchronos.eu/astronomy/IcyPlanetaryBody",
      "@type": "http://www.w3.org/2002/07/owl#Class",
      "http://www.w3.org/2000/01/rdf-schema#comment": "a document representing an icy body",
      "http://www.w3.org/2000/01/rdf-schema#isDefinedBy": {
        "@id": "http://ontology.projectchronos.eu/astronomy"
      },
      "http://www.w3.org/2000/01/rdf-schema#label": "IcyPlanetaryBody",
      "http://www.w3.org/2002/07/owl#sameAs": "http://umbel.org/umbel/rc/IcyPlanetaryBody"
    },
    {
      "@id": "http://ontology.projectchronos.eu/astronomy/Meteoroid",
      "@type": "http://www.w3.org/2002/07/owl#Class",
      "http://www.w3.org/2000/01/rdf-schema#comment": "a document representing a meteoroid",
      "http://www.w3.org/2000/01/rdf-schema#isDefinedBy": {
        "@id": "http://ontology.projectchronos.eu/astronomy"
      },
      "http://www.w3.org/2000/01/rdf-schema#label": "Meteoroid",
      "http://www.w3.org/2000/01/rdf-schema#sameAs": {
        "@id": "http://umbel.org/umbel/rc/SubplanetaryStellarOrbiter"
      },
      "http://www.w3.org/2002/07/owl#sameAs": "http://umbel.org/umbel/rc/Meteoroid"
    },
    {
      "@id": "http://ontology.projectchronos.eu/astronomy/Natural_satellite",
      "@type": "http://www.w3.org/2002/07/owl#Class",
      "http://www.w3.org/2000/01/rdf-schema#comment": "a document representing a natural satellite or moon",
      "http://www.w3.org/2000/01/rdf-schema#isDefinedBy": {
        "@id": "http://ontology.projectchronos.eu/astronomy"
      },
      "http://www.w3.org/2000/01/rdf-schema#label": "Natural_satellite",
      "http://www.w3.org/2002/07/owl#sameAs": [
        "http://umbel.org/umbel/rc/MoonOfAPlanet",
        "http://dbpedia.org/resource/Natural_satellite"
      ]
    },
    {
      "@id": "http://ontology.projectchronos.eu/astronomy/Outer_space",
      "@type": "http://www.w3.org/2002/07/owl#Class",
      "http://www.w3.org/2000/01/rdf-schema#comment": "a document representing the open space outside atmosphere, from Low Earth Orbit to Extra Galactic Space",
      "http://www.w3.org/2000/01/rdf-schema#isDefinedBy": {
        "@id": "http://ontology.projectchronos.eu/astronomy"
      },
      "http://www.w3.org/2000/01/rdf-schema#label": "Outer_space",
      "http://www.w3.org/2002/07/owl#sameAs": "http://dbpedia.org/ontology/Outer_space"
    },
    {
      "@id": "http://ontology.projectchronos.eu/astronomy/PlanetaryBody",
      "@type": "http://www.w3.org/2002/07/owl#Class",
      "http://www.w3.org/2000/01/rdf-schema#comment": "a document representing a general planet-shaped body or natural satellite",
      "http://www.w3.org/2000/01/rdf-schema#isDefinedBy": {
        "@id": "http://ontology.projectchronos.eu/astronomy"
      },
      "http://www.w3.org/2000/01/rdf-schema#label": "PlanetaryBody"
    },
    {
      "@id": "http://ontology.projectchronos.eu/astronomy/PlanetaryScience",
      "@type": "http://www.w3.org/2002/07/owl#Class",
      "http://www.w3.org/2000/01/rdf-schema#isDefinedBy": {
        "@id": "http://ontology.projectchronos.eu/astronomy"
      },
      "http://www.w3.org/2000/01/rdf-schema#label": "PlanetaryScience",
      "http://www.w3.org/2000/01/rdf-schema#subClassOf": "http://ontology.projectchronos.eu/sensors/FieldOfResearch",
      "http://www.w3.org/2002/07/owl#sameAs": "http://dbpedia.org/resource/Planetary_science"
    },
    {
      "@id": "http://ontology.projectchronos.eu/astronomy/Planetary_system",
      "@type": "http://www.w3.org/2002/07/owl#Class",
      "http://www.w3.org/2000/01/rdf-schema#isDefinedBy": {
        "@id": "http://ontology.projectchronos.eu/astronomy"
      },
      "http://www.w3.org/2000/01/rdf-schema#label": "Planetary_system",
      "http://www.w3.org/2000/01/rdf-schema#subClassOf": "http://ontology.projectchronos.eu/astronomy/AstronomicalObject",
      "http://www.w3.org/2002/07/owl#sameAs": "http://dbpedia.org/resource/Planetary_system"
    },
    {
      "@id": "http://ontology.projectchronos.eu/astronomy/RockyPlanetaryBody",
      "@type": "http://www.w3.org/2002/07/owl#Class",
      "http://www.w3.org/2000/01/rdf-schema#comment": "a document representing a rocky body",
      "http://www.w3.org/2000/01/rdf-schema#isDefinedBy": {
        "@id": "http://ontology.projectchronos.eu/astronomy"
      },
      "http://www.w3.org/2000/01/rdf-schema#label": "RockyPlanetaryBody",
      "http://www.w3.org/2002/07/owl#sameAs": "http://umbel.org/umbel/rc/RockyPlanetaryBody"
    },
    {
      "@id": "http://ontology.projectchronos.eu/astronomy/SolidPlanetaryBody",
      "@type": "http://www.w3.org/2002/07/owl#Class",
      "http://www.w3.org/2000/01/rdf-schema#comment": "planet  composed primarily of solid substances",
      "http://www.w3.org/2000/01/rdf-schema#isDefinedBy": {
        "@id": "http://ontology.projectchronos.eu/astronomy"
      },
      "http://www.w3.org/2000/01/rdf-schema#label": "SolidPlanetaryBody",
      "http://www.w3.org/2002/07/owl#sameAs": "http://umbel.org/umbel/rc/SolidPlanetaryBody"
    },
    {
      "@id": "http://ontology.projectchronos.eu/astronomy/Star",
      "@type": "http://www.w3.org/2002/07/owl#Class",
      "http://www.w3.org/2000/01/rdf-schema#comment": "a star",
      "http://www.w3.org/2000/01/rdf-schema#isDefinedBy": {
        "@id": "http://ontology.projectchronos.eu/astronomy"
      },
      "http://www.w3.org/2000/01/rdf-schema#label": "Star",
      "http://www.w3.org/2000/01/rdf-schema#subClassOf": "http://ontology.projectchronos.eu/astronomy/AstronomicalObject",
      "http://www.w3.org/2002/07/owl#sameAs": "http://umbel.org/umbel/rc/Star"
    },
    {
      "@id": "http://ontology.projectchronos.eu/astronomy/SubplanetaryStellarOrbiter",
      "@type": "http://www.w3.org/2002/07/owl#Class",
      "http://www.w3.org/2000/01/rdf-schema#comment": "a smaller body orbiting around stars or planets, a document representing smaller body orbiting around stars or planets",
      "http://www.w3.org/2000/01/rdf-schema#isDefinedBy": {
        "@id": "http://ontology.projectchronos.eu/astronomy"
      },
      "http://www.w3.org/2000/01/rdf-schema#label": "SubplanetaryStellarOrbiter",
      "http://www.w3.org/2002/07/owl#sameAs": "http://umbel.org/umbel/rc/SubplanetaryStellarOrbiter"
    },
    {
      "@id": "http://ontology.projectchronos.eu/astronomy/TerrestrialPlanet",
      "@type": "http://www.w3.org/2002/07/owl#Class",
      "http://www.w3.org/2000/01/rdf-schema#comment": "a document representing a solid/rocky planet",
      "http://www.w3.org/2000/01/rdf-schema#isDefinedBy": {
        "@id": "http://ontology.projectchronos.eu/astronomy"
      },
      "http://www.w3.org/2000/01/rdf-schema#label": "TerrestrialPlanet",
      "http://www.w3.org/2002/07/owl#sameAs": "http://umbel.org/umbel/rc/TerrestrialPlanet"
    },
    {
      "@id": "http://ontology.projectchronos.eu/astronomy/orbiting",
      "@type": "http://www.w3.org/2002/07/owl#ObjectProperty",
      "http://www.w3.org/1999/02/22-rdf-syntax-ns#domain": "http://ontology.projectchronos.eu/astronomy/AstronomicalObject",
      "http://www.w3.org/1999/02/22-rdf-syntax-ns#range": "http://ontology.projectchronos.eu/astronomy/AstronomicalObject",
      "http://www.w3.org/2000/01/rdf-schema#comment": "this property describe the generic astronomical object-object gravitational interaction",
      "http://www.w3.org/2000/01/rdf-schema#isDefinedBy": {
        "@id": "http://ontology.projectchronos.eu/astronomy"
      },
      "http://www.w3.org/2000/01/rdf-schema#label": "orbiting"
    },
    {
      "@id": "http://ontology.projectchronos.eu/astronomy/orbitsPlanet",
      "@type": "http://www.w3.org/2002/07/owl#ObjectProperty",
      "http://www.w3.org/1999/02/22-rdf-syntax-ns#domain": "http://ontology.projectchronos.eu/astronomy/Natural_satellite",
      "http://www.w3.org/1999/02/22-rdf-syntax-ns#range": [
        "http://ontology.projectchronos.eu/astronomy/PlanetaryBody",
        "http://ontology.projectchronos.eu/astronomy/DwarfPlanet"
      ],
      "http://www.w3.org/2000/01/rdf-schema#comment": "this property describe the Moon-Planet gravitational interaction",
      "http://www.w3.org/2000/01/rdf-schema#isDefinedBy": {
        "@id": "http://ontology.projectchronos.eu/astronomy"
      },
      "http://www.w3.org/2000/01/rdf-schema#label": "orbitsPlanet"
    },
    {
      "@id": "http://ontology.projectchronos.eu/sensors/PlanetaryAstronomy",
      "@type": "http://www.w3.org/2002/07/owl#Class",
      "http://www.w3.org/2000/01/rdf-schema#isDefinedBy": {
        "@id": "http://ontology.projectchronos.eu/astronomy"
      },
      "http://www.w3.org/2000/01/rdf-schema#label": "PlanetaryAstronomy",
      "http://www.w3.org/2000/01/rdf-schema#subClassOf": "http://ontology.projectchronos.eu/sensors/PlanetaryScience"
    },
    {
      "@id": "http://ontology.projectchronos.eu/sensors/PlanetaryGeology",
      "@type": "http://www.w3.org/2002/07/owl#Class",
      "http://www.w3.org/2000/01/rdf-schema#isDefinedBy": {
        "@id": "http://ontology.projectchronos.eu/astronomy"
      },
      "http://www.w3.org/2000/01/rdf-schema#label": "PlanetaryGeology",
      "http://www.w3.org/2000/01/rdf-schema#subClassOf": "http://ontology.projectchronos.eu/sensors/PlanetaryScience"
    },
    {
      "@id": "http://ontology.projectchronos.eu/sensors/SolarAstronomy",
      "@type": "http://www.w3.org/2002/07/owl#Class",
      "http://www.w3.org/2000/01/rdf-schema#isDefinedBy": {
        "@id": "http://ontology.projectchronos.eu/astronomy"
      },
      "http://www.w3.org/2000/01/rdf-schema#label": "SolarAstronomy",
      "http://www.w3.org/2000/01/rdf-schema#subClassOf": "http://ontology.projectchronos.eu/sensors/FieldOfResearch"
    },
    {
      "@id": "http://ontology.projectchronos.eu/sensors/StellarAstronomy",
      "@type": "http://www.w3.org/2002/07/owl#Class",
      "http://www.w3.org/2000/01/rdf-schema#isDefinedBy": {
        "@id": "http://ontology.projectchronos.eu/astronomy"
      },
      "http://www.w3.org/2000/01/rdf-schema#label": "StellarAstronomy",
      "http://www.w3.org/2000/01/rdf-schema#subClassOf": "http://ontology.projectchronos.eu/sensors/FieldOfResearch"
    }
  ]
}
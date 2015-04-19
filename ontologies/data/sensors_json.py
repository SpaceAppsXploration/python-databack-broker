SENSORS_JSON = {
    "rdfs:label": "An ontology of sensors, to describe how they work",
    "rdfs:comment": "a set of concepts to be used to describe sensors",
    "@context": {
        "owl": "http://www.w3.org/2002/07/owl#",
        "@base": "http://ontology.projectchronos.eu/sensors/ontology",
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "sensor": "http://ontology.projectchronos.eu/sensors/",
        "skos": "http://www.w3.org/2004/02/skos/core#",
        "defines": {
            "@reverse": "rdfs:isDefinedBy"
        }
    },
    "@id": "",
    "@type": "http://www.w3.org/2002/07/owl#Ontology",
    "defines": [
        {
            "owl:sameAs": "http://umbel.org/umbel/rc/Sensor",
            "rdfs:label": "Sensor",
            "rdfs:comment": "Sensor is a device that performs data-gathering. It is usually deployed with a supporting electronic device to form a detector (Data-gathering device + Data-handling device = Detector). 1) [Sensor detects some PhysicalEntity] : Sensors are described as objects detecting some physical entity: elementary particles, light, atoms, cosmic dust, etc.  2) [Sensor measures some PhysicalQuantity] : Detection of any physical entity entails that some physical quantity of the detected particle is measured: mass, charge, spin, velocity,... 3) [Sensor hasWorkingPrinciple some DetectorWorkingPrinciple] : Detection is possible due to physical principles exploited ad hoc. For example, ionisation of charged particles within a solid state detector, used as a reversely biased diode, or electron emission due to the photoelectric effect. 4) [Sensor hasOutput some PhysicalQuantity] : Sensors produce as output some physical quantity, most usually time-varying voltages, which are then read by the the readout electronics that supports the Sensor.",
            "@id": "http://ontology.projectchronos.eu/sensors/Sensor",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": [
                {
                    "owl:someValuesFrom": "http://ontology.projectchronos.eu/sensors/PhysicalQuantity",
                    "@type": "http://www.w3.org/2002/07/owl#Restriction",
                    "owl:onProperty": "http://ontology.projectchronos.eu/sensors/hasOutput"
                },
                {
                    "owl:someValuesFrom": "http://ontology.projectchronos.eu/sensors/PhysicalQuantity",
                    "@type": "http://www.w3.org/2002/07/owl#Restriction",
                    "owl:onProperty": "http://ontology.projectchronos.eu/sensors/measures"
                },
                {
                    "owl:someValuesFrom": "http://ontology.projectchronos.eu/sensors/DetectorWorkingPrinciple",
                    "@type": "http://www.w3.org/2002/07/owl#Restriction",
                    "owl:onProperty": "http://ontology.projectchronos.eu/sensors/hasWorkingPrinciple"
                },
                {
                    "owl:someValuesFrom": "http://ontology.projectchronos.eu/sensors/PhysicalEntity",
                    "@type": "http://www.w3.org/2002/07/owl#Restriction",
                    "owl:onProperty": "http://ontology.projectchronos.eu/sensors/detects"
                }
            ]
        },
        {
            "rdf:range": "http://ontology.projectchronos.eu/sensors/PhysicalEntity",
            "rdfs:label": "detects",
            "rdfs:comment": "A relation between Detector and PhysicalEntity. Detectors detect physical entities like particles, plasma, molecules, etc. For ex, spectrometers detect light. Magnetometers detect magnetic fields, which are part of the EM-field",
            "skos:altLabel": "to detect",
            "@id": "http://ontology.projectchronos.eu/sensors/detects",
            "@type": [
                "http://www.w3.org/2002/07/owl#AsymmetricProperty",
                "http://www.w3.org/2002/07/owl#IrreflexiveProperty",
                "http://www.w3.org/2002/07/owl#ObjectProperty"
            ]
        },
        {
            "rdfs:label": "emits",
            "rdfs:comment": "A relation between a Detector and a PhysicalEntity. The relation defines an \"active sensor\": if a sensor emits any particles or waves, which are backscattered and re-absorbed, then it is an \"active sensor\". The term \"emits\" implies therefore that the emitted physical entity is also reabsorbed by the same instrument. N.B. Active sensors should belong only to the family of instruments measuring properties of the electromagnetic spectrum. References for this assumption are: 1. http://www.nasa.gov/directorates/heo/scan/communications/outreach/funfacts/txt_passive_active.html#.VKA0MhAT1I; 2. http://www.seos-project.eu/modules/remotesensing/remotesensing-c02-p02.html",
            "rdfs:range": "http://ontology.projectchronos.eu/sensors/PhysicalEntity",
            "@id": "http://ontology.projectchronos.eu/sensors/emits",
            "skos:altLabel": "to emit",
            "rdfs:domain": "http://ontology.projectchronos.eu/sensors/Sensor",
            "@type": [
                "http://www.w3.org/2002/07/owl#AsymmetricProperty",
                "http://www.w3.org/2002/07/owl#IrreflexiveProperty",
                "http://www.w3.org/2002/07/owl#ObjectProperty"
            ]
        },
        {
            "rdfs:label": "hasFieldOfResearch",
            "rdfs:comment": "A relation between a Detector and FieldOfResearch. A detector is used for some research purpose, i.e. hasApplication in some FieldOfResearch. Examples of fields of research are: Determination of the elemental characteristics of a planet's surface; Dark Energy; Climate Change monitoring, etc...",
            "rdfs:range": "http://ontology.projectchronos.eu/sensors/FieldOfResearch",
            "@id": "http://ontology.projectchronos.eu/sensors/hasFieldOfResearch",
            "rdfs:domain": "http://ontology.projectchronos.eu/sensors/Sensor",
            "@type": "http://www.w3.org/2002/07/owl#ObjectProperty",
            "owl:inverseOf": "http://ontology.projectchronos.eu/sensors/isResearchedBy"
        },
        {
            "rdfs:range": "http://ontology.projectchronos.eu/sensors/PhysicalQuantity",
            "rdfs:label": "hasOutput",
            "rdfs:comment": "A relation between Detector and a Physical Quantity. Detectors give outputs which are then processed by the due electronics. Usual outputs are Physical Quantities such as varying voltages or current flows.",
            "@id": "http://ontology.projectchronos.eu/sensors/hasOutput",
            "@type": [
                "http://www.w3.org/2002/07/owl#AsymmetricProperty",
                "http://www.w3.org/2002/07/owl#IrreflexiveProperty",
                "http://www.w3.org/2002/07/owl#ObjectProperty"
            ]
        },
        {
            "rdfs:range": "http://ontology.projectchronos.eu/sensors/DetectorWorkingPrinciple",
            "rdfs:label": "hasWorkingPrinciple",
            "@id": "http://ontology.projectchronos.eu/sensors/hasWorkingPrinciple",
            "@type": [
                "http://www.w3.org/2002/07/owl#AsymmetricProperty",
                "http://www.w3.org/2002/07/owl#IrreflexiveProperty",
                "http://www.w3.org/2002/07/owl#ObjectProperty"
            ]
        },
        {
            "rdfs:label": "isEmittedBy",
            "rdfs:comment": "A relation between a PhysicalEntity and a Detector. It is the inverse of the emits property. In case the detector is an active sensor, it \"fires\" something out, usually light, which is backscattered and absorbed. This \"something\", say, light, isEmittedBy the firing Detector",
            "rdfs:range": "http://ontology.projectchronos.eu/sensors/Sensor",
            "@id": "http://ontology.projectchronos.eu/sensors/isEmittedBy",
            "rdfs:domain": "http://ontology.projectchronos.eu/sensors/PhysicalEntity",
            "@type": [
                "http://www.w3.org/2002/07/owl#AsymmetricProperty",
                "http://www.w3.org/2002/07/owl#IrreflexiveProperty",
                "http://www.w3.org/2002/07/owl#ObjectProperty"
            ],
            "owl:inverseOf": "http://ontology.projectchronos.eu/sensors/emits"
        },
        {
            "rdfs:label": "isResearchedBy",
            "rdfs:comment": "A relation between FieldOfResearch and Detector. For every field of research given detectors are used. For Example, to look for pollutants in the Atmosphere (Earth Observation) spectrometers are used. To investigate the surface of celestial bodies ( Solar System Studies) spectrometers are used, but also dust detectors, ecc... THIS PROPRTY IS UNDER EVOLUTION.",
            "rdfs:range": "http://ontology.projectchronos.eu/sensors/Sensor",
            "@id": "http://ontology.projectchronos.eu/sensors/isResearchedBy",
            "rdfs:domain": "http://ontology.projectchronos.eu/sensors/FieldOfResearch",
            "@type": "http://www.w3.org/2002/07/owl#ObjectProperty"
        },
        {
            "rdfs:label": "isTraversedBy",
            "rdfs:subPropertyOf": "http://ontology.projectchronos.eu/sensors/detects",
            "rdfs:range": "http://ontology.projectchronos.eu/sensors/PhysicalEntity",
            "@id": "http://ontology.projectchronos.eu/sensors/isTraversedBy",
            "rdfs:domain": "http://ontology.projectchronos.eu/sensors/Sensor",
            "@type": [
                "http://www.w3.org/2002/07/owl#AsymmetricProperty",
                "http://www.w3.org/2002/07/owl#IrreflexiveProperty",
                "http://www.w3.org/2002/07/owl#ObjectProperty"
            ]
        },
        {
            "rdfs:label": "measures",
            "rdfs:comment": "A relation between the Detector and the PhysicalQuantity it measures. Examples of physical quantities can be: polarization, mass, electric charge, etc...",
            "rdfs:range": "http://ontology.projectchronos.eu/sensors/PhysicalQuantity",
            "skos:altLabel": "to measure",
            "@id": "http://ontology.projectchronos.eu/sensors/measures",
            "@type": "http://www.w3.org/2002/07/owl#ObjectProperty"
        },
        {
            "owl:sameAs": "http://escience.rpi.edu/ontology/vsto/2/0/vsto.owl#CCD",
            "rdfs:label": "CCD",
            "skos:altLabel": "Charge-coupled device",
            "@id": "http://ontology.projectchronos.eu/sensors/CCD",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://escience.rpi.edu/ontology/vsto/2/0/vsto.owl#ImagingDetector"
        },
        {
            "owl:sameAs": "http://escience.rpi.edu/ontology/vsto/2/0/vsto.owl#FabryPerot",
            "rdfs:label": "FabryPerot",
            "skos:altLabel": "Fabry–Pérot interferometer",
            "@id": "http://ontology.projectchronos.eu/sensors/FabryPerot",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://escience.rpi.edu/ontology/vsto/2/0/vsto.owl#Interferometer"
        },
        {
            "owl:sameAs": "http://escience.rpi.edu/ontology/vsto/2/0/vsto.owl#Film",
            "rdfs:label": "Film",
            "skos:altLabel": "Photographic film",
            "@id": "http://ontology.projectchronos.eu/sensors/Film",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://escience.rpi.edu/ontology/vsto/2/0/vsto.owl#ImagingDetector"
        },
        {
            "owl:sameAs": "http://escience.rpi.edu/ontology/vsto/2/0/vsto.owl#ImagingDetector",
            "rdfs:label": "ImagingDetector",
            "rdfs:comment": "Taken from the ontology : http://escience.rpi.edu/ontology/vsto/2/0/vsto_all.owl",
            "@id": "http://ontology.projectchronos.eu/sensors/ImagingDetector",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/EMFieldInstrument"
        },
        {
            "owl:sameAs": "http://escience.rpi.edu/ontology/vsto/2/0/vsto.owl#Interferometer",
            "rdfs:label": "Interferometer",
            "@id": "http://ontology.projectchronos.eu/sensors/Interferometer",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/#OpticalInstrument"
        },
        {
            "owl:sameAs": "http://escience.rpi.edu/ontology/vsto/2/0/vsto.owl#MichelsonInterferometer",
            "rdfs:label": "MichelsonInterferometer",
            "skos:altLabel": "Michelson interferometer",
            "@id": "http://ontology.projectchronos.eu/sensors/MichelsonInterferometer",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://escience.rpi.edu/ontology/vsto/2/0/vsto.owl#Interferometer"
        },
        {
            "owl:sameAs": "http://escience.rpi.edu/ontology/vsto/2/0/vsto.owl#MultiChannelPhotometer",
            "rdfs:label": "MultiChannelPhotometer",
            "skos:altLabel": "Multi-Channel Photometer",
            "@id": "http://ontology.projectchronos.eu/sensors/MultiChannelPhotometer",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/Photometer"
        },
        {
            "owl:sameAs": "http://escience.rpi.edu/ontology/vsto/2/0/vsto.owl#Radar",
            "rdfs:label": "Radar",
            "@id": "http://ontology.projectchronos.eu/sensors/Radar",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": [
                "http://ontology.projectchronos.eu/sensors/EMFieldInstrument",
                {
                    "owl:someValuesFrom": "http://ontology.projectchronos.eu/sensors/EMSpectrum",
                    "@type": "http://www.w3.org/2002/07/owl#Restriction",
                    "owl:onProperty": "http://ontology.projectchronos.eu/sensors/emits"
                }
            ]
        },
        {
            "owl:sameAs": "http://escience.rpi.edu/ontology/vsto/2/0/vsto.owl#SingleChannelPhotometer",
            "rdfs:label": "SingleChannelPhotometer",
            "skos:altLabel": "Single-Channel Photometer",
            "@id": "http://ontology.projectchronos.eu/sensors/SingleChannelPhotometer",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/Photometer"
        },
        {
            "owl:sameAs": "http://escience.rpi.edu/ontology/vsto/2/0/vsto.owl#SpectroPhotometer",
            "rdfs:label": "SpectroPhotometer",
            "@id": "http://ontology.projectchronos.eu/sensors/SpectroPhotometer",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/Photometer"
        },
        {
            "owl:sameAs": "http://escience.rpi.edu/ontology/vsto/2/0/vsto.owl#Telescope",
            "rdfs:label": "Telescope",
            "@id": "http://ontology.projectchronos.eu/sensors/Telescope",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/OpticalInstrument"
        },
        {
            "rdfs:label": "Microscope",
            "@id": "http://ontology.projectchronos.eu/sensors/Microscope",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/OpticalInstrument"
        },
        {
            "owl:sameAs": "http://www.astro.umd.edu/~eshaya/astro-onto/owl/chemistry.owl#Ionization",
            "rdfs:label": "Ionization",
            "@id": "http://ontology.projectchronos.eu/sensors/Ionization",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/DetectorWorkingPrinciple"
        },
        {
            "owl:sameAs": "http://www.astro.umd.edu/~eshaya/astro-onto/owl/physics.owl#Diffraction",
            "rdfs:label": "Diffraction",
            "@id": "http://ontology.projectchronos.eu/sensors/Diffraction",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/DetectorWorkingPrinciple"
        },
        {
            "rdfs:label": "GeometricalOptics",
            "rdfs:comment": "Geometrical optics, or ray optics, describes light propagation in terms of rays. The ray in geometric optics is an abstraction, or instrument, useful in approximating the paths along which light propagates in certain classes of circumstances. The simplifying assumptions of geometrical optics include that light rays: \npropagate in rectilinear paths as they travel in a homogeneous medium \n bend, and in particular circumstances may split in two, at the interface between two dissimilar media \nfollow curved paths in a medium in which the refractive index changes \nmay be absorbed or reflected. \nGeometrical optics does not account for certain optical effects such as diffraction and interference. This simplification is useful in practice; it is an excellent approximation when the wavelength is small compared to the size of structures with which the light interacts. The techniques are particularly useful in describing geometrical aspects of imaging, including optical aberrations. [Source: http://en.wikipedia.org/wiki/Geometrical_optics]",
            "@id": "http://ontology.projectchronos.eu/sensors/GeometricalOptics",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/DetectorWorkingPrinciple"
        },
        {
            "rdfs:label": "AntennaTheory",
            "rdfs:comment": "An antenna (or aerial) is an electrical device which converts electric power into radio waves, and vice versa. It is usually used with a radio transmitter or radio receiver. In transmission, a radio transmitter supplies an electric current oscillating at radio frequency (i.e. a high frequency alternating current (AC)) to the antenna's terminals, and the antenna radiates the energy from the current as electromagnetic waves (radio waves). In reception, an antenna intercepts some of the power of an electromagnetic wave in order to produce a tiny voltage at its terminals, that is applied to a receiver to be amplified. [Source: http://en.wikipedia.org/wiki/Antenna_%28radio%29]",
            "@id": "http://ontology.projectchronos.eu/sensors/AntennaTheory",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/DetectorWorkingPrinciple"
        },
        {
            "rdfs:label": "Ferromagnetism",
            "@id": "http://ontology.projectchronos.eu/sensors/Ferromagnetism",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/DetectorWorkingPrinciple"
        },
        {
            "rdfs:label": "IonOptics",
            "@id": "http://ontology.projectchronos.eu/sensors/IonOptics",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/DetectorWorkingPrinciple"
        },
        {
            "rdfs:label": "Secondary Emission",
            "@id": "http://ontology.projectchronos.eu/sensors/SecondaryEmission",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/DetectorWorkingPrinciple"
        },
        {
            "rdfs:label": "Electron Emission",
            "@id": "http://ontology.projectchronos.eu/sensors/ElectronEmission",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/SecondaryEmission"
        },
        {
            "rdfs:label": "Photoelectron Emission",
            "@id": "http://ontology.projectchronos.eu/sensors/PhotoElectronEmission",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/ElectronEmission"
        },
        {
            "rdfs:label": "DustDetector",
            "skos:altLabel": "Dust Detector",
            "@id": "http://ontology.projectchronos.eu/sensors/DustDetector",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/DirectSensingInstrument"
        },
        {
            "owl:sameAS": "http://dbpedia.org/page/Particle_detector",
            "rdfs:label": "Particle Detector",
            "@id": "http://ontology.projectchronos.eu/sensors/ParticleDetector",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/Sensor"
        },
        {
            "rdfs:label": "Particle Detector",
            "@id": "http://ontology.projectchronos.eu/sensors/SolidStateDetector",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/ParticleDetector"
        },
        {
            "rdfs:label": "Microchannel Plate",
            "@id": "http://ontology.projectchronos.eu/sensors/MicrochannelPlate",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/ParticleDetector"
        },
        {
            "rdfs:label": "EMFieldInstrument",
            "rdfs:comment": "Electromagnetic field instruments measure some physical property of incoming photons. (My definition)",
            "skos:altLabel": "Electromagnetic field instruments",
            "owl:equivalentClass": {
                "@type": "http://www.w3.org/2002/07/owl#Class",
                "owl:intersectionOf": [
                    "http://ontology.projectchronos.eu/sensors/Sensor",
                    {
                        "owl:someValuesFrom": "http://ontology.projectchronos.eu/sensors/EMSpectrum",
                        "@type": "http://www.w3.org/2002/07/owl#Restriction",
                        "owl:onProperty": "http://ontology.projectchronos.eu/sensors/detects"
                    }
                ]
            },
            "@id": "http://ontology.projectchronos.eu/sensors/EMFieldInstrument",
            "rdfs:subClassOf": {
                "owl:someValuesFrom": "http://ontology.projectchronos.eu/sensors/PhysicalEntity",
                "@type": "http://www.w3.org/2002/07/owl#Restriction",
                "owl:onProperty": "http://ontology.projectchronos.eu/sensors/isTraversedBy"
            },
            "@type": "http://www.w3.org/2002/07/owl#Class"
        },
        {
            "rdfs:label": "MassSpectrometer",
            "skos:altLabel": "Mass Spectrometer",
            "@id": "http://ontology.projectchronos.eu/sensors/MassSpectrometer",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/Sensor"
        },
        {
            "rdfs:label": "Time-of-Flight Mass Spectrometer",
            "skos:altLabel": "Time-of-Flight Mass Spectrometer",
            "@id": "http://ontology.projectchronos.eu/sensors/TimeOfFlightMassSpectrometer",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/MassSpectrometer"
        },
        {
            "rdfs:label": "OpticalInstrument",
            "skos:altLabel": "Optical Instrument",
            "@id": "http://ontology.projectchronos.eu/sensors/OpticalInstrument",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": [
                "http://ontology.projectchronos.eu/sensors/EMFieldInstrument",
                {
                    "@type": "http://www.w3.org/2002/07/owl#Class",
                    "owl:intersectionOf": [
                        "http://ontology.projectchronos.eu/sensors/EMFieldInstrument",
                        {
                            "@type": "http://www.w3.org/2002/07/owl#Class",
                            "owl:complementOf": "http://ontology.projectchronos.eu/sensors/ActiveInstrument"
                        }
                    ]
                }
            ]
        },
        {
            "rdfs:label": "Photometer",
            "@id": "http://ontology.projectchronos.eu/sensors/Photometer",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/OpticalInstrument"
        },
        {
            "rdfs:label": "Polarimeter",
            "@id": "http://ontology.projectchronos.eu/sensors/Polarimeter",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/OpticalInstrument"
        },
        {
            "rdfs:label": "Active Instrument",
            "rdfs:comment": "An active instrument provides its own means of sensing the remote object. Typical of this would be a radar system.  Radar generates pulses of radio waves that it sends to a surface, and then receives their reflections back from the surface. Source: \"Basics of Space flight, Section II, Chapter 12. Typical Science Instruments\", Jet Propulsion Laboratory. http://www2.jpl.nasa.gov/basics/bsf12-1.php",
            "owl:disjointWith": "http://ontology.projectchronos.eu/sensors/PassiveInstrument",
            "owl:equivalentClass": {
                "@type": "http://www.w3.org/2002/07/owl#Class",
                "owl:intersectionOf": [
                    "http://ontology.projectchronos.eu/sensors/Sensor",
                    {
                        "owl:someValuesFrom": "http://ontology.projectchronos.eu/sensors/PhysicalEntity",
                        "@type": "http://www.w3.org/2002/07/owl#Restriction",
                        "owl:onProperty": "http://ontology.projectchronos.eu/sensors/emits"
                    }
                ]
            },
            "@id": "http://ontology.projectchronos.eu/sensors/ActiveInstrument",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/Sensor",
            "@type": "http://www.w3.org/2002/07/owl#Class"
        },
        {
            "rdfs:label": "AmountOfSubstance",
            "@id": "http://ontology.projectchronos.eu/sensors/AmountOfSubstance",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/PhysicalQuantity"
        },
        {
            "rdfs:label": "Intensity",
            "@id": "http://ontology.projectchronos.eu/sensors/Intensity",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/PhysicalQuantity"
        },
        {
            "rdfs:label": "Atom",
            "@id": "http://ontology.projectchronos.eu/sensors/Atom",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/PhysicalEntity"
        },
        {
            "rdfs:label": "Blue",
            "@id": "http://ontology.projectchronos.eu/sensors/Blue",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/Optical"
        },
        {
            "rdfs:label": "CMOS",
            "@id": "http://ontology.projectchronos.eu/sensors/CMOS",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": " http://escience.rpi.edu/ontology/vsto/2/0/vsto.owl#ImagingDetector"
        },
        {
            "rdfs:label": "CosmicRays",
            "@id": "http://ontology.projectchronos.eu/sensors/CosmicRays",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/Particle"
        },
        {
            "rdfs:label": "DeepSpace",
            "@id": "http://ontology.projectchronos.eu/sensors/DeepSpace",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/FieldOfResearch"
        },
        {
            "rdfs:label": "DetectorWorkingPrinciple",
            "rdfs:comment": "To be expanded",
            "@id": "http://ontology.projectchronos.eu/sensors/DetectorWorkingPrinciple",
            "@type": "http://www.w3.org/2002/07/owl#Class"
        },
        {
            "rdfs:label": "DirectSensingInstrument",
            "rdfs:comment": "Direct-sensing instruments, also called contact science instruments, register characteristics of phenomena in their vicinity. (Source: \"Basic of Space flight, Section II, Chapter 12. Typical Science Instruments\", Jet Propulsion Laboratory, www.jpl.nasa.gov/basics/bsf12-1.php )",
            "owl:disjointWith": "http://ontology.projectchronos.eu/sensors/RemoteSensingInstrument",
            "@id": "http://ontology.projectchronos.eu/sensors/DirectSensingInstrument",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "owl:equivalentClass": {
                "@type": "http://www.w3.org/2002/07/owl#Class",
                "owl:intersectionOf": [
                    "http://ontology.projectchronos.eu/sensors/Sensor",
                    {
                        "@type": "http://www.w3.org/2002/07/owl#Class",
                        "owl:complementOf": "http://ontology.projectchronos.eu/sensors/RemoteSensingInstrument"
                    }
                ]
            }
        },
        {
            "rdfs:label": "Dust",
            "@id": "http://ontology.projectchronos.eu/sensors/Dust",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/PhysicalEntity"
        },
        {
            "owl:sameAs": "http://dbpedia.org/resource/Electromagnetic_spectrum",
            "rdfs:label": "EMSpectrum",
            "rdfs:comment": "I copied and pasted this class and its subclasses from some image file (.png) of an ontology which I cannot find again. It is important to find it again to give credits.",
            "@id": "http://ontology.projectchronos.eu/sensors/EMSpectrum",
            "@type": "http://www.w3.org/2002/07/owl#Class"
        },
        {
            "owl:sameAs": "http://dbpedia.org/resource/Electric_charge",
            "rdfs:label": "ElectricCharge",
            "@id": "http://ontology.projectchronos.eu/sensors/ElectricCharge",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/PhysicalQuantity"
        },
        {
            "rdfs:label": "ElectricCurrent",
            "@id": "http://ontology.projectchronos.eu/sensors/ElectricCurrent",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/PhysicalQuantity"
        },
        {
            "rdfs:label": "ElectricFieldStrength",
            "@id": "http://ontology.projectchronos.eu/sensors/ElectricFieldStrength",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/PhysicalQuantity"
        },
        {
            "owl:sameAs": "http://dbpedia.org/resource/Electric_potential",
            "rdfs:label": "ElectricPotential",
            "@id": "http://ontology.projectchronos.eu/sensors/ElectricPotential",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/PhysicalQuantity"
        },
        {
            "owl:sameAs": "http://dbpedia.org/resource/Electrical_resistance_and_conductance",
            "rdfs:label": "ElectricalResistance",
            "@id": "http://ontology.projectchronos.eu/sensors/ElectricalResistance",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/PhysicalQuantity"
        },
        {
            "owl:sameAs": "http://dbpedia.org/resource/Energy",
            "rdfs:label": "Energy",
            "@id": "http://ontology.projectchronos.eu/sensors/Energy",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/PhysicalQuantity"
        },
        {
            "owl:sameAs": "http://dbpedia.org/resource/Energy_density",
            "rdfs:label": "EnergyDensity",
            "@id": "http://ontology.projectchronos.eu/sensors/EnergyDensity",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/PhysicalQuantity"
        },
        {
            "owl:sameAs": "http://dbpedia.org/page/Voltage",
            "rdfs:label": "Voltage",
            "@id": "http://ontology.projectchronos.eu/sensors/Voltage",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/PhysicalQuantity"
        },
        {
            "owl:sameAs": "http://dbpedia.org/page/Radiant_flux",
            "rdfs:label": "Radiant Flux",
            "@id": "http://ontology.projectchronos.eu/sensors/RadiantFlux",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/PhysicalQuantity"
        },
        {
            "rdfs:label": "Radiant Flux",
            "@id": "http://ontology.projectchronos.eu/sensors/ParticleFlux",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/PhysicalQuantity"
        },
        {
            "rdfs:label": "ExtremeUltraViolet",
            "@id": "http://ontology.projectchronos.eu/sensors/ExtremeUltraViolet",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/EMSpectrum"
        },
        {
            "rdfs:label": "FarInfrared",
            "@id": "http://ontology.projectchronos.eu/sensors/FarInfrared",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/Infrared"
        },
        {
            "rdfs:label": "FieldOfResearch",
            "rdfs:comment": "This is just a first sketch. To be expanded.",
            "@id": "http://ontology.projectchronos.eu/sensors/FieldOfResearch",
            "@type": "http://www.w3.org/2002/07/owl#Class"
        },
        {
            "owl:sameAs": "http://dbpedia.org/resource/Force",
            "rdfs:label": "Force",
            "@id": "http://ontology.projectchronos.eu/sensors/Force",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/PhysicalQuantity"
        },
        {
            "owl:sameAs": "http://dbpedia.org/resource/Frequency",
            "rdfs:label": "Frequency",
            "@id": "http://ontology.projectchronos.eu/sensors/Frequency",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/PhysicalQuantity"
        },
        {
            "owl:sameAs": "http://dbpedia.org/resource/Gamma_ray",
            "rdfs:label": "GammaRays",
            "@id": "http://ontology.projectchronos.eu/sensors/GammaRays",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/EMSpectrum"
        },
        {
            "owl:sameAs": "http://dbpedia.org/resource/Heat",
            "rdfs:label": "Heat",
            "@id": "http://ontology.projectchronos.eu/sensors/Heat",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/PhysicalQuantity"
        },
        {
            "rdfs:label": "Impulse",
            "@id": "http://ontology.projectchronos.eu/sensors/Impulse",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/PhysicalQuantity"
        },
        {
            "rdfs:label": "IndexOfRefraction",
            "@id": "http://ontology.projectchronos.eu/sensors/IndexOfRefraction",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/PhysicalQuantity"
        },
        {
            "owl:sameAs": "http://dbpedia.org/resource/Infrared",
            "rdfs:label": "Infrared",
            "@id": "http://ontology.projectchronos.eu/sensors/Infrared",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/EMSpectrum"
        },
        {
            "rdfs:label": "InfraredRadiometer",
            "@id": "http://ontology.projectchronos.eu/sensors/InfraredRadiometer",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/Radiometer"
        },
        {
            "owl:sameAs": "http://dbpedia.org/resource/Length_measurement",
            "rdfs:label": "Length",
            "@id": "http://ontology.projectchronos.eu/sensors/Length",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/PhysicalQuantity"
        },
        {
            "rdfs:label": "LuminousIntensity",
            "@id": "http://ontology.projectchronos.eu/sensors/LuminousIntensity",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/PhysicalQuantity"
        },
        {
            "rdfs:label": "MagneticFieldStrength",
            "@id": "http://ontology.projectchronos.eu/sensors/MagneticFieldStrength",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/PhysicalQuantity"
        },
        {
            "owl:sameAs": "http://dbpedia.org/resource/Magnetometer",
            "rdfs:label": "Magnetometer",
            "@id": "http://ontology.projectchronos.eu/sensors/Magnetometer",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": [
                "http://ontology.projectchronos.eu/sensors/EMFieldInstrument",
                {
                    "@type": "http://www.w3.org/2002/07/owl#Class",
                    "owl:intersectionOf": [
                        "http://ontology.projectchronos.eu/sensors/EMFieldInstrument",
                        {
                            "@type": "http://www.w3.org/2002/07/owl#Class",
                            "owl:complementOf": "http://ontology.projectchronos.eu/sensors/ActiveInstrument"
                        }
                    ]
                }
            ]
        },
        {
            "owl:sameAs": [
                "http://umbel.org/umbel/rc/Mass",
                "http://dbpedia.org/resource/Mass",
                "http://schema.org/Mass"
            ],
            "rdfs:label": "Mass",
            "@id": "http://ontology.projectchronos.eu/sensors/Mass",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/PhysicalQuantity"
        },
        {
            "rdfs:label": "MeanLifeTime",
            "@id": "http://ontology.projectchronos.eu/sensors/MeanLifeTime",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/PhysicalQuantity"
        },
        {
            "owl:sameAs": "http://dbpedia.org/resource/Molecule",
            "rdfs:label": "Molecule",
            "@id": "http://ontology.projectchronos.eu/sensors/Molecule",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/PhysicalEntity"
        },
        {
            "rdfs:label": "NearInfrared",
            "@id": "http://ontology.projectchronos.eu/sensors/NearInfrared",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/Infrared"
        },
        {
            "rdfs:label": "Optical",
            "@id": "http://ontology.projectchronos.eu/sensors/Optical",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/EMSpectrum"
        },
        {
            "owl:sameAs": "http://dbpedia.org/resource/Subatomic_particle",
            "rdfs:label": "Particle",
            "@id": "http://ontology.projectchronos.eu/sensors/Particle",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/PhysicalEntity"
        },
        {
            "rdfs:label": "PassiveInstrument",
            "rdfs:comment": "Most instruments only receive and process existing light, particles, or other phenomena, and they are said to be passive. Typical of this type would be an imaging instrument viewing a planet that is illuminated by sunlight, or a magnetometer measuring existing magnetic fields. Source: \"Basics of Space flight, Section II, Chapter 12. Typical Science Instruments\", Jet Propulsion Laboratory. http://www2.jpl.nasa.gov/basics/bsf12-1.php",
            "owl:equivalentClass": {
                "@type": "http://www.w3.org/2002/07/owl#Class",
                "owl:intersectionOf": [
                    "http://ontology.projectchronos.eu/sensors/Sensor",
                    {
                        "@type": "http://www.w3.org/2002/07/owl#Class",
                        "owl:complementOf": "http://ontology.projectchronos.eu/sensors/ActiveInstrument"
                    }
                ]
            },
            "@id": "http://ontology.projectchronos.eu/sensors/PassiveInstrument",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/Sensor",
            "@type": "http://www.w3.org/2002/07/owl#Class"
        },
        {
            "rdfs:label": "PhotoElectronIonization",
            "@id": "http://ontology.projectchronos.eu/sensors/PhotoElectronIonization",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://www.astro.umd.edu/~eshaya/astro-onto/owl/chemistry.owl#Ionization"
        },
        {
            "rdfs:label": "PhysicalEntity",
            "rdfs:comment": "Physical Entities are what is sensed by a detector. They can be atoms, ions, elementary particles, light, molecules, etc...",
            "@id": "http://ontology.projectchronos.eu/sensors/PhysicalEntity",
            "@type": "http://www.w3.org/2002/07/owl#Class"
        },
        {
            "rdfs:label": "PhysicalQuantity",
            "rdfs:comment": "A physical quantity (or \"physical magnitude\") is a physical property of a phenomenon, body, or substance, that can be quantified by measurement. Source: Wikipedia, http://en.wikipedia.org/wiki/Physical_quantity",
            "@id": "http://ontology.projectchronos.eu/sensors/PhysicalQuantity",
            "@type": "http://www.w3.org/2002/07/owl#Class"
        },
        {
            "owl:sameAs": "http://dbpedia.org/resource/Plasma_(physics)",
            "rdfs:label": "Plasma",
            "@id": "http://ontology.projectchronos.eu/sensors/Plasma",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/PhysicalEntity"
        },
        {
            "owl:sameAs": "http://dbpedia.org/resource/Power_(physics)",
            "rdfs:label": "Power",
            "@id": "http://ontology.projectchronos.eu/sensors/Power",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/PhysicalQuantity"
        },
        {
            "owl:sameAs": "http://dbpedia.org/resource/Pressure",
            "rdfs:label": "Pressure",
            "@id": "http://ontology.projectchronos.eu/sensors/Pressure",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/PhysicalQuantity"
        },
        {
            "rdfs:label": "Radio",
            "@id": "http://ontology.projectchronos.eu/sensors/Radio",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/EMSpectrum"
        },
        {
            "rdfs:label": "RadioCentrimetric",
            "@id": "http://ontology.projectchronos.eu/sensors/RadioCentrimetric",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/Radio"
        },
        {
            "rdfs:label": "RadioMetric",
            "@id": "http://ontology.projectchronos.eu/sensors/RadioMetric",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/Radio"
        },
        {
            "rdfs:label": "RadioMillimetric",
            "@id": "http://ontology.projectchronos.eu/sensors/RadioMillimetric",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/Radio"
        },
        {
            "rdfs:label": "RadioSubMillimetric",
            "@id": "http://ontology.projectchronos.eu/sensors/RadioSubMillimetric",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/Radio"
        },
        {
            "owl:sameAs": "http://dbpedia.org/resource/Radiometer",
            "rdfs:label": "Radiometer",
            "@id": "http://ontology.projectchronos.eu/sensors/Radiometer",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/OpticalInstrument"
        },
        {
            "rdfs:label": "Red",
            "@id": "http://ontology.projectchronos.eu/sensors/Red",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/Optical"
        },
        {
            "owl:sameAs": "http://dbpedia.org/resource/Remote_sensing",
            "rdfs:label": "RemoteSensingInstrument",
            "rdfs:comment": "Remote-sensing instruments exist to form some kind of image or characterization of the source of the phenomena that enter the instrument. In doing so, they record characteristics of objects at a distance, sometimes forming an image by gathering, focusing and recording light. (Source: \"Basics of Space flight, Section II, Chapter 12. Typical Science Instruments\", Jet Propulsion Laboratory, www.jpl.nasa.gov/basics/bsf12-1.php)",
            "@id": "http://ontology.projectchronos.eu/sensors/RemoteSensingInstrument",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "owl:equivalentClass": {
                "@type": "http://www.w3.org/2002/07/owl#Class",
                "owl:intersectionOf": [
                    "http://ontology.projectchronos.eu/sensors/Sensor",
                    {
                        "owl:someValuesFrom": "http://ontology.projectchronos.eu/sensors/PhysicalEntity",
                        "@type": "http://www.w3.org/2002/07/owl#Restriction",
                        "owl:onProperty": "http://ontology.projectchronos.eu/sensors/isTraversedBy"
                    }
                ]
            }
        },
        {
            "owl:sameAs": "http://dbpedia.org/resource/Solar_System",
            "rdfs:label": "SolarSystem",
            "@id": "http://ontology.projectchronos.eu/sensors/SolarSystem",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/FieldOfResearch"
        },
        {
            "owl:sameAs": "http://dbpedia.org/resource/Spectrograph",
            "rdfs:label": "Spectograph",
            "@id": "http://ontology.projectchronos.eu/sensors/Spectrograph",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/SpectroscopicInstrument"
        },
        {
            "owl:sameAs": "http://dbpedia.org/resource/Spectrometer",
            "rdfs:label": "Spectrometer",
            "@id": "http://ontology.projectchronos.eu/sensors/Spectrometer",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/SpectroscopicInstrument"
        },
        {
            "rdfs:label": "SpectroscopicInstrument",
            "@id": "http://ontology.projectchronos.eu/sensors/SpectroscopicInstrument",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/OpticalInstrument"
        },
        {
            "owl:sameAs": "http://dbpedia.org/resource/Spin_(physics)",
            "rdfs:label": "Spin_(physics)",
            "@id": "http://ontology.projectchronos.eu/sensors/Spin_(physics)",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/PhysicalQuantity"
        },
        {
            "owl:sameAs": "http://dbpedia.org/resource/Temperature",
            "rdfs:label": "Temperature",
            "@id": "http://ontology.projectchronos.eu/sensors/Temperature",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/PhysicalQuantity"
        },
        {
            "owl:sameAs": "http://ontology.projectchronos.eu/dbpediadocs/Time",
            "rdfs:label": "Time",
            "@id": "http://ontology.projectchronos.eu/sensors/Time",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/PhysicalQuantity"
        },
        {
            "rdfs:label": "Time of Flight",
            "@id": "http://ontology.projectchronos.eu/sensors/TimeOfFlight",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/Time"
        },
        {
            "owl:sameAs": "http://ontology.projectchronos.eu/dbpediadocs/Ultraviolet",
            "rdfs:label": "UltraViolet",
            "@id": "http://ontology.projectchronos.eu/sensors/UltraViolet",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/EMSpectrum"
        },
        {
            "rdfs:label": "UltravioletRadiometer",
            "@id": "http://ontology.projectchronos.eu/sensors/UltravioletRadiometer",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/Radiometer"
        },
        {
            "owl:sameAs": "http://ontology.projectchronos.eu/dbpediadocs/Velocity",
            "rdfs:label": "Velocity",
            "@id": "http://ontology.projectchronos.eu/sensors/Velocity",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/PhysicalQuantity"
        },
        {
            "owl:sameAs": [
                "http://umbel.org/umbel/rc/Volume",
                "http://dbpedia.org/resource/Volume"
            ],
            "rdfs:label": "Volume",
            "@id": "http://ontology.projectchronos.eu/sensors/Volume",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/PhysicalQuantity"
        },
        {
            "owl:sameAs": "http://ontology.projectchronos.eu/dbpediadocs/Wavelength",
            "rdfs:label": "Wavelength",
            "@id": "http://ontology.projectchronos.eu/sensors/Wavelength",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/PhysicalQuantity"
        },
        {
            "owl:sameAs": "http://ontology.projectchronos.eu/dbpediadocs/X-ray",
            "rdfs:label": "X-ray",
            "@id": "http://ontology.projectchronos.eu/sensors/X-Rays",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/EMSpectrum"
        },
        {
            "owl:sameAs": "http://ontology.projectchronos.eu/dbpediadocs/Ion",
            "rdfs:label": "Ion",
            "@id": "http://ontology.projectchronos.eu/sensors/Ion",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/Atom"
        },
        {
            "owl:sameAs": "http://ontology.projectchronos.eu/dbpediadocs/Isotope",
            "rdfs:label": "Isotope",
            "@id": "http://ontology.projectchronos.eu/sensors/Isotope",
            "@type": "http://www.w3.org/2002/07/owl#Class",
            "rdfs:subClassOf": "http://ontology.projectchronos.eu/sensors/Atom"
        },
        {
            "owl:sameAs": "http://ontology.projectchronos.eu/dbpediadocs/Electron",
            "rdfs:label": "Electron",
            "@id": "http://ontology.projectchronos.eu/sensors/Electron",
            "@type": [
                "http://www.w3.org/2002/07/owl#NamedIndividual",
                "http://ontology.projectchronos.eu/sensors/Particle"
            ]
        },
        {
            "owl:sameAs": "http://ontology.projectchronos.eu/dbpediadocs/Neutrino",
            "rdfs:label": "Neutrino",
            "@id": "http://www.w3.org/2002/07/owl#Neutrino",
            "@type": [
                "http://www.w3.org/2002/07/owl#NamedIndividual",
                "http://ontology.projectchronos.eu/sensors/Particle"
            ]
        },
        {
            "owl:sameAs": "http://ontology.projectchronos.eu/dbpediadocs/Neutron",
            "rdfs:label": "Neutron",
            "@id": "http://ontology.projectchronos.eu/sensors/Neutron",
            "@type": [
                "http://www.w3.org/2002/07/owl#NamedIndividual",
                "http://ontology.projectchronos.eu/sensors/Particle"
            ]
        },
        {
            "owl:sameAs": "http://ontology.projectchronos.eu/dbpediadocs/Photon",
            "rdfs:label": "Photon",
            "@id": "http://ontology.projectchronos.eu/sensors/Photon",
            "@type": [
                "http://www.w3.org/2002/07/owl#NamedIndividual",
                "http://ontology.projectchronos.eu/sensors/Particle"
            ]
        },
        {
            "owl:sameAs": "http://ontology.projectchronos.eu/dbpediadocs/Proton",
            "rdfs:label": "Proton",
            "@id": "http://ontology.projectchronos.eu/sensors/Proton",
            "@type": [
                "http://www.w3.org/2002/07/owl#NamedIndividual",
                "http://ontology.projectchronos.eu/sensors/Particle"
            ]
        },
        {
            "skos:altLabel": "#AllDisjointsProperties",
            "@id": "",
            "@type": "http://www.w3.org/2002/07/owl#AllDisjointProperties",
            "owl:members": [
                "http://ontology.projectchronos.eu/sensors/detects",
                "http://ontology.projectchronos.eu/sensors/emits",
                "http://ontology.projectchronos.eu/sensors/hasFieldOfResearch",
                "http://ontology.projectchronos.eu/sensors/hasOutput",
                "http://ontology.projectchronos.eu/sensors/isEmittedBy",
                "http://ontology.projectchronos.eu/sensors/isResearchedBy",
                "http://ontology.projectchronos.eu/sensors/measures"
            ]
        }
    ]
}
import tkinter as tk
import random

prompts = [
    "The Eternal Night City: In a world where night has fallen permanently, a hidden metropolis thrives beneath the surface. The city is illuminated by intricate neon signage, holographic billboards, and underground train systems, offering a haven for those who prefer the cover of darkness.",
    "The Desert Oasis: A story set in a remote desert, where an underground oasis is concealed beneath the dunes. The subterranean water source sustains a flourishing, self-sustaining community of desert-dwelling nomads and explorers.",
    "Undersea Research Station: In a high-tech undersea research facility, scientists study the mysterious depths of the ocean. The story could revolve around their discoveries, the challenges they face, and the creatures they encounter.",
    "Cave of Echoes: Set within an immense underground cave system with incredible acoustics, a musician discovers that the cave's echoes possess magical properties. The tale might follow their journey to harness this newfound power for artistic expression.",
    "Journey Through Time: A time-travel adventure in which a group of explorers discovers a hidden portal within an ancient underground temple. The portal allows them to traverse various historical eras, uncovering secrets and confronting temporal challenges.",
    "Challenging Navigation: Navigating the Bioluminescent Abyss would be a visual spectacle but also challenging due to the lack of natural light. Explorers would have to rely on the bioluminescence, specialized gear, and knowledge of the ecosystem to survive and traverse this alien world.",
    "Mysteries and Discoveries: The environment is riddled with secrets, hidden chambers, and puzzles, offering opportunities for exploration and discovery. These discoveries could include ancient artifacts, hidden knowledge, or rare bioluminescent species.",
    "Sky Kingdom of Floating Islands: High above the clouds, a kingdom of floating islands conceals itself from the world below. The narrative could focus on a character's journey to visit or infiltrate this elusive world, with gravity-defying technology and structures.",
    "Volcanic Forge: Deep within the earth, an underground forge powered by volcanic activity is used to create mythical weapons. The story could revolve around the quest for a legendary, world-altering weapon forged within its fiery depths.",
    "Moonbase: Set in a future where humanity has established a lunar base, the narrative explores life on the moon, the challenges of space travel, and the relationships among the lunar inhabitants.",
    "Hidden Arctic Vault: A top-secret facility buried beneath the Arctic ice holds archives of lost knowledge and cutting-edge technology. The protagonist may be an archaeologist, scientist, or secret agent seeking to uncover the truth behind this enigmatic installation.",
    "Agricultural Wonderland: In a vast, hidden underground farm, a community thrives by cultivating exotic crops in a controlled environment. The story could delve into the lives of the farmers, the rare plants they grow, and the secrets they protect.",
    "Clockwork Labyrinth: Within an enormous, underground clockwork labyrinth, intricate gears, cogs, and clock mechanisms dominate the landscape. The story could center around characters navigating this mechanical wonderland, solving puzzles, and unlocking the labyrinth's secrets.",
    "Aerial City in the Clouds: High above the surface world, a hidden city floats amidst the clouds. The inhabitants harness the power of wind and air currents to keep the city aloft. The story might follow a character's journey to this breathtaking and mysterious floating metropolis.",
    "Crystal Gardens of Light: In an underground world, immense crystal gardens create a stunning spectacle. These crystals are not bioluminescent but refract natural sunlight in an enchanting display. The narrative could involve characters protecting or preserving this fragile ecosystem.",
    "Jungle Within a Tree: Deep within the hollowed trunk of an ancient, colossal tree, a lush and self-contained jungle thrives. The story could revolve around a group of explorers delving into the tree's depths, encountering unique wildlife, and unearthing long-forgotten secrets.",
    "Subterranean Ice Palace: Hidden beneath an icy tundra, a palace made entirely of ice and inhabited by an enigmatic ruler holds the power to control the region's climate. The narrative may follow characters navigating this palace and its challenges.",
    "Underground Library of Forgotten Words: In a subterranean library, the forgotten words of ancient languages come to life when spoken. Characters could embark on a linguistic journey to decipher these words and their lost meanings.",
    "Skyward Archipelago: In a world of floating islands, each island is a unique biome with its own culture and ecosystem. Characters may travel between these floating realms, encountering diverse societies and challenges.",
    "Deep Sea Bioluminescent City: Set in the depths of the ocean, a bioluminescent city thrives among the strange and wondrous creatures of the abyss. The story could follow an underwater explorer uncovering the city's mysteries.",
    "Crystal Maze of Illusions: Inside a maze constructed from illusion-inducing crystals, characters navigate shifting realities, optical illusions, and puzzling environments. The story might explore the nature of perception and reality.",
    "Living Lava Caves: Within a network of lava caves, the walls and formations are alive, composed of heat-resistant, silicon-based life forms. Characters could explore this fiery underworld, confronting both the dangers and the wonders it holds.",
    "The Colorful Fungi Forest: In a subterranean forest, the flora consists of vibrant, phosphorescent fungi that emit colors based on their mood and environmental conditions. The story could follow a botanist or artist studying these living, expressive fungi.",
    "Skyport of Airship Pirates: High above the clouds, a hidden skyport serves as a base for a group of airship pirates. The narrative might focus on their daring heists, rivalries with other sky crews, and the hidden treasures of the skies.",
    "Giant Ant Colony: Within a vast underground ant colony, intelligent ants have created a complex society with their own laws, politics, and technologies. The story could explore the life and adventures of a human who becomes part of this ant civilization.",
    "Biomimetic Underwater City: In the depths of the ocean, a city is constructed with biomimetic architecture, mirroring the forms and functions of marine life. The narrative could delve into the challenges of sustaining this underwater metropolis.",
    "Island of the Ancestors: A remote island is a sacred burial ground, and the spirits of the deceased return to influence the living. The story could follow a character who communicates with these spirits and unravels the island's mystical history.",
    "Amphibious Space Station: A space station hovers at the edge of Earth's atmosphere, designed to support both human and aquatic life. The narrative may explore the unique challenges faced by the inhabitants and the interactions between these two environments.",
    "Inverted Mountain Realm: In a realm where gravity is reversed, an inverted mountain towers into the sky, with its depths explored from the mountaintop. The story could involve daring adventurers scaling the peak to access the inverted world.",
    "Crystal Desert Oasis: A seemingly endless desert conceals an oasis filled with colossal, gemstone-like crystals. The narrative could revolve around those who seek to harness the power or secrets of these mysterious desert gems.",
    "Insect Metropolis: In a city built and operated by sentient insects, a protagonist from the surface world encounters this hidden civilization. The story explores the culture, technology, and interactions between insects and humans.",
    "Aqua-Art Gallery: An underwater art gallery showcases sculptures and paintings, illuminated by the ocean's natural light. The story could follow an artist or curator working in this unique aquatic space, striving to create and protect the delicate artwork.",
    "Magnetic Fields of the Crystal Plains: An expansive landscape covered in shimmering crystal formations. The crystals respond to magnetic fields, creating captivating displays of color and light as characters navigate this otherworldly terrain.",
    "Holographic Dreamscape: A virtual dreamscape where people can immerse themselves in holographic worlds created by their own thoughts and desires. The narrative might explore the consequences of living in a world of endless virtual possibilities.",
    "Giant Fungus Treetop Village: An ancient forest of colossal bioluminescent mushrooms, where communities of creatures, including humans, have constructed treetop villages. The story could center around the lives and adventures of these inhabitants.",
    "Stealth Archipelago: A hidden archipelago shrouded in perpetual mist, home to a society of stealthy ninja-like inhabitants. Characters could be trained in the ways of the archipelago's secretive arts, navigating through treacherous conditions.",
    "Holographic Amusement Park: An underground amusement park where holographic technology creates an ever-shifting landscape filled with fantastical rides, games, and experiences. The story might follow visitors as they explore this magical entertainment world.",
    "Living Coral Reef Civilization: Beneath the ocean's surface, an advanced civilization exists among the living coral reefs. The narrative could delve into the culture and challenges of these marine beings, who have harnessed the power of the coral.",
    "Elemental Artisan Realms: A multiverse where each realm is dedicated to crafting a specific element—fire, water, earth, or air. The story might revolve around a character's journey to master their chosen element and save the multiverse.",
    "Library of Forgotten Emotions: An ancient, mystical library containing forgotten emotions captured in physical form. Characters could explore the library's vast collection of emotional experiences and their impact on the world.",
    "Timeless Wilderness: In a realm untouched by time, characters encounter ancient creatures and landscapes from various historical eras. The story could focus on the adventure of exploring these time-warped regions.",
    "Pirate Ship Graveyard: A hidden graveyard beneath the ocean's surface, filled with the remains of sunken pirate ships and treasures. The story might revolve around underwater archaeologists, explorers, or salvagers who seek the riches and mysteries hidden within these wrecks.",
    "Moonlit Treetop City: In the canopy of an ancient moonlit forest, an enchanting treetop city thrives. Illuminated by the soft glow of the moon, the city's inhabitants include mystical creatures, and the story may follow an outsider's journey to discover its secrets.",
    "Quantum World Nexus: At the heart of a surreal landscape, a nexus point connects multiple parallel worlds. Characters could travel between these realities, each with unique laws of physics and realities.",
    "Aeolian Skyport: In an endless sky filled with colossal airships, a bustling skyport serves as a hub for trade and adventure. The story might follow the crew of one such airship and their high-flying escapades."
    "Living Ice Palace: In an icy realm, an enchanting ice palace comes to life, constantly shifting and growing as characters explore its frozen halls. The narrative may delve into the mysteries and dangers within the living ice.",
    "Aurora Canyon: Set in a massive canyon beneath a sky filled with constant northern lights, the canyon walls are covered in phosphorescent crystals, creating a breathtaking natural display. Characters could navigate this unique environment and its luminescent beauty.",
    "Kinetic Wilderness: A realm where the environment is in constant motion, with geological features and flora that shift and change. The story could revolve around characters learning to adapt and survive in this dynamic landscape.",
    "Lost Orbital Station: In the vastness of space, a long-lost orbital station reappears, seemingly abandoned but with remnants of its previous crew and secrets to uncover. The narrative may explore the station's history and the challenges faced by those who discover it.",
    "Sonic Symphony Caverns: A network of caves where sound is tangible and takes on physical form. Characters might venture into this cavernous world to harness the power of sound or navigate its musical challenges.",
    "The Lighthouse Archipelago: A series of remote islands with ancient lighthouses that serve as portals to other dimensions. The story could involve characters exploring these islands, uncovering the mysteries of the lighthouses, and their interdimensional journeys.",
    "Weather Wizardry School: In a hidden school for weather wizards, students learn to control and manipulate the elements. The narrative may follow a young aspiring weather wizard as they navigate the challenges and politics of this magical institution.",
    "Avalanche Academy: In a snow-covered mountain range, a secluded academy teaches the art of controlling avalanches for various purposes, including avalanche rescue and defense against natural disasters.",
    "Village of Floating Lanterns: A secluded village built on stilts in a vast, serene lake. The inhabitants use floating lanterns to light up the village at night, creating a tranquil and picturesque atmosphere.",
    "Crystalline Subterrane: A hidden underground world composed entirely of luminous crystals. The characters could navigate this surreal environment and uncover its secrets while facing challenges unique to the crystalline landscape.",
    "Arcane Circus Troupe: Within a mystical forest, an ancient circus troupe, composed of magical beings, performs extraordinary feats and illusions under the enchanting moonlight. The story may center around the lives and adventures of the circus members.",
    "Echoing Catacombs: An underground labyrinth of catacombs where echoes hold magical properties. Characters could explore the catacombs, utilizing echoes to solve puzzles, communicate, or confront mysterious entities.",
    "Celestial Observatory: Perched on a mountaintop, an observatory enables observers to witness celestial events from other galaxies. The story could follow the lives of astronomers who uncover profound cosmic truths.",
    "River of Memories: A river with waters that capture and reflect the memories of those who touch it. Characters may embark on a journey along this river, discovering the hidden stories within its shimmering depths.",
    "Aquatic Nomads of the Underground Sea: In an underground sea, nomadic communities live on floating islands and navigate the vast underground waters. The narrative might revolve around their resourcefulness and encounters with unique sea creatures.",
    "Uncharted Rainforest Valley: A remote rainforest valley untouched by civilization, teeming with undiscovered flora and fauna. The story could follow explorers and researchers as they venture into this uncharted wilderness.",
    "Time-Looped Metropolis: A sprawling city where time loops and replays specific days or moments in history. The narrative might explore the impact of this temporal anomaly on the city's inhabitants and the search for a way to break the cycle.",
    "Psychic Carnival: A mysterious traveling carnival where psychic abilities are showcased. The story could center around the lives of the performers and the secrets they hold in this otherworldly carnival.",
    "Monumental Graveyard of Giants: In a forgotten desert, enormous statues of long-extinct giants lay buried beneath the sands. The narrative may follow archaeologists and treasure hunters who seek to unearth the secrets and treasures hidden within this colossal graveyard.",
    "Village of Color-Changing Leaves: A hidden village nestled within an ancient forest, where the leaves of trees change color based on the emotions and thoughts of the inhabitants. The story could revolve around the community's emotional harmony and struggles.",
    "Floating Marketplace of Elemental Crystals: In a skyborne city, a bustling marketplace features stalls of elemental crystals, each harnessed for various purposes. The narrative might follow traders, adventurers, and individuals who interact with these magical crystals.",
    "Symphonic Caves of Resonance: A series of underground caves known for their unique resonating properties. Sound and music create physical effects within these caves, and the story may follow musicians and explorers who harness this resonance.",
    "Crystal Petting Zoo: In a hidden valley, a unique zoo features creatures made entirely of colorful and translucent crystals. The narrative could follow the caretakers of these crystal beings and their extraordinary interactions with visitors.",
    "Aerial Silk City: Suspended high above the ground, a city is interconnected by intricate networks of silk bridges, pathways, and structures. The characters may navigate this ethereal environment and its challenges.",
    "Underwater Clockwork Metropolis: In a deep-sea metropolis, intricate clockwork mechanisms power the city's functions. The story might revolve around characters who live and work in this world of underwater engineering.",
    "Alchemy Academy of Living Elements: In an isolated academy, students learn the art of alchemy, specializing in the transformation of elements. The narrative could follow the journeys of alchemical apprentices as they unlock the secrets of their craft.",
    "Luminous Desert Oasis: Within a seemingly endless desert, a hidden oasis thrives with giant, bioluminescent plants. The story might focus on travelers who seek refuge in this radiant sanctuary.",
    "Mirror Lake of Reflection: In a serene lake, the waters reflect the thoughts, memories, and innermost desires of those who gaze into it. Characters could journey to this reflective lake to confront their inner selves and make profound discoveries.",
    "Dimensional Art Gallery: A mysterious art gallery where each painting or sculpture represents a different dimension. The narrative may follow visitors as they step into these works of art, exploring the worlds they contain.",
    "Terracotta Army Guardians: A vast underground chamber houses an army of animated terracotta soldiers tasked with guarding a hidden ancient treasure. The story could focus on those who seek to protect or pilfer this legendary hoard.",
    "Ethereal Ice Palace: A palace constructed from enchanted ice with shifting crystalline patterns. Characters could explore this otherworldly structure and uncover its enchantments and secrets.",
    "The Whispering Forest: In a mystical forest, the trees and creatures communicate through whispers carried by the wind. The story could follow characters as they navigate the forest and learn its secrets.",
    "Floating Island of Knowledge: High above the world, a floating island is a repository of knowledge, guarded by ancient scholars and enigmatic guardians. The narrative may revolve around those who seek access to its wisdom.",
    "Quantum Cityscape: A city where quantum phenomena govern daily life, allowing for teleportation, time manipulation, and other reality-bending powers. Characters could explore the city's quantum mysteries and challenges.",
    "Bazaar of Dreams: In a bustling marketplace, vendors trade in dreams and fantasies. The story might focus on characters who buy, sell, or chase their own dreams in this fantastical bazaar.",
    "Crystalized Volcano Caverns: Deep within an active volcano, caverns are adorned with luminous crystals that absorb and channel the volcano's energy. The narrative could revolve around those who harness this power.",
    "Celestial Lighthouse Keepers: A network of lighthouses in the sky guides celestial travelers through the cosmos. The story might follow the keepers of these lighthouses as they ensure safe passage among the stars.",
    "The Canopy of Lost Civilizations: In a dense treetop canopy, remnants of long-lost civilizations are hidden. Characters could explore these ancient ruins and unravel the mysteries of the arboreal world.",
    "Elemental Clockwork City: A city powered by intricate clockwork mechanisms and harnessed elemental forces. The narrative may follow residents and engineers who balance the elements to maintain the city's functionality.",
    "Museum of Forgotten Memories: A mysterious museum where visitors can explore the memories of the past. The story could focus on those who visit the museum and the emotions and revelations it stirs.",
    "Oracle's Tower: Perched on a mountaintop, a tower houses an oracle who can glimpse the future. Characters may seek the oracle's wisdom, navigate the tower's challenges, or uncover the truth behind the predictions.",
    "Living Ecosystem Spaceship: A massive spaceship functions as a self-sustaining ecosystem, carrying its inhabitants through the cosmos. The narrative might explore life aboard this organic spaceship and the challenges it presents.",
    "The Language of Elements: In a world where words carry elemental power, characters learn to wield the elements through language. The story could revolve around the journey of mastering this unique form of communication.",
]


# Function to generate and display a random prompt
def generate_prompt():
  random_prompt = random.choice(prompts)
  prompt_display.config(text=random_prompt)


# Create a Tkinter window
window = tk.Tk()
window.title("Prompt Generator")

# Create a label to display the random prompt
prompt_display = tk.Label(window, text="", wraplength=400, padx=10, pady=10)
prompt_display.pack()

# Create a button to generate a random prompt
generate_button = tk.Button(window,
                            text="Generate Prompt",
                            command=generate_prompt)
generate_button.pack()

# Initialize with an initial prompt
generate_prompt()

# Start the Tkinter main loop
window.mainloop()

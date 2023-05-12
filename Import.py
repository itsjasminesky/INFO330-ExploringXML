import sqlite3
import sys
import xml.etree.ElementTree as ET

# Incoming Pokemon MUST be in this format
#
# <pokemon pokedex="" classification="" generation="">
#     <name>...</name>
#     <hp>...</name>
#     <type>...</type>
#     <type>...</type>
#     <attack>...</attack>
#     <defense>...</defense>
#     <speed>...</speed>
#     <sp_attack>...</sp_attack>
#     <sp_defense>...</sp_defense>
#     <height><m>...</m></height>
#     <weight><kg>...</kg></weight>
#     <abilities>
#         <ability />
#     </abilities>
# </pokemon>
 #Create a Python program, Import.py, which will take an XML file as input,
#and insert new Pokemon into the pokemon.sqlite database. This will require you 

#An example Pokemon input file of that sort is given in the file Bulbasaur.xml. 
#Make sure you don't import a duplicate of a Pokemon that is already there! --->


# Read pokemon XML file name from command-line
# (Currently this code does nothing; your job is to fix that!)

if len(sys.argv) < 2:
    print("You must pass at least one XML file name containing Pokemon to insert")
    sys.exit(1)

connection = sqlite3.connect('pokemon.sqlite')
cur = connection.cursor()


#to open the file given as a command-line argument, use Python's XML
# libraries to parse the XML, then INSERT the resulting data into the database
# tavle inide the sqlite fil. 
for i, arg in enumerate(sys.argv):
    if i == 0:
        continue 

    tree = ET.parse(arg)
    root = tree.getroot()

name = root.find('name').text
pokedex = root.get('pokedexNumber')
classification = root.get('classification')
generation = root.get('generation')
hp = root.find('hp').text
attack = root.find('attack').text
defense = root.find('defense').text
speed = root.find('speed').text
sp_attack = root.find('sp_attack').text
sp_defense = root.find('sp_defense').text
height = root.find('height/m').text
weight = root.find('weight/kg').text
abilities = [ability.text for ability in root.find('abilities').iter('ability')]

# Insert the Pokemon into the database
cur.execute("""
            INSERT INTO pokemon (name, pokedex_number, classification, generation, hp, attack, defense, speed, sp_attack, sp_defense, height_m, weight_kg)"""
)

pokemon_id = cur.lastrowid

connection.commit()
connection.close()



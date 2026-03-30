import data_fetcher
import animals_web_generator

animal = input("Enter a name of an animal:")
animals_data = data_fetcher.fetch_data(animal)
if len(animals_data) == 0:
    output = f'<h2>The animal "{animal}" doesn\'t exist.</h2>'
else:
    selected_aimals = animals_web_generator.ask_skin_type(animals_data)
    # Write Cards
    output = ''
    for animal_data in animals_data:
        if animal_data["name"] in selected_aimals:
            output += animals_web_generator.serialize_animal(animal_data)

# Open Template and insert Cards
with open("animals_template.html", "r") as website:
    template = website.read()
html_with_animals = template.replace("__REPLACE_ANIMALS_INFO__", output)

# Write Output
with open("animals.html", "w") as website:
    website.write(html_with_animals)
print("Website was successfully generated to the file animals.html.")

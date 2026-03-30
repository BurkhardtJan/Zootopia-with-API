import data_fetcher


def ask_skin_type(animals_data):
    """ Asks user for skin type and returns list of all animals with it"""
    skintype_list = []
    skin_dict = {}
    selected_skin_namelist = []
    # Collect all skin-types
    for animal_data in animals_data:
        if "skin_type" in animal_data["characteristics"]:
            skin = animal_data['characteristics']['skin_type']
            skin_dict[animal_data["name"]] = skin
            if skin not in skintype_list:
                skintype_list.append(skin)
        else:
            skin_dict[animal_data["name"]] = None
    # Handle user input
    print("Press corresponding number to select a Skin-Type.")
    print("Press anything else for all Skin-Types.")
    for i in range(len(skintype_list)):
        print(f"{i + 1}: {skintype_list[i]}")
    selection = input()
    try:
        if int(selection) > 0:
            selected_skin = skintype_list[int(selection) - 1]
            print(f"You selected {selection}: {skintype_list[int(selection) - 1]}")
            for name, skin in skin_dict.items():
                if skin == selected_skin:
                    selected_skin_namelist.append(name)
            return selected_skin_namelist
        else:
            selected_skin = None
            print(f"You selected all Skin-Types")
            for name, skin in skin_dict.items():
                selected_skin_namelist.append(name)
            return selected_skin_namelist
    except:
        selected_skin = None
        print(f"You selected all Skin-Types")
        for name, skin in skin_dict.items():
            selected_skin_namelist.append(name)
        return selected_skin_namelist


def serialize_animal(animal_obj):
    """ Returns HTML Card output for single Animal"""
    output = ''
    output += '<li class="cards__item">'
    output += f'<div class="card__title">{animal_data["name"]}</div>\n'
    output += '<p class="card__text">'
    output += '<ul>'
    if "diet" in animal_data["characteristics"]:
        output += f"<li><strong>Diet:</strong> {animal_data['characteristics']['diet']}</li>\n"
    if "locations" in animal_data:
        output += f"<li><strong>Location</strong>: {animal_data['locations'][0]}</li>\n"
    if "type" in animal_data["characteristics"]:
        output += f"<li><strong>Type</strong>: {animal_data['characteristics']['type']}</li>\n"
    if "skin_type" in animal_data["characteristics"]:
        output += f"<li><strong>Skin-Type</strong>: {animal_data['characteristics']['skin_type']}</li>\n"
    output += '</ul>'
    output += '</p>'
    output += '</li>'
    return output


animal = input("Enter a name of an animal:")
animals_data = data_fetcher.fetch_data(animal)
if len(animals_data) == 0:
    output = f'<h2>The animal "{animal}" doesn\'t exist.</h2>'
else:
    selected_aimals = ask_skin_type(animals_data)
    # Write Cards
    output = ''
    for animal_data in animals_data:
        if animal_data["name"] in selected_aimals:
            output += serialize_animal(animals_data)

# Open Template and insert Cards
with open("animals_template.html", "r") as website:
    template = website.read()
html_with_animals = template.replace("__REPLACE_ANIMALS_INFO__", output)

# Write Output
with open("animals.html", "w") as website:
    website.write(html_with_animals)
print("Website was successfully generated to the file animals.html.")

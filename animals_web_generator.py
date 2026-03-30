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


def serialize_animal(animal_data):
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

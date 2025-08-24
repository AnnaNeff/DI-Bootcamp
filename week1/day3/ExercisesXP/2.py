zara_brand = dict({})
zara_brand["name"] = ["Zara"]
zara_brand["creation_date"] = 1975
zara_brand["creator_name"]= ["Amancio Ortega Gaona"]
zara_brand["type_of_clothes"] = ["men", "women", "children", "home"]
zara_brand["international_competitors"] = ["Gap", "H&M", "Benetton"]
zara_brand["number_stores"] = 7000

major_color_dict = dict({})
major_color_dict["France"] = ["blue"]
major_color_dict["Spain"] = ["red"]
major_color_dict["US"] = ["pink", "green"]

zara_brand["major_color"] = [major_color_dict]

print(zara_brand)




zara_brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": f"Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
                    "France": "blue", 
                    "Spain": "red", 
                    "US": ["pink", "green"]
                    }
}
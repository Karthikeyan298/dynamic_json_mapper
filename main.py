from dynamic_json_mapper import DynamicJsonMapper

if __name__ == '__main__':
    data_json = {
        "Name": "Karthikeyan",
        "Education": ["B.E", "HSC"],
        "City": {
            "Urban": "Tvl",
            "Rural": "Sct"
        }
    }

    mapping_template = {
        "Username_B_": {
            "Name_A_": "<data>"
        },
        "Studies_B_": {
            "Education_A_": "<data>"
        },
        "City_B_": {
            "Urban_B_": {
                "City_A_": {
                    "Urban_A_": "<data>"
                }
            }
        }
    }

    mapper = DynamicJsonMapper()

    print(mapper.map_json(mapping_template, data_json, "_B_", "_A_", "<data>"))


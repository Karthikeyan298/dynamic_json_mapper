# dynamic_json_mapper
This repo has the python script which can dynamically map json from one form to another with the given template


The dynamic json mapper needs five attributes.

* mapping template which describes how to map you source json to destination json.

* Fields end with _B_ is the destination json.

* Fields end with _A_ is the source json.

* "`<data>`" represents the location of your actual data

mapping_template:
```{
                "Username_B_": {
                    "Name_A_": "<data>"
                },
                "Studies_B_": {
                    "Education_A_": ["", "<data>"]
                },
                "City_B_": {
                    "Urban_B_": {
                        "City_A_": {
                            "Urban_A_": "<data>"
                        }
                    }
                }
            }
```            

data_json:
```{
                "Name": "Karthikeyan",
                "Education": ["B.E", "B.Sc"],
                "City": {
                    "Urban": "XYZ",
                    "Rural": "ABC"
                }
            }
        }
```
Expected output of the above template
```{
  'Username': 'Karthikeyan',
  'Studies': 'B.Sc',
  'City': {
    'Urban': 'XYZ'
  }
}
```

ids = {
    "id1":{
        "name": "Sara",
        "class": "V",
        "subjects": ["english", "math", "science"]

    },
    "id2":{
        "name": "David",
        "class": "V",
        "subjects": ["english", "math", "science"]

    },
    "id3":{
        "name": "Sara",
        "class": "V",
        "subjects": ["english", "math", "science"]

    },
    "id4":{
        "name": "Surya",
        "class": "V",
        "subjects": ["english", "math", "science"]

    }

}

result = {}

for key,val in ids.items():
        if val not in result.values():
           result[key] = val

print(result)
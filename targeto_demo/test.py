import time
import pandas as pd
from demo import data_config
start = time.time()

def value_mapping_for_string(value, value_mapping):
        if value_mapping:
            for condition in value_mapping:
                if condition["is_int_mapping"]:
                    try:
                        int_value = int(value)
                    except ValueError:
                        continue  
                    if condition["min"] is not None and condition["max"] is not None:
                        if condition["min"] <= int_value <= condition["max"]:
                            return condition["standard_value"]
                    elif condition["max"] is not None:
                        if int_value <= condition["max"]:
                            return condition["standard_value"]
                    elif condition["min"] is not None:
                        if int_value >= condition["min"]:
                            return condition["standard_value"]
                else:
                    if condition["include"] and condition["exclude"]: 
                        if value in condition["include"] and value in condition["exclude"]:
                            return condition["standard_value"]
                    elif condition["include"] is not None:
                        if value in condition["include"]:
                            return condition["standard_value"]
                    elif condition["exclude"] is not None:
                        if value not in condition["exclude"]:
                            return condition["standard_value"]
            print(value)           
            return value
        else:
            print("No mapping found")
            return value

# Load CSV data
df = pd.read_csv("C:\\Users\\abc\\Desktop\\targeto_demo\\test.csv")

# Define your education mapping
# education_mapping = {
#     "value_mapping": get_config_data()["config"][3]["value_mapping"],
#     "values_data": get_config_data()['standard_values'][0]['values_data'],
#     "data_type":'string'
# }

# Create a dictionary to map values to {unique_id, parent_id} pairs
mapping_dict = {item["value"]: (item["unique_id"], item["parent_id"]) for item in data_config['data']['standard_values'][1]["values_data"]}

def custom_map(value):
    return mapping_dict.get(value, value)

# Apply the custom mapping function
df['education_mapped'] = df['education'].apply(custom_map)
df["education"] = df["education"].map(lambda x: value_mapping_for_string(x, data_config['data']["config"][3]["value_mapping"])).map(custom_map)

# print(df)
# end = time.time()
# print('execution time' ,end-start)

values_data = [
                    {
                        "value": "75+",
                        "unique_id": 15,
                        "parent_id": 2,
                        "min": 75,
                        "max": None
                    },
                    {
                        "value": "",
                        "unique_id": 2,
                        "parent_id": 1,
                        "min": None,
                        "max": None
                    },
                    {
                        "value": "18-20",
                        "unique_id": 3,
                        "parent_id": 2,
                        "min": 18,
                        "max": 20
                    },
                    {
                        "value": "21-24",
                        "unique_id": 4,
                        "parent_id": 2,
                        "min": 21,
                        "max": 24
                    },
                    {
                        "value": "25-29",
                        "unique_id": 5,
                        "parent_id": 2,
                        "min": 25,
                        "max": 29
                    },
                    {
                        "value": "30-34",
                        "unique_id": 6,
                        "parent_id": 2,
                        "min": 30,
                        "max": 34
                    },
                    {
                        "value": "35-39",
                        "unique_id": 7,
                        "parent_id": 2,
                        "min": 35,
                        "max": 39
                    },
                    {
                        "value": "40-44",
                        "unique_id": 8,
                        "parent_id": 2,
                        "min": 40,
                        "max": 44
                    },
                    {
                        "value": "45-49",
                        "unique_id": 9,
                        "parent_id": 2,
                        "min": 45,
                        "max": 49
                    },
                    {
                        "value": "50-54",
                        "unique_id": 10,
                        "parent_id": 2,
                        "min": 50,
                        "max": 54
                    },
                    {
                        "value": "55-59",
                        "unique_id": 11,
                        "parent_id": 2,
                        "min": 55,
                        "max": 59
                    },
                    {
                        "value": "60-64",
                        "unique_id": 12,
                        "parent_id": 2,
                        "min": 60,
                        "max": 64
                    },
                    {
                        "value": "65-69",
                        "unique_id": 13,
                        "parent_id": 2,
                        "min": 65,
                        "max": 69
                    },
                    {
                        "value": "70-74",
                        "unique_id": 14,
                        "parent_id": 2,
                        "min": 70,
                        "max": 74
                    }
                ]

values_dict = {}
for standard_value in values_data:
    key = (standard_value['min'], standard_value['max'])
    values_dict[key] = (standard_value['unique_id'], standard_value['parent_id'])

def value_mapping_for_integer(value):
    for key in values_dict:
        min_val, max_val = key
        if min_val is not None and max_val is not None:
            if min_val <= value <= max_val:
                return values_dict[key]
        elif max_val is not None:
            if value <= max_val:
                return values_dict[key]
        elif min_val is not None:
            if value >= min_val:
                return values_dict[key]
            
df['age'] = df['age'].map(value_mapping_for_integer)
# print(df)
end = time.time()
print('execution time' ,end-start)

print(df.head())
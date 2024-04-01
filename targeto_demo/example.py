data_config = {
    "success": True,
    "data": {
        "total_count": "1",
        "client_id": 4,
        "site_id": 12,
        "config_id": 5,
        "name": "test config6",
        "description": "test Configsss 30 char min .....",
        "create_date": "2024-02-28T09:35:07.319Z",
        "last_update": "2024-03-01T10:52:27.684Z",
        "config": [
            {
                "column_type": {
                    "data_type": "string",
                    "column_type": "email",
                    "bypass_values": False,
                    "column_parent_type": "matchable_ids"
                },
                "value_mapping": [
                    {
                        "max": None,
                        "min": None,
                        "exclude": [],
                        "include": [],
                        "is_int_mapping": False,
                        "standard_value": ""
                    },
                    {
                        "max": 1,
                        "min": 10000,
                        "exclude": None,
                        "include": None,
                        "is_int_mapping": True,
                        "standard_value": ""
                    }
                ],
                "local_column_name": "email_locl",
                "bucket_column_name": "email_43"
            },
            {
                "column_type": {
                    "data_type": "integer",
                    "column_type": "Income (USD)",
                    "bypass_values": True,
                    "column_parent_type": "signals"
                },
                "local_column_name": "income",
                "bucket_column_name": "income_43"
            },
            {
                "column_type": {
                    "data_type": "integer",
                    "column_type": "Age Range",
                    "bypass_values": True,
                    "column_parent_type": "signals"
                },
                "local_column_name": "age",
                "bucket_column_name": "signal_age"
            },
            {
                "column_type": {
                    "data_type": "string",
                    "column_type": "Education (Highest Level)",
                    "bypass_values": True,
                    "column_parent_type": "signals"
                },
                "value_mapping": [
                    {
                        "max": 8,
                        "min": None,
                        "exclude": None,
                        "include": None,
                        "is_int_mapping": True,
                        "standard_value": "Primary Education"
                    },
                    {
                        "max": 12,
                        "min": 9,
                        "exclude": None,
                        "include": None,
                        "is_int_mapping": True,
                        "standard_value": "Secondary Education"
                    },
                    {
                        "max": None,
                        "min": None,
                        "exclude": [],
                        "include": [
                            "B.com",
                            "B.tech",
                            "BE_1",
                            "BA"
                        ],
                        "is_int_mapping": False,
                        "standard_value": "College Education"
                    },
                    {
                        "max": None,
                        "min": None,
                        "exclude": [],
                        "include": [
                            "M.Tech",
                            "PHD"
                        ],
                        "is_int_mapping": False,
                        "standard_value": "Postgraduate Education"
                    }
                ],
                "local_column_name": "study",
                "bucket_column_name": "signal_education"
            }
        ],
        "standard_values": [
            {
                "column_type": "Age Range",
                "data_type": "integer",
                "values_data": [
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
            },
            {
                "column_type": "Education (Highest Level)",
                "data_type": "string",
                "values_data": [
                    {
                        "value": "",
                        "unique_id": 17,
                        "parent_id": 16,
                        "min": None,
                        "max": None
                    },
                    {
                        "value": "Primary Education",
                        "unique_id": 18,
                        "parent_id": 17,
                        "min": None,
                        "max": None
                    },
                    {
                        "value": "Secondary Education",
                        "unique_id": 19,
                        "parent_id": 17,
                        "min": None,
                        "max": None
                    },
                    {
                        "value": "College Education",
                        "unique_id": 20,
                        "parent_id": 17,
                        "min": None,
                        "max": None
                    },
                    {
                        "value": "Professional School",
                        "unique_id": 21,
                        "parent_id": 20,
                        "min": None,
                        "max": None
                    },
                    {
                        "value": "Postgraduate Education",
                        "unique_id": 22,
                        "parent_id": 20,
                        "min": None,
                        "max": None
                    },
                    {
                        "value": "Undergraduate Education",
                        "unique_id": 23,
                        "parent_id": 20,
                        "min": None,
                        "max": None
                    }
                ]
            },
            {
                "column_type": "Income (USD)",
                "data_type": "integer",
                "values_data": [
                    {
                        "value": "$10,000-$14,999",
                        "unique_id": 165,
                        "parent_id": 164,
                        "min": 10000,
                        "max": 14999
                    },
                    {
                        "value": "$15,000-$19,999",
                        "unique_id": 166,
                        "parent_id": 164,
                        "min": 15000,
                        "max": 19999
                    },
                    {
                        "value": "$20000 - $39999",
                        "unique_id": 167,
                        "parent_id": 164,
                        "min": 20000,
                        "max": 39999
                    },
                    {
                        "value": "$40000 - $49999",
                        "unique_id": 168,
                        "parent_id": 164,
                        "min": 40000,
                        "max": 49999
                    },
                    {
                        "value": "$50000 - $74999",
                        "unique_id": 169,
                        "parent_id": 164,
                        "min": 50000,
                        "max": 74999
                    },
                    {
                        "value": "$75000 - $99999",
                        "unique_id": 170,
                        "parent_id": 164,
                        "min": 75000,
                        "max": 99999
                    },
                    {
                        "value": "$100000 - $149999",
                        "unique_id": 171,
                        "parent_id": 164,
                        "min": 100000,
                        "max": 149999
                    },
                    {
                        "value": "$150,000-$174,999",
                        "unique_id": 172,
                        "parent_id": 164,
                        "min": 150000,
                        "max": 174999
                    },
                    {
                        "value": "$175,000-$199,999",
                        "unique_id": 173,
                        "parent_id": 164,
                        "min": 175000,
                        "max": 199999
                    },
                    {
                        "value": "$200,000-$249,999",
                        "unique_id": 174,
                        "parent_id": 164,
                        "min": 200000,
                        "max": 249999
                    },
                    {
                        "value": "$250,000+",
                        "unique_id": 175,
                        "parent_id": 164,
                        "min": 250000,
                        "max": None
                    },
                    {
                        "value": "",
                        "unique_id": 164,
                        "parent_id": 163,
                        "min": None,
                        "max": None
                    }
                ]
            }
        ]
    }
}


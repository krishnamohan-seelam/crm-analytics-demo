layer_01_metrics = {
    "Total Voters": "1000",
    "New Voters": "15%",
    "Native Voters": "80%",
    "Literate Voters": "80%",
    "Police Cases": "5",
    "BPL Voters": "10%",
    "Average Age": "30",
    "Average Voter per family": "5",
    "BPL Voters": "10%",
    "Phone Nos.": "78%",
    "WhatsApp": "60%",
}
layer_02_metrics = {
    "Politically Neutral": "15%",
    "Voter Govt. Benefits": "10%",
    "Voter's Family  Govt. Benifits": "30%",
    "Voter's Accepts Money": "15%",
    "Voter's Family Accepts Money": "15%",
    "Own House": "24%",
    "Native": "56%",
}

charts_metrics = {
    "Political Party": {
        "data": {
            "Party": ["A", "B", "C"],
            "Pop": [
                20,
                10,
                19,
            ],
        },
        "x": "Party",
        "y": "Pop",
        "chart_type": "bar",
    },
    "Caste Analysis": {
        "data": {"Caste": ["A", "B", "C", "D"], "Support": [6, 10, 15, 20]},
        "x": "Caste",
        "y": "Support",
        "chart_type": "bar",
    },
    "Voter Data": {
        "data": {
            "Gender": ["Male", "Female", "Neutral"],
            "Percent": ["48%", "48%", "2%"],
            "Voter Avg Age": [34, 30, 36],
            "New Voters": [66, 38, 2],
        },
        "chart_type": "table",
    },
}
gauge_metrics = {
    "Local MLA Rating": {
        "data": {"value": 4.8, "reference": 2.5},
        "chart_type": "gauge",
    },
    "Opp MLA Rating": {
        "data": {"value": 1.8, "reference": 2.5},
        "chart_type": "gauge",
    },
    "Corporator/Village President Rating": {
        "data": {"value": 3.8, "reference": 2.5},
        "chart_type": "gauge",
    },
}

table_metrics = {
    "Voter Data": {
        "data": {
            "Gender": ["Male", "Female", "Neutral"],
            "Percent": ["48%", "48%", "2%"],
            "Voter Avg Age": [34, 30, 36],
            "New Voters": [66, 38, 2],
        },
        "chart_type": "table",
    },
}

piechart_metrics = {
    "Reservation Breakup": {
        "data": {"labels": ["A", "B", "C", "D"], "values": [20, 40, 30, 10]},
        "chart_type": "donut",
    },
    "Voter Income": {
        "data": {
            "labels": [
                "Above 10 LPA",
                "Less than 10 LPA",
                "2.5 to 5.0 LPA",
                "5 to 10 LPA",
            ],
            "values": [10, 13, 50, 27],
        },
        "chart_type": "donut",
    },
    "Voter Family Income": {
        "data": {
            "labels": [
                "Above 10 LPA",
                "Less than 10 LPA",
                "2.5 to 5.0 LPA",
                "5 to 10 LPA",
            ],
            "values": [20, 15, 35, 30],
        },
        "chart_type": "donut",
    },
    "Education": {
        "data": {
            "labels": [
                "No Education",
                "Primary",
                "SSC",
                "HSC",
                "Graduate",
                "Post Graduate"
            ],
            "values": [10, 20, 15, 15,30,10],
        },
        "chart_type": "donut",
    },
     "Profession": {
        "data": {
            "labels": [
                "Agriculture",
                "Govt",
                "Business",
                "Private",
                "Unemployed",
            ],
            "values": [33, 17, 10, 20,20],
        },
        "chart_type": "donut",
    },
}

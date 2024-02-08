import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    # 'databaseURL':"https://face-known-default-rtdb.firebaseio.com/",
    # 'databaseURL':"https://attendingclas-default-rtdb.firebaseio.com/",
    'databaseURL': "https://smartattendans-default-rtdb.firebaseio.com",
})

ref = db.reference('Students')

data = {
    "Dingane": {
        "name": "Dingane Tebeila",
        "major": "Robotics",
        "starting_year": 2020,
        "total_attendance": 9,
        "standing": "G",
        "year": 3,
        "last_attendance": "2023-06-01 05:34:16"
    },
    "Andrew": {
        "name": "Andrew Maphake",
        "major": "Policing",
        "starting_year": 2021,
        "total_attendance": 3,
        "standing": "F",
        "year": 2,
        "last_attendance": "2023-06-07 15:30:11"
    },
    "Itu": {
        "name": "Itumeleng Tebeila",
        "major": "HR",
        "starting_year": 2021,
        "total_attendance": 2,
        "standing": "P",
        "year": 2,
        "last_attendance": "2023-06-02 13:30:16"
    },
    # "Dakalo": {
    #     "name": "Dakalo Mulalo",
    #     "major": "Teaching",
    #     "starting_year": 2021,
    #     "total_attendance": 3,
    #     "standing": "F",
    #     "year": 2,
    #     "last_attendance": "2023-06-07 15:30:11"
    # },
    # "Faith": {
    #     "name": "Faith Masinga",
    #     "major": "Policing",
    #     "starting_year": 2021,
    #     "total_attendance": 3,
    #     "standing": "F",
    #     "year": 2,
    #     "last_attendance": "2023-06-07 15:30:11"
    # },
    # "Kairo": {
    #     "name": "Allison Chiloane",
    #     "major": "Boxing",
    #     "starting_year": 2021,
    #     "total_attendance": 3,
    #     "standing": "F",
    #     "year": 2,
    #     "last_attendance": "2023-06-07 15:30:11"
    # },
    "Kholo": {
        "name": "Kholofelo Seporo",
        "major": "Lying",
        "starting_year": 2021,
        "total_attendance": 3,
        "standing": "F",
        "year": 2,
        "last_attendance": "2023-06-07 15:30:11"
    },
    # "Mang": {
    #     "name": "Stranger Mahlatse",
    #     "major": "Coaching",
    #     "starting_year": 2021,
    #     "total_attendance": 3,
    #     "standing": "F",
    #     "year": 2,
    #     "last_attendance": "2023-06-07 15:30:11"
    # },
    "Mpho": {
        "name": "Gift Seporo",
        "major": "Scientist",
        "starting_year": 2021,
        "total_attendance": 3,
        "standing": "F",
        "year": 2,
        "last_attendance": "2023-06-07 15:30:11"
    },
    # "Pabi": {
    #     "name": "Paballo Nakedi",
    #     "major": "Austronomist",
    #     "starting_year": 2021,
    #     "total_attendance": 3,
    #     "standing": "F",
    #     "year": 2,
    #     "last_attendance": "2023-06-07 15:30:11"
    # },
    "Shadi": {
        "name": "Mashadi Tebeila",
        "major": "Comrade",
        "starting_year": 2021,
        "total_attendance": 3,
        "standing": "F",
        "year": 2,
        "last_attendance": "2023-06-07 15:30:11"
    },
    # "Zowii": {
    #     "name": "Zowii Chiloane",
    #     "major": "Mathematician",
    #     "starting_year": 2021,
    #     "total_attendance": 3,
    #     "standing": "F",
    #     "year": 2,
    #     "last_attendance": "2023-06-07 15:30:11"
    # },
    # "Rato": {
    #     "name": "Lerato Chiloane",
    #     "major": "Marketing",
    #     "starting_year": 2022,
    #     "total_attendance": 10,
    #     "standing": "E",
    #     "year": 2,
    #     "last_attendance": "2023-06-09 15:00:16"
    # },
    # "Gladys": {
    #     "name": "Gladys Tebeila",
    #     "major": "Networking",
    #     "starting_year": 2020,
    #     "total_attendance": 12,
    #     "standing": "G",
    #     "year": 3,
    #     "last_attendance": "2023-06-01 05:34:16"
    # }
}

for key, value in data.items():
    ref.child(key).set(value)
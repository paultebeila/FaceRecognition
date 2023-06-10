import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://face-known-default-rtdb.firebaseio.com/"
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
    "Rato": {
        "name": "Lerato Chiloane",
        "major": "Marketing",
        "starting_year": 2022,
        "total_attendance": 10,
        "standing": "E",
        "year": 2,
        "last_attendance": "2023-06-09 15:00:16"
    },
    "321654": {
        "name": "Lekula Test",
        "major": "Physics",
        "starting_year": 2021,
        "total_attendance": 3,
        "standing": "P",
        "year": 2,
        "last_attendance": "2023-06-07 15:30:11"
    }
}

for key, value in data.items():
    ref.child(key).set(value)
from pyrebase import pyrebase
import firebaseConfigFile
import numpy as np

firebase = pyrebase.initialize_app(firebaseConfigFile.firebaseConfig)
storage = firebase.storage()
db = firebase.database()


def readFirebase(variablesObject):
    data = db.child("state/pi1").get()
    if data.val() == 0:
        print("henüz soru yok")
        return 0

    elif data.val() == 1:
        print("soru geldi")
        questionArray = []
        keyArray = ["question", "a", "b", "c", "d", "e"]

        data = (db.child("questions/pi1").get()).val()

        for i in keyArray:
            questionArray.append(data[i])

        questionArray = np.asarray(questionArray)

        variablesObject.setQuestion(questionArray)
        storage.child("pi1/2.jpg").download("1.jpg")
        print(questionArray)
        return 1


def writeFirebase(answer):
    db.child("state/pi1").set(0)
    db.child("answers/pi1").set(answer)

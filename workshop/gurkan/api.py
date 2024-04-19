from flask import Flask, request

app = Flask(__name__)

kisiler = [

    {"id": 1, "ad" : "Gamze", "soyad": "Topçu", "görev": "Kayıtçı"},
    {"id": 2,"ad" : "Gürkan", "soyad": "Yılmaz", "görev": "İzleyici"},
    {"id": 3,"ad": "Seher", "soyad": "Sarı", "görev": "Repocu"},
    {"id": 4,"ad": "İrem", "soyad": "Balaban", "görev": "İzleyici"},
    {"id": 5,"ad": "Çağrı", "soyad": "Daşkın", "görev": "İzleyici"},
    {"id": 6,"ad": "Yunus Emre", "soyad": "Önder", "görev": "İzleyici"}

]

@app.route('/api/v1/kisi', methods=['GET'])

def get_kisi():
    try:
        return {"status": "ok", "message": "başarılı", "data": kisiler}, 200

    except Exception as ex:
        return {"status": "fail", "message": ex.args[0], "data": None}, 404

@app.route('/api/v1/kisi', methods=['PUT'])
def add_kisi():
    try:
        gelen_kisi = request.json
        kisiler.append(
            {
            "id":7,
            "ad" : gelen_kisi["ad"],
            "soyad" : gelen_kisi["soyad"],
            "görev" : gelen_kisi["görev"]
        })
        print (kisiler)
        return {"status": "ok", "message": "kisi eklendi", "id" : 7 }, 201


    except Exception as ex:
        return {"status": "fail", "message": ex.args[0]}, 404


@app.route('/api/v1/kisi/<int:_id>', methods=['DELETE'])
def delete_kisi(_id):
    try:
        for kisi in kisiler:
            if kisi["id"] == _id:
                kisiler.remove(kisi)
                return {"status": "ok", "message": "kisi silindi"}, 202


    except Exception as ex:
        return {"status": "fail", "message": ex.args[0]}, 400

@app.route('/api/v1/kisi/<int:_id>', methods=['PATCH'])
def update_kisi(_id):
    try:
        gelen_veri = request.json

        for kisi in kisiler:
            if kisi["id"] == _id:
                kisi["soyad"] = gelen_veri.get("soyad", kisi["soyad"])
                return {"status": "ok", "message": "kisi değiştirildi"}, 200


    except Exception as ex:
        return {"status": "fail", "message": ex.args[0]}, 400


def sunucuyu_ayaga_kaldir():
    app.run()

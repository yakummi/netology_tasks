from flask import Flask, request
from flask import jsonify
from flask.views import MethodView
from db import Advertisements, Session
import requests

app = Flask('app')


class SiteMethods(MethodView):

    def get(self, advertisements_id: int):
        with Session() as session:
            advertisements_id = session.query(Advertisements).get(advertisements_id)

            return jsonify({
                'id': advertisements_id.id,
                'description': advertisements_id.description,
                'owner': advertisements_id.owner,
                'header': advertisements_id.header,
                'creation_date': advertisements_id.creation_date
            })

    def post(self):
        json_data = request.json
        with Session() as session:
            new_advertisements = Advertisements(**json_data)
            session.add(new_advertisements)
            session.commit()
            return jsonify({
                'id': new_advertisements.id,
                'description': new_advertisements.description,
                'header': new_advertisements.header,
                'owner': new_advertisements.owner,
                'creation_date': new_advertisements.creation_date.timestamp()
            })


    def delete(self, advertisements_id: int):
        with Session() as session:
            session.query(Advertisements).filter_by(id=advertisements_id).delete()
            session.commit()
            return jsonify({
                'status': 'succesfully delete!'
            })

app.add_url_rule('/advertisements/<int:advertisements_id>', view_func=SiteMethods.as_view('advertisements_id'), methods=['GET', 'DELETE']) # делаем url

app.add_url_rule('/advertisements/', view_func=SiteMethods.as_view('advertisements'), methods=['POST'])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5003)

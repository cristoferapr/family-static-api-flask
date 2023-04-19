"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")
jackson_family.add_member("John", 33, [7, 13, 22])
jackson_family.add_member("Jane", 35, [10, 14, 3])
jackson_family.add_member("Jimmy", 5, [1])

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route("/member/<int:member_id>")
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member is not None:
        return jsonify(member), 200
    return jsonify("member id not found"), 404

@app.route('/member', methods=['POST'])
def add_member():
    data = request.get_json()
    
    if 'first_name' not in data or 'age' not in data or 'lucky_numbers' not in data:
        return jsonify({'error': 'missing required fields'}), 400

    member_id = data.get('id')
    if member_id:
        member = jackson_family.get_member(member_id)
        if member is not None:
            return jsonify({'error': f'member with ID {member_id} already exists'}), 400
    else:
        # Generate a new member ID
        member_id = jackson_family._generateId()

    jackson_family.add_member(data['first_name'], data['age'], data['lucky_numbers'], member_id)
    
    return jsonify("member added succesfully"), 200

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    result = jackson_family.delete_member(member_id)
    if 'error' in result:
        return jsonify(result), 400
    return jsonify(result), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)

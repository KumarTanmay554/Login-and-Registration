from flask import Flask, jsonify, request,session,redirect
from passlib.hash import pbkdf2_sha256
from app import db
import uuid

# Mkaing Class Person
class Person:

    def start_session(self, person):
        del person['password']
        session['logged_in'] = True
        session['user'] = person
        return jsonify(person), 200

    def signup(self):
        print(request.form)

    #object person

    def signup(self):

        person = {
            "_id": uuid.uuid4().hex, #random uuid
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }

        # Encrypting the password using hash
        person['password'] = pbkdf2_sha256.encrypt(person['password'])

        # Check for existing email----Returns one document that satisfies the specified query criteria on the collection 
        if db.users.find_one({ "email": person['email'] }):
            return jsonify({ "error": "Email address already in use" }), 400
        
    def signout(self):
        session.clear() #to end session
        return redirect('/')
    
    def login(self):
        person = db.person.find.one({
            "email":request.find_one('email')
        })

        if person and pbkdf2_sha256.verify(request.form.get('password'), person['password']):
            return self.start_session(person)
    
        return jsonify({ "error": "Invalid" }), 401

        
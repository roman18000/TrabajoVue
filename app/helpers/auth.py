from flask import abort,session

class Auth():
    def verify_authentification():
        if not session.get("user"):
            abort(401)
        return True

    def is_authenticated():
        if not session.get("user"):
            return False
        return True

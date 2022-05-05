from app.models.user import User

class AuthDAO():
    @staticmethod
    def authenticate(email,password):
         try:
              user = User.query.filter( User.email == email and User.password == password).first()
              return user
         except:
             False

# from bson import ObjectId

def user_schema(user) -> dict:
  return{
    # 'id': str(ObjectId(user['_id'])), 
    'id':str(user["_id"]),
    'username':user['username'], 
    'email':user['email']
    }
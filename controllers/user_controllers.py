from fastapi import APIRouter, HTTPException, Response, status
from models.user_model import LoginUser, RegisterUser
from config.db_helpers import get_users_collection
from schemas.userSchema import user_serializer

user_router = APIRouter()

collection = get_users_collection()

@user_router.post('/login', tags=["User routes"])
def login_user(loginUser: LoginUser, response: Response):
    db_user = collection.find_one({'email': LoginUser.email.lower()})
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Incorrect Email or Password')
    
    if not db_user['password'] == loginUser.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Incorrect Email or Password')
    
    return {'status': 'success', 'user': db_user}


@user_router.post('/register', tags=["User routes"])
def create_user(registerUser: RegisterUser, response: Response):
    user = collection.find_one({'email': registerUser.email.lower()})
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail='Account already exists')
    collection.insert_one(dict(registerUser))
    new_user = user_serializer(collection.find_one({'email': registerUser.email.lower()}))
    return {"status": "success", 'user': new_user}
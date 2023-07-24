from config.database import db

def get_users_collection():
    return db['users']

def get_workers_collection():
    return db['workers']

def get_vehicles_collection():
    return db['vehicles']
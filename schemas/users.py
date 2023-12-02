def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "username": item["username"],
        "email": item["email"],
        "full_name": item["full_name"],
        "disabled": item["disabled"],
        "hashed_password": item["hashed_password"]
        }
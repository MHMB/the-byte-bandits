from fastapi import APIRouter

router = APIRouter()

@router.get("/user/{username}")
def get_user(username: str):
    # TODO: Fetch user profile
    return {"user": {"username": username}}

@router.post("/user/{username}/risk")
def update_risk_profile(username: str):
    # TODO: Update risk profile
    return {"message": "Risk profile updated"} 
from fastapi import HTTPException
from fastapi import APIRouter
from agents.pipeline import chain

router = APIRouter()
@router.get('/generate')
async def get_user_prompt(query:str):
    try:
        print(f"{query} received at the endpoint")
        response=chain(query)
        print(response)
        return {"success":True,'data':response}
    except Exception as e:
        print(f"Error in get_sql_query: {str(e)}")
        raise HTTPException(status_code=400,detail=f"Error:{str(e)}")
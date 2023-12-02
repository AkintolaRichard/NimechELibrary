from fastapi import APIRouter, HTTPException, status, Depends
from bson.objectid import ObjectId

from models.materials import Material, Search
from config.db import materials_collection
from schemas.materials import materialEntity, materialsEntity, searchEntity
from models.users import User
from routes.users import get_current_active_user

material = APIRouter()

@material.get('/api/v1.0/materials')
async def find_all_materials(page: int = 1):
    """Get all the materials
    :return: All the materials
    :rtype: Dict
    """
    pageNum = (page - 1) * 10
    return materialsEntity(materials_collection.find().skip(pageNum).limit(10))

@material.post('/api/v1.0/materials')
async def upload_material(material: Material, current_user: User = Depends(get_current_active_user)):
    """Upload material

    :param: Material
    :raise HTTPException: 404
    :return: success message
    :rtype: json
    """
    try:
        materials_collection.insert_one(dict(material))
        return {"message": "successful"}
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Can't store the material details")

@material.post('/api/v1.0/materials/search')
async def find_materials(search: Search):
    thestr = dict(search)
    thestr = thestr["searchword"]
    return searchEntity(materials_collection.find(), thestr)

@material.put('/api/v1.0/materials/{id}/material')
async def update_material(id, material: Material, current_user: User = Depends(get_current_active_user)):
    materials_collection.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(material)
        })
    return materialEntity(materials_collection.find_one({"_id":ObjectId(id)}))

@material.delete('/api/v1.0/materials/{id}/material')
async def delete_material(id, current_user: User = Depends(get_current_active_user)):
    """Delete material

    :param id: mongodb id
    :raise HTTPException: 404
    :return: deleted material details
    :rtype: json
    """
    try:
        return materialEntity(materials_collection.find_one_and_delete({"_id":ObjectId(id)}))
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The material is not available")
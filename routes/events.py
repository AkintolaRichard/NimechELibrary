from fastapi import APIRouter, HTTPException, status, Depends
from bson.objectid import ObjectId

from models.events import Event
from config.db import events_collection
from schemas.events import eventEntity, eventsEntity
from models.users import User
from routes.users import get_current_active_user

event = APIRouter()

@event.get('/api/v1.0/events')
async def find_all_events():
    """Get all the events
    :return: All the materials
    :rtype: Dict
    """
    return eventsEntity(events_collection.find())

@event.get('/api/v1.0/events/{id}/event')
async def find_an_event(id):
    """Get an event

    :param id: mongodb id
    :raise HTTPException: 404
    :return: an event
    :rtype: json
    """
    try:
        return eventEntity(events_collection.find_one({"_id":ObjectId(id)}))
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No such event")

@event.post('/api/v1.0/events')
async def create_event(event: Event, current_user: User = Depends(get_current_active_user)):
    """Register an event

    :param: Event
    :raise HTTPException: 400
    :return: success message
    :rtype: json
    """
    try:
        events_collection.insert_one(dict(event))
        return {"message": "successful"}
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Can't register the event")

@event.put('/api/v1.0/events/{id}/event')
async def update_event(id, event: Event, current_user: User = Depends(get_current_active_user)):
    events_collection.find_one_and_update({"_id":ObjectId(id)},
                                          {
                                              "$set":dict(event)
                                            })
    return eventEntity(events_collection.find_one({"_id":ObjectId(id)}))

@event.delete('/api/v1.0/events/{id}/event')
async def delete_event(id, current_user: User = Depends(get_current_active_user)):
    """Delete event

    :param id: mongodb id
    :raise HTTPException: 404
    :return: deleted event
    :rtype: json
    """
    try:
        return eventEntity(events_collection.find_one_and_delete({"_id":ObjectId(id)}))
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No such event")
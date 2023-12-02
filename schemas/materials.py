def materialEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "courseCode": item["courseCode"],
        "courseName": item["courseName"],
        "courseLecturer": item["courseLecturer"],
        "materialName": item["materialName"],
        "url": item["url"]
        }

def materialsEntity(entity) -> list:
    return [materialEntity(item) for item in entity]

def searchEntity(entity, thestr) -> list:
    thestr = thestr.lower()
    return [materialEntity(item) for item in entity \
            if thestr in str(item["courseCode"]).lower() or \
            thestr == str(item["courseName"]).lower() or \
            thestr in str(item["materialName"]).lower() or \
            thestr in str(item["courseLecturer"]).lower()
            ]

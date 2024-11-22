from datetime import datetime, timedelta

def resolve_retrieve_recent_history(_, info, limit=None):
    limit = limit or 10
    db = info.context['db']
    recent_history = list(db.queries.find().sort("_id", -1).limit(limit))
    return recent_history


def resolve_retrieve_query(_, info, name):
    query = {"name": {"$regex": name, "$options": "i"}}
    result = info.context['db'].queries.find_one(query)
    return result


def resolve_save_query(_, info, input):
    query = {"name": input.get("name")} # Assuming "name" is a unique identifier
    input["timestamp"] = datetime.utcnow() + timedelta(hours=2) # WARNING: UTC + 2 only correct when not using DST
    update_result = info.context['db'].queries.update_one(
        query,
        {"$set": input},
        upsert=True  # This ensures insertion if no document matches the query
    )
    if update_result.upserted_id:
        output = f'New item added: {input.get("name")}'
    else:
        output = f'Item overwritten: {input.get("name")}'
    return output

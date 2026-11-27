def open_desk(role, store, failed_pickup=None):
    rows = []
    for pickup in store.waiting_pickups():
        row = {"name": pickup.name}
        if role == "dispatcher":
            row["pickup_id"] = pickup.id
            if pickup.id == failed_pickup:
                row["error"] = "Pickup could not be saved"
                row["action"] = "Retry pickup"
            else:
                row["action"] = "Mark picked up"
        rows.append(row)
    return {"rows": rows, "message": "" if rows else "No pickups waiting"}


def collect(role, pickup_id, store):
    if role != "dispatcher":
        raise PermissionError
    try:
        store.mark_collected(pickup_id)
    except OSError:
        return open_desk(role, store, failed_pickup=pickup_id)
    store.record_event("pickup.collected", pickup_id)
    return open_desk(role, store)

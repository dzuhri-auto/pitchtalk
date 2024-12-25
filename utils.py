def contruct_product_datas(product_datas=[]):
    temp_datas = {"max_level": 3, "max_speed_boost": 5, "max_time_boost": 5}
    for datas in product_datas:
        if datas.get("type").lower() not in ("level", "speed_boost", "time_boost"):
            continue
        if datas.get("type").lower() == "level" and datas.get("requirementLevel") > temp_datas.get(
            "max_level"
        ):
            temp_datas["max_level"] = datas.get("requirementLevel")
        elif datas.get("type").lower() == "speed_boost" and datas.get(
            "requirementLevel"
        ) > temp_datas.get("max_speed_boost"):
            temp_datas["max_speed_boost"] = datas.get("requirementLevel")
        elif datas.get("type").lower() == "time_boost" and datas.get(
            "requirementLevel"
        ) > temp_datas.get("max_time_boost"):
            temp_datas["max_time_boost"] = datas.get("requirementLevel")
    return temp_datas

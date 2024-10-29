import os

from bot.utils import logger
from helpers import get_tele_user_obj_from_query_id


async def register_query_id() -> None:
    query_file_name = "query_ids.txt"
    add = True
    while add:
        query_id = input("\nPlease input query id (press Enter to exit): ")

        if not query_id:
            break

        tele_user_obj = get_tele_user_obj_from_query_id(query_id)
        username = tele_user_obj.get("username")
        first_name = tele_user_obj.get("first_name")
        last_name = tele_user_obj.get("last_name")

        if os.path.exists(query_file_name):
            if os.path.getsize(query_file_name) > 0:
                # Open the file in append mode and add the input value
                with open(query_file_name, "a") as file:
                    file.write("\n" + query_id)
                    logger.success(
                        f"Successfully added @{username} | {first_name} {last_name} to {query_file_name}"
                    )
            else:
                # initial
                with open(query_file_name, "a") as file:
                    file.write(query_id)
                    logger.success(
                        f"Successfully added @{username} | {first_name} {last_name} to {query_file_name}"
                    )
        else:
            logger.success(f"{query_file_name} does not exist.")

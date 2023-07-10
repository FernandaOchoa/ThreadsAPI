from threads_api import ThreadsAPI
import asyncio

async def get_user_profile_threads(print_threads=False):
    threads_api = ThreadsAPI()

    username = "fherz8a"
    user_id = await threads_api.get_user_id_from_username(username)

    result = []

    if user_id:
        threads = await threads_api.get_user_profile_threads(username, user_id)
        for thread in threads:
            text = thread['thread_items'][0]['post']['caption']
            likes = thread['thread_items'][0]['post']['like_count']
            result.append({'text': text, 'likes': likes})
            

            if print_threads:
                print(f"Text: {text} || Likes: {likes}")

        return result
    else:
        if print_threads:
            print(f"User ID not found for username '{username}'")
        return None

if __name__ == "__main__":
    asyncio.run(get_user_profile_threads(print_threads=True))

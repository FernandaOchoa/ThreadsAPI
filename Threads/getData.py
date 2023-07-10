from get_user_profile_threads import get_user_profile_threads
import asyncio
import pandas as pd

threads_data = asyncio.run(get_user_profile_threads())

if threads_data is not None:
    cleanThreads = []
    likes_data =[]
    chars = ['"', "'", '}', '{', 'text', '\n', ':', '\'', '\"']

    for thread in threads_data:
        for char in chars:
            thread = str(thread).lstrip(' ')
            thread = str(thread).replace(char, '').lstrip('"\'')
        if ', likes' in thread:
            split_data = thread.split(', likes')
            cleanThreads.append(split_data[0])
            likes_data.append(split_data[1])
        else:
            cleanThreads.append(thread)
            likes_data.append('0')  
    df = pd.DataFrame({
        'Cleaned Text': cleanThreads,
        'Likes': likes_data
    })
    print(df)
df.to_csv('./data/data.csv', index=False,header=False)


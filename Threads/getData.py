from get_user_profile_threads import get_user_profile_threads
import asyncio
import pandas as pd

threadsData = asyncio.run(get_user_profile_threads())

if threadsData is not None:
    cleanThreads = []
    likesData =[]
    chars = ['"', "'", '}', '{', 'text', '\n', ':', '\'', '\"']

    for thread in threadsData:
        for char in chars:
            thread = str(thread).lstrip(' ')
            thread = str(thread).replace(char, '').lstrip('"\'')
        if ', likes' in thread:
            split_data = thread.split(', likes')
            cleanThreads.append(split_data[0])
            likesData.append(split_data[1])
        else:
            cleanThreads.append(thread)
            likesData.append('0')  
    df = pd.DataFrame({
        'Text': cleanThreads,
        'Likes': likesData
    })
    df = df.dropna()
    df['Text'] = df['Text'].replace('\\\\n', '', regex=True)
    df['Text'] = df['Text'].replace('\\\\n\\\\n', '', regex=True)
    print(df)
df.to_csv('./data/data.csv', index=False,header=False)


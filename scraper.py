import random
import time
import requests
import json


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.5.708 Yowser/2.5 Safari/537.36',
}
for page in range(1, 11):

    url = f'https://hearthstone.blizzard.com/en-us/api/community/leaderboardsData?region=EU&leaderboardId=arena&page={page}&seasonId=36'

    req = requests.get(url, headers=headers)

    src = req.text
    json_ranks = json.loads(src)

    rows = json_ranks['leaderboard']

    full_data = []

    for item in rows['rows']:
        rank = item['rank']
        accountid = item['accountid']
        rating = item['rating']

        full_data.append(
            {
                'Rank': rank,
                'Account': accountid,
                'Rating': rating
            }
        )

    with open(f'player_data/page_{page}.json', 'a', encoding='utf-8') as file:
        json.dump(full_data, file, indent=4, ensure_ascii=False)

    time.sleep(random.randrange(2, 4))

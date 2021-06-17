from InstagramAPI import InstagramAPI
import json
import Config

def getTotalFollowers(api, user_id):

    followers = []
    next_max_id = True
    while next_max_id:
        if next_max_id is True:
            next_max_id = ''

        _ = api.getUserFollowers(user_id, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return followers

def getTotalFollowings(api, user_id):
    followers = []
    next_max_id = True
    while next_max_id:
        if next_max_id is True:
            next_max_id = ''

        _ = api.getUserFollowings(user_id, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return followers

#----------------------------
api=InstagramAPI(Config.Email,Config.Password)
api.login()

user_id=api.username_id
followers=getTotalFollowers(api,user_id)
#print("จำนวนผู้ติดตาม = ",len(followers))
followings=getTotalFollowings(api,user_id)
#print("เราติดตาม = ",len(followings))

#api.getProfileData()
#api.getSelfUserFeed()
#api.getTimeline()
api.getSelfUserFollowers()
with open('data.json','w') as outfile :
     json.dump(api.LastJson,outfile)



class my_instagram:
    def __init__(self,name,user_id,followers,following,posts):
        self.name=""
        self.user_id=""
        self.followers=followers
        self.following=following
        self.posts=posts
    def num_followers(self):
        self.followers+=1   
    def num_following(self):
        self.following+=1   
    def added_post(self):
        self.posts+=1
user=my_instagram("meghana","meg_1",20,30,4)
print(user.followers)
print(user.following)
print(user.posts)
user.num_followers()
print(user.followers)
user.num_following()
print(user.following)
user.added_post()
print(user.posts)
import pandas as pd
from pymongo import MongoClient
import numpy as np

# 1. Load all CSVs
print("Loading data...")
users_df = pd.read_csv('Users.csv', low_memory=False)
posts_df = pd.read_csv('Posts.csv', low_memory=False)
comments_df = pd.read_csv('Comments.csv', low_memory=False)
badges_df = pd.read_csv('Badges.csv', low_memory=False)  # NEW

# Clean NaN
users_df = users_df.replace({np.nan: None})
posts_df = posts_df.replace({np.nan: None})
comments_df = comments_df.replace({np.nan: None})
badges_df = badges_df.replace({np.nan: None})  # NEW

# ------------------------------------------
# 2. COMMENTS → PostId
# ------------------------------------------
print("Grouping Comments by Post...")
comment_map = {}
for comment in comments_df.to_dict('records'):
    pid = comment.get('PostId')
    comment_map.setdefault(pid, []).append(comment)

# ------------------------------------------
# 3. POSTS → OwnerUserId 
# ------------------------------------------
print("Grouping Posts by User and Nesting Comments...")
post_map = {}
for post in posts_df.to_dict('records'):
    post['Comments'] = comment_map.get(post['Id'], [])
    uid = post.get('OwnerUserId')
    post_map.setdefault(uid, []).append(post)

# ------------------------------------------
# 4. BADGES → UserId  
# ------------------------------------------
print("Grouping Badges by User...")
badge_map = {}
for badge in badges_df.to_dict('records'):
    uid = badge.get('UserId')
    badge_map.setdefault(uid, []).append(badge)

# ------------------------------------------
# 5. FINAL ASSEMBLY
# ------------------------------------------
client = MongoClient('mongodb://localhost:27017/')
db = client['superuser']
collection = db.DeepNestedUsers

batch = []
batch_size = 300  

print("Starting final assembly and insertion...")

for user in users_df.to_dict('records'):
    
    uid = user.get('Id')
    
    # Embed posts
    user['MyPosts'] = post_map.get(uid, [])
    
    # Embed badges  ✅ NEW
    user['Badges'] = badge_map.get(uid, [])
    
    batch.append(user)
    
    if len(batch) >= batch_size:
        collection.insert_many(batch)
        batch = []

# Insert remaining
if batch:
    collection.insert_many(batch)

print(" Done! Users now have Posts + Comments + Badges embedded.")
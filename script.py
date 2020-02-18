# -*- coding: utf-8 -*-
"""
 @Time    : 2020/2/15 19:26
 @Author  : XiongSheng Dai
 @Contact : daixiongsheng@gmail.com
 @File    : mongo.py
 @Desc    :

"""
import json
import requests
import pymongo
import time

myclient = pymongo.MongoClient("mongodb://10.15.1.4:27017/")

class Group:
    def __init__(self, group):
        self.id = group['id']
        self.login = group['login']
        self.name = group['name']
        self.description = group['description']
        self.avatar_url = group['avatar_url']
        self.organization_id = group['organization_id']
        self.public = group['public']
        self.scene = group['scene']
        self.created_at = group['created_at']
        self.updated_at = group['updated_at']
        self.isPaid = group['isPaid']
        self.organization = group['organization']
        self.owners = group['owners']
        self._serializer = group['_serializer']

    def dict(self):
        return {
            'id': self.id,
            'login': self.login,
            'name': self.name,
            'description': self.description,
            'avatar_url': self.avatar_url,
            'public': self.public,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'isPaid': self.isPaid,
            'owners': self.owners,
            'scene': self.scene,
            'organization': self.organization,
            'organization_id': self.organization_id,
            '_serializer': self._serializer,

        }


class User:
    def __init__(self, user):
        self.id = user['id']
        self.login = user['login']
        self.name = user['name']
        self.description = user['description']
        self.avatar = user['avatar']
        self.avatar_url = user['avatar_url']
        self.followers_count = user['followers_count']
        self.following_count = user['following_count']
        self.status = user['status']
        self.public = user['public']
        self.scene = user['scene']
        self.created_at = user['created_at']
        self.updated_at = user['updated_at']
        self.isPaid = user['isPaid']
        self.profile = user['profile']
        self._serializer = user['_serializer']

    def dict(self):
        return {
            'id': self.id,
            'login': self.login,
            'name': self.name,
            'scene': self.scene,
            'description': self.description,
            'avatar': self.avatar,
            'avatar_url': self.avatar_url,
            'followers_count': self.followers_count,
            'following_count': self.following_count,
            'status': self.status,
            'public': self.public,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'isPaid': self.isPaid,
            'profile': self.profile,
            '_serializer': self._serializer,

        }


class Book:

    def __init__(self, book):
        self.id = book['id']
        self.type = book['type']
        self.slug = book['slug']
        self.name = book['name']
        self.user_id = book['user_id']
        self.description = book['description']
        self.created_at = book['created_at']
        self.updated_at = book['updated_at']
        self.content_updated_at = book['content_updated_at']
        self.public = book['public']
        self._serializer = book['_serializer']
        # self.items_count = book['items_count']
        # self.likes_count = book['likes_count']
        # self.watches_count = book['watches_count']
        # self.creator_id = book['creator_id']
        # self.source = book['source']
        # self.pinned_at = book['pinned_at']
        # self.archived_at = book['archived_at']
        # self.status = book['status']
        # self.stack_id = book['stack_id']
        # self.rank = book['rank']
        # self.creator = book['creator']
        # self.cover = book['cover']
        # self.like_count = book['like_count']

    def dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'slug': self.slug,
            'name': self.name,
            'user_id': self.user_id,
            'description': self.description,
            'public': self.public,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'content_updated_at': self.content_updated_at,
            '_serializer': self._serializer,
            # 'items_count': self.items_count,
            # 'likes_count': self.likes_count,
            # 'watches_count': self.watches_count,
            # 'creator_id': self.creator_id,
            # 'source': self.source,
            # 'pinned_at': self.pinned_at,
            # 'archived_at': self.archived_at,
            # 'status': self.status,
            # 'stack_id': self.stack_id,
            # 'rank': self.rank,
            # 'creator': self.creator,
            # 'cover': self.cover,
            # 'like_count': self.like_count,
        }


class Doc:
    def __init__(self, doc):
        self.id = doc['id']
        self.space_id = doc['space_id']
        self.type = doc['type']
        self.sub_type = doc['sub_type']
        self.title = doc['title']
        self.title_draft = doc['title_draft']
        self.tag = doc['tag']
        self.slug = doc['slug']
        self.user_id = doc['user_id']
        self.book_id = doc['book_id']
        self.last_editor_id = doc['last_editor_id']
        self.cover = doc['cover']
        self.description = doc['description']
        self.custom_description = doc['custom_description']
        self.format = doc['format']
        self.status = doc['status']
        self.read_status = doc['read_status']
        self.view_status = doc['view_status']
        self.public = doc['public']
        self.draft_version = doc['draft_version']
        self.comments_count = doc['comments_count']
        self.likes_count = doc['likes_count']
        self.content_updated_at = doc['content_updated_at']
        self.created_at = doc['created_at']
        self.updated_at = doc['updated_at']
        self.published_at = doc['published_at']
        self.first_published_at = doc['first_published_at']
        self.word_count = doc['word_count']
        self.selected_at = doc['selected_at']
        self.pinned_at = doc['pinned_at']
        self.last_editor = doc['last_editor']
        self.share = doc['share']
        self._serializer = doc['_serializer']
        pass

    def dict(self):
        return {
            'id': self.id,
            'space_id': self.space_id,
            'type': self.type,
            'sub_type': self.sub_type,
            'title': self.title,
            'title_draft': self.title_draft,
            'tag': self.tag,
            'slug': self.slug,
            'user_id': self.user_id,
            'book_id': self.book_id,
            'last_editor_id': self.last_editor_id,
            'cover': self.cover,
            'description': self.description,
            'custom_description': self.custom_description,
            'format': self.format,
            'status': self.status,
            'read_status': self.read_status,
            'view_status': self.view_status,
            'public': self.public,
            'draft_version': self.draft_version,
            'comments_count': self.comments_count,
            'likes_count': self.likes_count,
            'content_updated_at': self.content_updated_at,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'published_at': self.published_at,
            'first_published_at': self.first_published_at,
            'word_count': self.word_count,
            'selected_at': self.selected_at,
            'pinned_at': self.pinned_at,
            'last_editor': self.last_editor,
            'share': self.share,
            '_serializer': self._serializer,
        }


db = myclient['m_yuque']
uc = db['users']
bc = db['books']
dc = db['docs']
gc = db['groups']
session = requests.session()

session.headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'python requests',
}

data_url = 'https://www.yuque.com/api/explore/docs?limit=20&page={}'


def get_data(data_url):
    for page in range(1, 100):
        res = session.get(data_url.format(page))
        books, docs, users, groups = [], [], [], []
        books_id, users_id, groups_id = [], [], []
        jobj = json.loads(res.text, encoding='utf-8')

        for doc in jobj['data']:
            docs.append(Doc(doc).dict())

            user = doc['user']
            book = doc['book']
            if user['type'] == 'User':
                if user['id'] not in users_id:
                    users_id.append(user['id'])
                    users.append(User(user).dict())
            elif user['type'] == 'Group':
                if user['id'] not in groups_id:
                    groups_id.append(user['id'])
                    groups.append(Group(user).dict())

            if book['id'] not in books_id:
                books_id.append(book['id'])
                books.append(Book(book).dict())
                user = book['user']
                if user['type'] == 'User':
                    if user['id'] not in users_id:
                        users_id.append(user['id'])
                        users.append(User(user).dict())
                elif user['type'] == 'Group':
                    if user['id'] not in groups_id:
                        groups_id.append(user['id'])
                        groups.append(Group(user).dict())

        tp = [
            (bc, books),
            (uc, users),
            (dc, docs),
            (gc, groups),
        ]

        for t in tp:
            col, d = t
            i = 0
            while len(d) and i < len(d): i = (d.remove(d[i]), i)[1] if col.find(d[i]).count() != 0 else i + 1
            if len(d):
                col.insert_many(d)

        time.sleep(3)


get_data(data_url)


doc_detail_url = 'https://www.yuque.com/api/docs/{}?book_id={}'

def get_doc_detail(slug, book_id):
    url = doc_detail_url.format(slug, book_id)
    res = session.get(url)
    try:
        jobj = json.loads(res.text, encoding='utf-8')
        return jobj['data']['content']
    except:
        return ' '


for doc in dc.find():
    if 'content' in doc:
        continue
    new = doc.copy()
    new['content'] = get_doc_detail(doc['slug'], doc['book_id'])
    dc.update(doc, new)
    time.sleep(1)

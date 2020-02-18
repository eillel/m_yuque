const MongoClient = require('mongodb').MongoClient;
const url = "mongodb://10.15.1.4:27017/";
const databese = 'm_yuque'


module.exports = {
  dbo: null,
  getUser(query = {}) {
    let {id = null, limit = 20, page = 1} = query
    delete query.limit
    delete query.page
    const match = id ? {id: parseInt(id)} : {}
    limit = parseInt(limit)
    page = parseInt(page)
    return Promise.resolve(MongoClient.connect(url).then(db => {
      return db.db(databese).collection("users").find(query).skip((page-1)*limit).limit(limit).toArray()
    }));
  },

  getBook(query = {}) {
    let {id = null, limit = 20, page = 1} = query
    const match = id ? {id: parseInt(id)} : {}
    limit = parseInt(limit)
    page = parseInt(page)
    return MongoClient.connect(url)
      .then(db => {
        return db.db(databese)
          .collection("books")
          .aggregate([
            {
              $lookup: {
                from: 'users',
                localField: 'user_id',
                foreignField: 'id',
                as: 'user'
              }
            },
            {
              $lookup: {
                from: 'groups',
                localField: 'user_id',
                foreignField: 'id',
                as: 'group'
              }
            },
            {
              $match: match
            }
          ])
          .skip((page-1)*limit).limit(limit)
          .toArray()
      });
  },
  getDoc(query) {
    let {id = null, limit = 20, page = 1} = query
    const match = id ? {id: parseInt(id)} : {}
    limit = parseInt(limit)
    page = parseInt(page)
    return MongoClient.connect(url).then(db => {
      return db.db(databese).collection("docs").aggregate([
        {
          $lookup: {
            from: 'users',
            localField: 'user_id',
            foreignField: 'id',
            as: 'user'
          }
        },
        {
          $lookup: {
            from: 'books',
            localField: 'book_id',
            foreignField: 'id',
            as: 'book'
          }
        },
        {
          $match: match
        }
      ])
        .skip((page-1)*limit).limit(limit).toArray()
    });
  },

}


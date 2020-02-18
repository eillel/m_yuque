const http = require('http')
const querystring = require('querystring')
const db = require('./mongo')


const PORT = 9000
const HOST = '127.0.0.1'

const server = http.createServer(((req, res) => {

  res.setHeader("Access-Control-Allow-Origin", req.headers.origin||"*");
  res.setHeader("Access-Control-Allow-Credentials", "true");
  res.setHeader('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE,OPTIONS');
  res.setHeader('Access-Control-Request-Headers', 'access_token');
  res.setHeader("Access-Control-Allow-Headers", "Content-Type,Access-Control-Allow-Headers,Content-Length,Accept,Authorization,X-Requested-With");
  res.setHeader("Content-Type", "application/json;charset=utf-8");

  const {method, url} = req
  const [path, query] = [url.split('?')[0], querystring.parse(url.split('?')[1])]

  if (method === 'GET') {
    switch (path) {
      case '/api/users':
        db.getUser(query).then(data => {
          res.end(JSON.stringify({data:data}))
        })
        break
      case '/api/docs':
        db.getDoc(query).then(data => {
          res.end(JSON.stringify({data:data}))
        })
        break
      case '/api/books':
        db.getBook(query).then(data => {
          res.end(JSON.stringify({data:data}))
        })
        break
      default:
        res.end(JSON.stringify(
          {
            data: []
          }
        ))
    }
  }

}))

server.listen(PORT, () => {
  console.log(`listen on http://${HOST}:${PORT}`)
})

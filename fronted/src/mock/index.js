import Mock from 'mockjs'

Mock.mock('/api/user/login', {
  "status": 0,
  "data": {
    "account": "zhangsan",
    "msg": ''
  }
})

Mock.mock('/api/user/signup', {
  "status": 0,
  "data": {
    "account": "zhangsan",
    "msg": ''
  }
})
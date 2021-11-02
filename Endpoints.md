## Endpoints

| Endpoint | Request Methods |
| -------- | -------- |
|  users/register/ |  `POST`        |
|  users/login/ |    `POST`    |
|  users/logout/ |   `GET`       |
|  users/view/ |     `GET`     |
|  users/change-password/ |  `PUT`        |
|  users/<str:username>/questions/ |  `GET`       |
|  users/<str:username>/answers/ |     `GET`     |
|  users/<str:username>/update/ |      `PUT`,`PATCH`    |
|  users/<str:username>/profile_pic/upload/ |     `PUT`  |
|  question/all/ |  `GET`        |
|  question/new/ |    `POST`    |
|  question/{qid}/ |   `GET`,`PUT`,`DELETE`       |
|  question/{qid}/answer/all/ |     `GET`     |
|  question/{qid}/answer/new/ |  `POST`        |
|  question/{qid}/answer/{aid} |  `GET`,`PUT`,`DELETE`|

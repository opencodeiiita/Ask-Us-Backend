## Endpoints

| Endpoint | Request Methods |
| -------- | -------- |
|  `users/register/` |  `POST`        |
|  `users/login/` |    `POST`    |
|  `users/logout/` |   `GET`       |
|  `users/view/` |     `GET`     |
|  `users/change-password/` |  `PUT`        |
|  `users/{username}/questions/` |  `GET`       |
|  `users/{username}/answers/` |     `GET`     |
|  `users/{username}/update/` |      `PUT`,`PATCH`    |
|  `users/{username}/profile_pic/upload/` |     `PUT`  |
|  `question/all/` |  `GET`        |
|  `question/new/` |    `POST`    |
|  `question/{qid}/` |   `GET`,`PUT`,`DELETE`,`PATCH`       |
|  `question/{qid}/answer/all/` |     `GET`     |
|  `question/{qid}/answer/new/` |  `POST`        |
|  `question/{qid}/answer/{aid}/` |  `GET`,`PUT`,`DELETE`,`PATCH`|

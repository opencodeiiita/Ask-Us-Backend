## Database Schema

### User 

| Field    | Data Type | Required |
| -------- | --------- | -------- |
| first_name    | String    | true     |
| last_name    | String    | true     |
| username | String    | true     |
| email    | String    | true     |
| password | String    | true     |
| password2   | String    | true     |

### Question

| Field  | Data Type | Required |
| ------ | --------- | -------- |
| title | String     | true     |
| description   | String    | true     |
| date_posted |DateTime| false    |
| no_of_answers | Integer    | false     |
| no_of_upvotes | Integer    | false     |
| author | Foreign Key     | false     |

### Answer

| Field  | Data Type | Required |
| ------ | --------- | -------- |
| question |Foreign Key| false     |
| answer_text   |String| true     |
| date_posted |DateTime| false    |
| no_of_upvotes | Integer    | false|
| no_of_Downvotes | Integer    | false |
| author | Foreign Key     | false  |

### Profile

| Field  | Data Type | Required |
| ------ | --------- | -------- |
| user |OneToOne| false |
| profile_img  |Image| false|

User Table is related to ProfileTable through an OneToOne relationship. This means that a user can have only one Profile Image associated with them at a time.

User Table is related to Question and Answer through a foreign key relationship. If a user is deleted from the User Table, then all respective related Questions, Answers are also deleted.

Question Table is related to Answer Table through a foreign key relationship. If a question is deleted from the question Table, then all respective related Answers are also deleted from the Answer Table.

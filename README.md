# Sample Course API

URL https://avigael-course-api.herokuapp.com/

This API is used by another [project](https://github.com/avigael/test-course-api "github"). The sole purspose of this API is to return an array of course data which includes detailed information about individual courses. As well as be able to get completed courses data, or rather, courses that have previously been enrolled in by this person.

**NOTE**: This API is soley for hosting data for this specific [project](https://github.com/avigael/test-course-api "github").


------------


### Get Courses

**Definition**

`GET /courses`

**Response**

- `200 OK` on success

### Get Completed Courses

**Definition**

`GET /courses/completed`

**Response**

- `200 OK` on success

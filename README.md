## How to run
Requirements:
* python 3.5+
* Flask
* sqlite3

To run the server, navigate to the root directory
and run the following commands
1. Optional `pyenv virtualenv 3.5.2 xggity3`
2. Optional `pyenv local xggity3`
3. `pip install -r requirements.txt`
4. `python run.py`

## How to interact with the server
The server runs on localhost:8080 with 2 endpoints
* POST `localhost:8080/upsert_question`
    * You can use this endpoint to add new questions or update an existing question
    with the following syntax:
    ```
    {
        // the question text
        "question": string,
        // question id to update, which is returned when creating the question
        "question_id": Optional[number] 
    }
    ```
    * Subsequent response
    ```
    {
        // success message or error message
        "message": string,
        "error": string,
        // question id created or updated
        "question_id": number 
    }
    ```
* GET `localhost:8080/question_history/<question_id>`
    * You can use this endpoint to get a basic HTML view of the history of updates applied to a question

## My time with the project
What went well for me was establishing a data 
model that worked for all the requirements at hand. I felt like 
the needs really tended towards a very traditional relational model
which made it fairly easy for me to decide how to build it out.
Also, the tooling that python provided really helped simplify some of the more
difficult portions of the problem such as the question history diffs.

The most difficult aspect of this problem was definitely working with sqlite. 
The python api along with the database engine itself isn't really up to par with some
of the more standard solutions out there, such as PostgreSQL or MySQL.

If I had more time on this project I would definitely use PostgreSQL, modularize
the project some more, abstract a lot of the database calls behind a library
and spend more time finding a better diffing engine.

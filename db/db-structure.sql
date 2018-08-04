CREATE TABLE IF NOT EXISTS users(
  id INTEGER NOT NULL,
  sex VARCHAR NOT NULL,
  age INTEGER NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS questions(
  id INTEGER NOT NULL,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  question TEXT NOT NULL,
  PRIMARY KEY (updated_at, id)
);

CREATE TABLE IF NOT EXISTS question_responses(
  question_id INTEGER NOT NULL,
  user_id INTEGER NOT NULL,
  response TEXT NOT NULL,
  PRIMARY KEY (question_id, user_id)
);

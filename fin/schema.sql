DROP TABLE IF EXISTS parent;
DROP TABLE IF EXISTS child;
DROP TABLE IF EXISTS goal;

CREATE TABLE parent(
	parent_id INTEGER PRIMARY KEY AUTOINCREMENT,
	parent_username TEXT UNIQUE NOT NULL,
	parent_email TEXT UNIQUE NOT NULL,
	parent_password TEXT NOT NULL
);

CREATE TABLE child(
	child_id INTEGER PRIMARY KEY AUTOINCREMENT,
	child_username TEXT UNIQUE NOT NULL,
	parent_email TEXT UNIQUE NOT NULL,
	child_password TEXT NOT NULL
);

CREATE TABLE goal(
	goal_id INTEGER PRIMARY KEY AUTOINCREMENT,
	author_id INTEGER ,
	task_author INTEGER,

	goal_name TEXT UNIQUE ,
	income_amt INTEGER ,
	goal_amt INTEGER ,
	goal_saving INTEGER,

	fix_saving_amt INTEGER,
	saving_amt INTEGER ,
	emergency_amt INTEGER ,
	
	bonus INTEGER ,
    time_left INTEGER ,
	personal_amt INTEGER ,
	counter INTEGER,

	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,


	task_name  TEXT,

	task_amt INTEGER,
	task_count INTEGER,
	
	FOREIGN KEY (author_id) REFERENCES child (child_id),
	
	FOREIGN KEY (task_author) REFERENCES parent (parent_id)

);









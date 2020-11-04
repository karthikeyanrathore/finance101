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
	author_id INTEGER NOT NULL,
	
	goal_name TEXT UNIQUE NOT NULL,
	income_amt INTEGER NOT NULL,
	goal_amt INTEGER NOT NULL,
	saving_amt INTEGER NOT NULL,
	emergency_amt INTEGER NOT NULL,
	
	bonus INTEGER NOT NULL,
    time_left INTEGER NOT NULL,
	personal_amt INTEGER NOT NULL,
	counter INTEGER,

	created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

	FOREIGN KEY (author_id) REFERENCES child (child_id)
);

/*
TODO: CONNECT task with parent and goal 
UPDATE task -> goal -> bonus - > time 
*/

/*
CREATE TABLE task(
	task_id INTEGER PRIMARY KEY AUTOINCREMENT,
	goal_author_id INTEGER NOT NULL,
	author_id INTEGER NOT NULL,

	task_name INTEGER NOT NULL,
	task_amt INTEGER NOT NULL,

	FOREIGN KEY (goal_author_id) REFERENCES goal (goal_id),
	FOREIGN KEY (author_id) REFERENCES parent (parent_id),

);

*/








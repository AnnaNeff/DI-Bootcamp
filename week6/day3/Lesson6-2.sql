-- Table: advanced_sql.employees

-- DROP TABLE IF EXISTS advanced_sql.employees;

CREATE TABLE IF NOT EXISTS employees
(
    employee_id integer NOT NULL,
    first_name text COLLATE pg_catalog."default" NOT NULL,
    last_name text COLLATE pg_catalog."default" NOT NULL,
    department_id integer NOT NULL,
    CONSTRAINT employees_pkey PRIMARY KEY (employee_id),
    CONSTRAINT department_id_fk FOREIGN KEY (department_id)
        REFERENCES departments (department_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS employees
    OWNER to postgres;
-- Index: fki_department_id_fk

-- DROP INDEX IF EXISTS advanced_sql.fki_department_id_fk;

CREATE INDEX IF NOT EXISTS fki_department_id_fk
    ON advanced_sql.employees USING btree
    (department_id ASC NULLS LAST)
    WITH (fillfactor=100, deduplicate_items=True)
    TABLESPACE pg_default;
-- Table: advanced_sql.departments

-- DROP TABLE IF EXISTS advanced_sql.departments;

CREATE TABLE IF NOT EXISTS departments
(
    department_id integer NOT NULL,
    name text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT departments_pkey PRIMARY KEY (department_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS departments
    OWNER to postgres;

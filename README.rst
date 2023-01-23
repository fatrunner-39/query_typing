Решение на задачу 1

SELECT e.id, e.name, (WITH RECURSIVE all_deps AS(
    SELECT id, parent_id, name 
        FROM departments 
        WHERE id = e.department_id
    UNION ALL
    SELECT d.id, d.parent_id, d.name
        FROM departments d 
        INNER JOIN all_deps
        ON d.parent_id = all_deps.id
        )
    SELECT ARRAY(SELECT id FROM all_deps)) visible_department_ids
        FROM employees e INNER JOIN departments d ON e.department_id = d.id;

USE theater_db;
SELECT 
    p.title AS 'Show Title', 
    p.opening_date AS 'Premiere Date', 
    c.full_name AS 'Lead Actor', 
    c.role_type AS 'Role'
FROM 
    productions p
JOIN 
    cast_members c ON p.production_id = c.production_id
WHERE 
    p.opening_date >= '2026-01-01'
ORDER BY 
    p.opening_date ASC;
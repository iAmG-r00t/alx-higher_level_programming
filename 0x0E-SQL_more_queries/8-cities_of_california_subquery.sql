-- lists all cities of california that can be found in the database
-- where the states table contain only one record where name = california
-- results are sorted in ASC by cities.id
SELECT id, name FROM cities WHERE state_id = (
  SELECT id
  FROM states
  where name='California'
) ORDER BY cities.id ASC;

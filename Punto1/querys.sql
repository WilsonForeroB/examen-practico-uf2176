-- Obtener el id del usuario que su nombre es Juan.
SELECT * FROM nombre_tabla WHERE nombre = 'Juan';

-- Inserta en la base de datos, el usuario Juan, con nombre, apellido y correo. La tabla tiene auto númerico.
INSERT INTO nombre_tabla (nombre, apellido, correo) VALUES ('Juan', 'apellido_Juan', 'correo_Juan');

-- Actualizar el campo edad de Juan a 60 años.
-- Suponiendo que existan varios Juan en la tabla es mejor cambiar la edad sabiendo el id. Asi que asumire que se sabe el id de Juan.
UPDATE nombre_tabla SET edad = 60 WHERE id = id_Juan;

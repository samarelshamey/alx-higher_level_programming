-- Script that lists all privileges of the MySQL users user_0d_1 and user_0d_2
SELECT User, Host, Grant_priv, Create_priv, Insert_priv, Update_priv, Delete_priv, Select_priv
FROM mysql.user
WHERE User IN ('user_0d_1', 'user_0d_2');

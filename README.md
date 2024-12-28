# ProyectoFinalSantinoCalcagnini
# ProyectoFinalSantinoCalcagnini

# Aclaración: El siguiente archivo describe cómo debería funcionar el proyecto. El proyecto aún no funciona del todo, existen algunas funcionalidades que no llegué a pulir.

## Descripción

ProyectoFinalSantinoCalcagnini es una aplicación web desarrollada con Django. El proyecto incluye funcionalidades como la creación, edición y eliminación de posts, autenticación de usuarios, y un sistema de mensajería.

## Funcionalidades

- **Autenticación de Usuarios**: Registro, inicio de sesión y cierre de sesión de usuarios.
- **Gestión de Posts**: Crear, editar, visualizar y eliminar posts.
- **Sistema de Mensajería**: Enviar y recibir mensajes entre usuarios.
- **Perfil de Usuario**: Visualizar y actualizar el perfil de usuario.
- **Cargar Imágenes**: Subir y visualizar imágenes en los posts.
- **Protección de Formularios**: Uso de tokens CSRF para proteger los formularios contra ataques de falsificación de solicitudes.

## Estructura del Proyecto

# Un archivo manage.py

# Un proyecto principal con los settings y urls principales

# Los templates de la página principal

# 3 Apps:
Pagina
Cuentas
Mensajería

Cada una con sus respectivos views, urls, models y templates. 

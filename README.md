# Sistema de Gestión PanCamp

### Descripción
El Sistema de Gestión PanCamp es una solución integral diseñada para optimizar la administración diaria de una panadería. Este sistema permite gestionar eficientemente las ventas, compras y mantener un control detallado del inventario a través de la generación de informes en formato CSV. Su objetivo es facilitar la operación, asegurando un manejo ágil y organizado de productos, proveedores, clientes y empleados.

### Funcionalidades
- Registro de Ventas: Captura y almacena los detalles de cada transacción, incluyendo información del cliente, el empleado responsable y los productos vendidos.
- Registro de Compras: Permite registrar compras a proveedores, detallando los productos adquiridos, cantidades y precios de compra.
- Informe de Ventas: Genera un informe detallado de las ventas realizadas en un formato CSV, permitiendo un análisis sencillo y preciso.
- Informe de Stock: Proporciona un informe del inventario disponible, también en formato CSV, para mantener un control actualizado del stock.

### Estructura del Proyecto
El sistema está organizado en módulos independientes que interactúan entre sí:

- gestion_ventas.py: Módulo encargado de la captura y registro de ventas.
- gestion_compras.py: Módulo utilizado para el registro de las compras realizadas a los proveedores.
- gestion_informes.py: Módulo que gestiona la generación de informes de ventas y stock en formato CSV.
- main.py: Script principal que actúa como interfaz del sistema, permitiendo la interacción con los diferentes módulos.

### Detalles de Implementación

**Registro de Ventas (registrar_venta())**
Este módulo captura los detalles de una venta, incluyendo la información del cliente, empleado y los productos vendidos. Todos los registros se almacenan en un archivo ventas.json para su posterior consulta y generación de informes.

**Registro de Compras (registrar_compra())**
Permite registrar compras de productos a proveedores, almacenando información sobre el proveedor, productos comprados y sus precios. Los registros se guardan en un archivo compras.json.

**Generación de Informe de Ventas (generar_informe_ventas())**
Este módulo crea un informe de ventas en formato CSV, nombrado como informe_ventas_<fecha>.csv, donde <fecha> corresponde al día de generación. Este informe contiene todos los registros de ventas realizados hasta la fecha.

**Generación de Informe de Stock (generar_informe_stock())**
Genera un informe en formato CSV, nombrado como informe_stock_<fecha>.csv, que detalla el inventario disponible en la panadería. Este informe se basa en los registros actualizados del stock.

**Estructura de Datos**
Categorías de Productos
El sistema clasifica los productos en las siguientes categorías:
- Panadería, Pastelería, Bebidas, Promociones
Cada categoría contiene una lista de productos con precios asociados, facilitando el proceso de ventas y compras.

**Control de Stock**
El sistema mantiene un registro actualizado del stock de productos, el cual es fundamental para la generación del informe de stock, asegurando que siempre se tenga visibilidad del inventario disponible.

### Contacto
Para cualquier consulta o sugerencia sobre el proyecto, puedes ponerte en contacto con [Karen Cristancho] a través de [karenlorenacriscaceres@gmail.com].

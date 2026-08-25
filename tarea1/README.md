## 860. Lemonade Change

https://leetcode.com/problems/lemonade-change/description/

Criterio Greedy: Si el cliente pago con $20. Al tener que devolver $15 de cambio, el algoritmo elige siempre entregar primero un billete de $10 y uno de $5, Se elige deshacerse del recurso $10 tan pronto como puede, para proteger y acumular el recurso versátil $5. El algoritmo hace esto a ciegas. No importa si los siguientes 100 clientes van a pagar con $20 o con $5, simplemente asume que retener la moneda más pequeña y versátil siempre será la jugada más segura.

Complejidad: Tiempo O(N) (donde N es el número de clientes, ya que se recorre la lista una sola vez) y Espacio O(1) (solo se usan dos variables enteras para contar, sin importar el tamaño de la entrada).

![Accepted — Lemonade Change](evidencias\lemonade-change-accepted.png)

## 455. Assign Cookies

https://leetcode.com/problems/assign-cookies/description/

Criterio Greedy: Tras ordenar ambos arreglos, en cada paso el algoritmo elige emparejar al niño menos exigente disponible con la galleta más pequeña que logre satisfacerlo, Porque asignar una galleta muy grande a un niño que se conformaba con poco desperdicia recursos que se necesitarán para los niños más exigentes. Si la galleta actual es demasiado pequeña, se descarta definitivamente, ya que al estar ordenados tampoco servirá para ninguno de los siguientes niños.

Complejidad:
Tiempo: O(N log N + M log M), donde N es la cantidad de niños y M la cantidad de galletas. El tiempo está dominado por el ordenamiento inicial sort(). La fase de asignación con los dos punteros toma un tiempo lineal O(N + M).

Espacio: O(1) auxiliar, ya que solo se utilizan un par de variables para los punteros, operando sobre los arreglos directamente.

![Accepted — Assign Cookies](evidencias\assign-cookies-accepted.png)

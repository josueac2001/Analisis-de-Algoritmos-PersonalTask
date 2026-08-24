https://leetcode.com/problems/lemonade-change/description/

Criterio Greedy: Al tener que devolver $15 de cambio (pago con $20), el algoritmo elige siempre entregar primero un billete de $10 y uno de $5, Se elige deshacerse del recurso $10 tan pronto como puede, para proteger y acumular el recurso versátil $5. El algoritmo hace esto a ciegas. No importa si los siguientes 100 clientes van a pagar con $20 o con $5, simplemente asume que retener la moneda más pequeña y versátil siempre será la jugada más segura.

Complejidad: Tiempo O(N) (donde N es el número de clientes, ya que se recorre la lista una sola vez) y Espacio O(1) (solo se usan dos variables enteras para contar, sin importar el tamaño de la entrada).

![Accepted — Lemonade Change](evidencias\lemonade-change-accepted.png)

## 88. Merge Sorted Array

https://leetcode.com/problems/merge-sorted-array/description/

Estrategia (Two Pointers in-place): Como nums1 tiene espacio vacío al final, utilizamos dos punteros empezando desde el final de ambos arreglos válidos. Comparamos los últimos elementos de nums1 y nums2, colocando el mayor en la última posición disponible de nums1. Se escribe de atrás hacia adelante para no sobreescribir los valores originales de nums1 que aún no han sido procesados.

Complejidad:
Tiempo: O(m + n), ya que en el peor de los casos se recorren todos los elementos de ambos arreglos una sola vez. Se cumple el requisito (Follow up) de LeetCode.
Espacio: O(1) auxiliar, porque se modifica nums1 directamente sin crear arreglos adicionales.

![Accepted — Merge Sorted Array](evidencias/merge-sorted-array-accepted.png)
# 3.6 Análisis de Complejidad Algorítmica (Big-O)

---

## 1. Análisis de la Tabla Hash (Eliminación de repetidos)

* **Mejor caso y Caso Promedio:** $\mathcal{O}(1)$ por búsqueda e inserción. Asumiendo una distribución uniforme en los *buckets*, el procesamiento total de $n$ palabras toma $\mathcal{O}(n)$.
* **Peor caso:** $\mathcal{O}(n)$ por operación en caso de colisiones masivas (todas las palabras cayendo en el mismo *bucket*), degradando el tiempo total a $\mathcal{O}(n^2)$.
* **Complejidad Espacial:** $\mathcal{O}(n)$ para almacenar las palabras únicas.

---

## 2. Comparativa de Algoritmos de Ordenamiento

### A. Merge Sort
* **Complejidad Temporal:** $\mathcal{O}(n \log n)$ constante en el mejor, promedio y peor caso. Divide el problema en $\log n$ niveles y realiza $n$ comparaciones para combinar.
* **Complejidad Espacial:** $\mathcal{O}(n)$ debido a las estructuras auxiliares necesarias durante la división y mezcla.

### B. Quick Sort
* **Mejor caso y Caso Promedio:** $\mathcal{O}(n \log n)$, alcanzado cuando la elección del pivote divide el conjunto de datos de manera equitativa.
* **Peor caso:** $\mathcal{O}(n^2)$, cuando el pivote resulta ser consistentemente el menor o mayor elemento.
* **Complejidad Espacial:** $\mathcal{O}(\log n)$ en el caso promedio debido a la pila de llamadas recursivas.

---

## 3. Contraste Teórico vs. Resultados Empíricos (Punto 5)

Al comparar las complejidades teóricas con las mediciones empíricas obtenidas en las pruebas con textos de ~100, ~1,000 y ~10,000 palabras:

1. **Comportamiento Asintótico:** Al incrementar el tamaño de la entrada por un factor de $10\times$, el tiempo de ejecución no aumentó de forma cuadrática ($100\times$), lo cual confirma el comportamiento teórico de $\mathcal{O}(n \log n)$ en lugar de $\mathcal{O}(n^2)$.
2. **Diferencias Prácticas:** Aunque ambos algoritmos comparten una complejidad promedio de $\mathcal{O}(n \log n)$, la implementación de **Quick Sort** suele presentar menor *overhead* de memoria en comparación con **Merge Sort**.

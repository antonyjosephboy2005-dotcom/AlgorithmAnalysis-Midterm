# Midterm Assignment Report: Algorithm Analysis
**Course:** Algorithm Analysis (2025-2026 Fall Semester)[cite: 1, 2]  
**Lecturer:** Dr. Coşkun Şahin  
**Student Name:** [Adeniyi Olueadarasimi Joseph]  
**Student Number:** [2422190020]  
**Program:** Software Engineering (English)[cite: 1]  

---

## 1. Introduction
For this midterm project assignment, two fundamental sorting algorithms were selected for implementation and analysis: **Bubble Sort** and **Insertion Sort**. Both algorithms are comparison-based sorting techniques that operate in-place, making them excellent candidates for educational analysis regarding CPU time complexity and memory efficiency.

---

## 2. Explanation of Selected Algorithms

### Bubble Sort
Bubble Sort is a straightforward sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted. Larger elements "bubble" up to the end of the array with each full iteration.

### Insertion Sort
Insertion Sort builds the final sorted array one item at a time. It takes an element from the input data, finds its correct position in the already-sorted sub-list, and inserts it there. It iterates through the input consuming one element each repetition, and growing a sorted output list.

---

## 3. Complexity Analysis (CPU & Memory Workload)

| Algorithm | Best-Case Time (CPU) | Average-Case Time (CPU) | Worst-Case Time (CPU) | Space Complexity (Memory) |
| :--- | :--- | :--- | :--- | :--- |
| **Bubble Sort** | $O(n)$ *(with optimization)* | $O(n^2)$ | $O(n^2)$ | $O(1)$ |
| **Insertion Sort** | $O(n)$ *(already sorted)* | $O(n^2)$ | $O(n^2)$ *(reverse sorted)* | $O(1)$ |

* **CPU Workload (Time Complexity):** 
  * *Bubble Sort* takes $O(n^2)$ comparisons and swaps in the average and worst cases because of its nested loops. However, with an optimized early-exit flag, its best-case drops to $O(n)$ if the array is already sorted.
  * *Insertion Sort* also operates at $O(n^2)$ for average and worst cases (like a reverse-ordered array), but its best case is $O(n)$ when processing an already sorted array because the inner loop terminates immediately.
* **Memory Workload (Space Complexity):** 
  * Both algorithms have a space complexity of **$O(1)$** because they sort the data *in-place*, meaning they require a constant amount of extra memory space regardless of the input size.

---

## 4. Comparison and Best Use Cases

* **Comparison:** While both algorithms share an average-case time complexity of $O(n^2)$, **Insertion Sort** generally performs better in practice than Bubble Sort. Insertion Sort does fewer total writes/swaps and adapts much faster to partially sorted datasets.
* **Best Use Cases:**
  * **Insertion Sort** is ideal for small data sets or arrays that are already substantially sorted, as well as online sorting where elements are received streaming in real-time.
  * **Bubble Sort** is primarily used for educational purposes to introduce fundamental concepts of iteration, comparisons, and algorithm optimization checks.

---

## 5. AI Usage Statement
[Gemini (Google AI)] was used in the [Code generation and Report structure] section of this product. The tool was utilized via the prompt/input "Help me write, structure, and analyze Bubble Sort and Insertion Sort for my algorithm assignment" for the purpose of [Code generation / Algorithm editing / Documentation / Text correction]. The output generated has been reviewed and verified by me for technical accuracy, safety, and originality. I bear full responsibility for the work[cite: 1].
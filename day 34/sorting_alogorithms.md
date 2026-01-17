# Sorting Algorithms – Overview

This repository covers commonly used sorting algorithms along with their
time and space complexity. These algorithms are fundamental for understanding
data structures and problem-solving in computer science.

---

## 1. Bubble Sort

**Idea:**  
Repeatedly compare adjacent elements and swap them if they are in the wrong order.

**Time Complexity:**
- Best Case: O(n) (already sorted)
- Average Case: O(n²)
- Worst Case: O(n²)

**Space Complexity:**  
- O(1) (In-place)

**Properties:**
- Stable: Yes  
- Adaptive: Yes  
- In-place: Yes  

---

## 2. Insertion Sort

**Idea:**  
Insert each element into its correct position in the sorted part of the array.

**Time Complexity:**
- Best Case: O(n)  
- Average Case: O(n²)  
- Worst Case: O(n²)  

**Space Complexity:**  
- O(1) (In-place)

**Properties:**
- Stable: Yes  
- Adaptive: Yes  
- In-place: Yes  

---

## 3. Selection Sort

**Idea:**  
Repeatedly select the minimum element and place it at the beginning.

**Time Complexity:**
- Best Case: O(n²)  
- Average Case: O(n²)  
- Worst Case: O(n²)  

**Space Complexity:**  
- O(1) (In-place)

**Properties:**
- Stable: No  
- Adaptive: No  
- In-place: Yes  

---

## 4. Merge Sort

**Idea:**  
Divide the array into halves, sort them, and merge the sorted halves.

**Time Complexity:**
- Best Case: O(n log n)  
- Average Case: O(n log n)  
- Worst Case: O(n log n)  

**Space Complexity:**  
- O(n)

**Properties:**
- Stable: Yes  
- Adaptive: No  
- In-place: No  

---

## 5. Quick Sort

**Idea:**  
Pick a pivot element and partition the array around the pivot.

**Time Complexity:**
- Best Case: O(n log n)  
- Average Case: O(n log n)  
- Worst Case: O(n²)  

**Space Complexity:**  
- O(log n) (recursive stack)

**Properties:**
- Stable: No  
- Adaptive: No  
- In-place: Yes  

---

## 6. Counting Sort

**Idea:**  
Count the frequency of each element and use it to place elements in sorted order.

**Time Complexity:**
- Best Case: O(n + k)  
- Average Case: O(n + k)  
- Worst Case: O(n + k)  
  (k = range of input values)

**Space Complexity:**  
- O(n + k)

**Properties:**
- Stable: Yes  
- Adaptive: No  
- In-place: No  

---

## Quick Comparison Table

| Algorithm       | Best       | Average    | Worst      | Space   | Stable | In-place |
|-----------------|------------|------------|------------|---------|--------|----------|
| Bubble Sort     | O(n)       | O(n²)      | O(n²)      | O(1)    | Yes    | Yes      |
| Insertion Sort  | O(n)       | O(n²)      | O(n²)      | O(1)    | Yes    | Yes      |
| Selection Sort  | O(n²)      | O(n²)      | O(n²)      | O(1)    | No     | Yes      |
| Merge Sort      | O(n log n) | O(n log n) | O(n log n) | O(n)    | Yes    | No       |
| Quick Sort      | O(n log n) | O(n log n) | O(n²)      | O(log n)| No     | Yes      |
| Counting Sort   | O(n + k)   | O(n + k)   | O(n + k)   | O(n + k)| Yes    | No       |

---

## Status
- Bubble Sort: Completed
- Insertio

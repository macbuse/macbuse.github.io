# Rolling dice


Here’s a table showing the possible outcomes when rolling two six-sided dice. The rows represent the result of the first die, and the columns represent the result of the second die. Each cell contains the sum of the two dice.

| 🎲1\🎲2 | 1  | 2  | 3  | 4  | 5  | 6  |
|--------|----|----|----|----|----|----|
| **1**  | 2  | 3  | 4  | 5  | 6  | 7  |
| **2**  | 3  | 4  | 5  | 6  | 7  | 8  |
| **3**  | 4  | 5  | 6  | 7  | 8  | 9  |
| **4**  | 5  | 6  | 7  | 8  | 9  | 10 |
| **5**  | 6  | 7  | 8  | 9  | 10 | 11 |
| **6**  | 7  | 8  | 9  | 10 | 11 | 12 |

Each sum appears with different probabilities, with 7 being the most common outcome. Let me know if you need additional details! 🎲

Sure! Here's a more detailed breakdown of the possible outcomes when rolling two six-sided dice.

### **Understanding the Table**
- The **rows** represent the result of rolling the first die (1–6).
- The **columns** represent the result of rolling the second die (1–6).
- Each cell in the table contains the **sum** of the two dice.

### **Expanded Table of Outcomes**
| 🎲1\🎲2 | **1** | **2** | **3** | **4** | **5** | **6** |
|--------|------|------|------|------|------|------|
| **1**  | **2**  | 3  | 4  | 5  | 6  | 7  |
| **2**  | 3  | **4**  | 5  | 6  | 7  | 8  |
| **3**  | 4  | 5  | **6**  | 7  | 8  | 9  |
| **4**  | 5  | 6  | 7  | **8**  | 9  | 10 |
| **5**  | 6  | 7  | 8  | 9  | **10** | 11 |
| **6**  | 7  | 8  | 9  | 10 | 11 | **12** |

### **Probability of Each Sum**
Since each die has 6 sides, there are **6 × 6 = 36 total possible outcomes**. Some sums occur more frequently than others:

| **Sum** | **Ways to Get It** | **Probability** |
|---------|------------------|--------------|
| **2**  | (1,1)  | **1/36** ≈ 2.78% |
| **3**  | (1,2), (2,1)  | **2/36** ≈ 5.56% |
| **4**  | (1,3), (2,2), (3,1)  | **3/36** ≈ 8.33% |
| **5**  | (1,4), (2,3), (3,2), (4,1)  | **4/36** ≈ 11.11% |
| **6**  | (1,5), (2,4), (3,3), (4,2), (5,1)  | **5/36** ≈ 13.89% |
| **7**  | (1,6), (2,5), (3,4), (4,3), (5,2), (6,1)  | **6/36** ≈ 16.67% |
| **8**  | (2,6), (3,5), (4,4), (5,3), (6,2)  | **5/36** ≈ 13.89% |
| **9**  | (3,6), (4,5), (5,4), (6,3)  | **4/36** ≈ 11.11% |
| **10** | (4,6), (5,5), (6,4)  | **3/36** ≈ 8.33% |
| **11** | (5,6), (6,5)  | **2/36** ≈ 5.56% |
| **12** | (6,6)  | **1/36** ≈ 2.78% |

### **Key Takeaways**
- The most common sum is **7**, occurring **16.67%** of the time.
- The least common sums are **2 and 12**, each occurring **2.78%** of the time.
- The probabilities are **symmetrical**, meaning sums on opposite ends (e.g., 3 & 11, 4 & 10) have the same likelihood.

Would you like a visual representation, such as a probability chart? 😊

![Dice Probability Chart](./dice.png)

---


If you roll **a large number of dice** (e.g., 1000 six-sided dice), the sum will follow a **normal distribution (bell curve)** due to the **central limit theorem**. 

### **What Happens When Rolling Many Dice?**
- The **minimum sum** is **1000** (if all dice roll 1).
- The **maximum sum** is **6000** (if all dice roll 6).
- The **most common sum** will be around the **average**, which is:

  \[
  \text{Average sum} = 1000 \times \frac{(1+6)}{2} = 3500
  \]

- The distribution will be **bell-shaped**, with most results clustering near **3500**, and fewer results near **1000** or **6000**.

### **Let’s Simulate Rolling 1000 Dice**
I'll generate a histogram to visualize the distribution.

Here’s the distribution of sums when rolling **1000 six-sided dice** multiple times. As expected, it forms a **bell curve (normal distribution)** centered around **3500**, with very few results near the extremes (1000 or 6000). 

![Dice Simulation](./ddd.png)

This happens because as the number of dice increases, the distribution of sums becomes more **symmetrical and predictable** due to the central limit theorem. 

Let me know if you want to tweak the simulation! 🎲📊


---

## Fail


To calculate the probability of rolling the same number at least **3 times in a row** over **10 rolls of a fair six-sided die**, we need to account for streaks of three or more consecutive identical results.

### **Approach**
1. **Simulate Rolling a Die**: We generate 10 dice rolls and check if any number appears **at least** 3 times consecutively.
2. **Monte Carlo Simulation**: Since calculating this exactly with combinatorics is complex, we can estimate the probability by simulating the process many times.

Let me run the simulation and give you an estimate. 🎲

It seems like I can’t do more advanced data analysis right now. Please try again later. If you'd like, I can explain the general approach or walk you through how to run the simulation yourself in Python. Let me know how you'd like to proceed!

# **Performance Optimization Assignment**

## **Task Overview**

You are provided with a Python function that currently takes **8 seconds** to complete. Your goal is to optimize the function so that it runs in **under 3 seconds** while maintaining the correct output.

## **Objective**

- **Current Execution Time**: 8 seconds.
- **Goal**: Optimize the function to run in **under 3 seconds**.
- **Output**: Ensure the function produces the same correct result.

## **Environment requirements**

Python version 3.7 or newer is needed. If you haven't installed Python, you can install Python from https://www.python.org/downloads/

## **Instructions**

1. **Run Setup**: Execute the following command to start the local Ethereum blockchain using Ganache:
    ```bash
    python3 setup_ganache.py
    ```
    This will set up the local blockchain for your application. Once Ganache is running, you can proceed to the next step.
    
2. **Run Code**: Execute the following command to run the code:
    ```bash
    python3 main.py
    ```
3. **Review the Code**: Review the provided Python code and understand its functionality and current performance. The function currently takes **8 seconds** to complete for typical input.

4. **Optimize the Code**: Identify bottlenecks and improve performance (e.g., more efficient algorithms, data structures).
    
5. **Test the Code**: Ensure the function runs correctly and meets the time requirement (under 3 seconds).

6. **Submit**: Provide your optimized code and an explanation of the changes you made.

## **Deliverables**

- **Optimized Code**: Your improved version of the function.
- **Explanation**: A brief description of what optimizations you made.
- **Performance**: Ensure the function runs in under 3 seconds.

## **Evaluation Criteria**

Your solution will be evaluated based on the following criteria:

- **Time Complexity**: Did you reduce the time complexity of the function? If so, by how much?
- **Execution Time**: Does the function now run in under 3 seconds?
- **Code Quality**: Is the code clean, readable, and efficient?

**Note**: You are only allowed to use `threading` or `asyncio`. You are **not allowed** to use any libraries.

# Fetch Rewards

#### Testing Website: http://sdetchallenge.fetch.com/
#### Tools: Python, Selenium and Chrome WebDriver

This algorithm is designed to find a fake gold bar among a set of 9 identical-looking gold bars using a balance scale. The key objectives are to minimize the number of weighings and comparisons, resulting in an efficient solution with a time and space complexity of O(1).

## Problem Statement
You are given 9 gold bars that look identical, except for one fake bar, which weighs less than the others. Your goal is to determine which gold bar is fake using a balance scale. You can only place gold bars on the scale plates and find out which side weighs more or less.

## Strategy
1. Divide the gold bars into three groups: A, B, and C, each containing three bars.

2. Compare groups A and B on the balance scale.
    - If the scale is balanced, the fake bar is in group C.
    - If the scale is unbalanced, let's say group A is heavier, the fake bar is in group B or vice versa.

3. Divide the group containing the fake bar (group A or group B) into individual bars: X1, X2, and X3.

4. Compare X1 and X2 on the balance scale.

    - If the scale is balanced, the fake bar is X3.- If the scale is unbalanced, let's say X1 and is heavier, the fake bar is either X2 or vice versa.

The total time complexity of the algorithm is O(1) because the number of bars and groups involved remains constant. The space complexity is also O(1) as you only need a small constant amount of memory to keep track of the bars and groups.

## Steps for running the code

1. Install Python

2. Install Chrome WebDriver
3. Install all requirements using this command
    
        pip install -r requirements.txt

4. Run the test automation code using this command

        python3 app.py
# Problem 209. Minimum Size Subarray Sum

### Solution Video Link
`https://www.youtube.com/watch?v=aYqYMIqZx5s`

### Explanation

## Brute Force
- Time complexity: O(n^2)
- Space complexity: O(1)

1. Using nested for loop, check each window if sum >= target
2. If valid window, save the window size (if smallest recorded yet)

## Sliding Window Algorithm 
- Time complexity: O(n)
- Space complexity: O(1) --> just uses pointers, no extra data structures

1. Use two pointers left (l) and right (r) to capture a "window"
2. Add value at r to the total sum of window
    - a. If the total is >= target then we know: *sum of all items up to right pointer*
    - b. This means we should check if there is a smaller sub-window in our window that qualifies
    - c. Since window wasn't valid until current r, we know no possible subwindows starting at l
    - d. We subtract value at l from total, and iterate l++ to check new window
    - e. If qualifies we continue checking smaller subwindow, else we continue iterating r until end of array
